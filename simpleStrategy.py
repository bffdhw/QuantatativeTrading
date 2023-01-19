# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 16:51:37 2021

@author: Longer
"""

import pandas as pd
from datetime import datetime

#index_col=0get rid of "Unnamed: 0" column in a pandas 
#index_col=0 : 避免讀取csv後出現unnamed欄位
df = pd.read_csv('./raw_m.csv', index_col=0)

'''
================= preprocess =================
'''

#String to datetime
#轉換字串為時間格式
df['time']= pd.to_datetime(df['time']).dt.time
df['date']= pd.to_datetime(df['date']).dt.date

#set market opening/closing time (or back testing period in a day)
#設定要擷取的資料期間
start_time = datetime.strptime('08:46', '%H:%M').time()
end_time   = datetime.strptime("13:29", '%H:%M').time()

#to get "last candle stick closing price" for this strategy
#新增column，紀錄前1根K棒收盤價
df['prev_c'] = df['c'].shift()

#got 1 row of NA at column "prev_c", drop it
#首筆資料沒有前面的K棒資料，drop
df = df.dropna()

#calculate the volatility of price (closing price)
#計算漲跌幅(未轉換為百分比)
df['vol'] = (df['c'].astype(int) - df['prev_c'].astype(int))/ df['prev_c'].astype(int)


'''
================= trading parameter =================
'''

#how much unit holding right now
#部位大小
position = 0 

#the cost of  each time trading
#每次交易的成本
cost = 0 

#to determine transaction is done or not
#紀錄本日是否已交易，True表示已交易，則今日不再交易
flag = False 

#set stop loss price
stop_loss = -20


'''
================= evaluation parameter =================
'''

#profit >= 0 at the end of each day
win=0
#profit < 0 at the end of each day
lose=0

#cumsum of profit
cum = 0

#vector about each profit record of transaction 
pl=[] #單筆損益
#vector about each cumsum profit record of transaction 
PnL=[] #累計損益

#recording which day triggered the transaction signal
date=[]

#vector about each profit record of win/lose
#to calculate "profit factor" for evaluation
win_list=[]
lose_list=[]

#how many time transaction has been made
#交易次數
num = 0

'''
================= strategy =================
'''

for i in range(0,len(df)):

    #refresh the flag to False at the first candle stick of each day
    #8:46，表示換日，刷新flag為False
    if df.iloc[i]["time"] == start_time:
        flag=False    

    #if meet the condition, then triggered the transaction 
    #一分K急漲0.03%、目前未持有部位、今日尚未交易，以收盤價新倉1口  
    if df.iloc[i]["vol"] > 0.003 and not position and not flag:
        
        #set position to 1
        #部位 = 1
        position = 1 
        
        #recording the buying price as cost
        #cost紀錄成本價格  
        cost = df.iloc[i]["c"] 
        
        #set the flag true, means already make a transaction today
        #flag紀錄已交易         
        flag = True    
        
        #add 1 to total transaction times 
        #總交易次數+1
        num = num + 1
        
        #just print
        print("新倉")
        print(df.iloc[i]["date"],df.iloc[i]["time"])
        print("\n")
        
        
        
        
    #if meet stopping loss condition
    #達停損條件、目前持有部位，停損
    if (df.iloc[i]["c"] - cost) <= stop_loss and position :
        
        #sell all position
        #平倉，部位歸零
        position=0
        
        #stop loss means lose
        #輸的次數+1
        lose = lose+1
        
        #apppend transaction profit at this transaction
        #紀錄單次損益
        pl.append(df.iloc[i]["c"] - cost)
        
        #calculate cumsum 
        #計算累計損益
        cum = cum + df.iloc[i]["c"]-cost
        
        #append records to each vector about the transaction
        #新增此筆交易各項紀錄
        PnL.append(cum)
        date.append(df.iloc[i]["date"])
        lose_list.append(df.iloc[i]["c"] - cost)
        
        #just print
        print("停損")
        print(df.iloc[i]["c"] - cost)
        print("\n")    
    
       
    #if meet the end of the date, sell all position(if there is)
    #13:29，表示此筆資料為當天最後一根分K，平倉
    if (df.iloc[i]["time"] == end_time) and position:
        
        #sell all position
        #平倉，部位歸零
        position=0
        
        #determine win/lose
        #判斷輸贏
        if df.iloc[i]["c"]-cost>=0 :
            win = win+1
            win_list.append(df.iloc[i]["c"] - cost)
        else :
            lose = lose+1
            lose_list.append(df.iloc[i]["c"] - cost)
        
        #apppend transaction profit at this transaction
        #紀錄單次損益
        pl.append(df.iloc[i]["c"]-cost)
        
        #calculate cumsum 
        #計算累計損益
        cum= cum + df.iloc[i]["c"]-cost
        
        #append records to each vector about the transaction
        #新增此筆交易各項紀錄
        PnL.append(cum)
        date.append(df.iloc[i]["date"])
        
        #just print
        print("當日平倉")
        print(df.iloc[i]["c"]-cost)
        print(cum)
        print("\n")
           
'''
================= evaluate =================
'''

print("Sum:",num)
print("Win:",win," Lose:",lose)
print("Odds:",win/num)
print("Cum:",cum)
print("PF:",sum(win_list)/(sum(lose_list)*-1))

#calculate MDD
high=0
high2=0
dd=0
dd_list=[]
for i in PnL:
    #累計損益創新高，刷新high
    if i>high:
        high=i
    #累計損益小於前一次新高，回檔開始
    if i<high:
        #
        if (high-i)>dd:
            dd=high-i
            dd_list.append(dd)
    if i==high:
        dd=0
print("MDD:", max(dd_list))
        

'''
================= cumsum line plot =================
'''
df_plot= pd.DataFrame(PnL,index=date,columns=["PnL"])
df_plot.plot(rot=45)