# QuantitativeTrading

For quantitative trading strategies backup.

Some trading strategies back-testing on Taiwan futures market. 

## 3 Step to ideate a quantitative trading strategy
- Indicator : What kind of information about the data we want to use for trading(Such as price, KD, MACD etc.).
- Signal : What kind of condition will trigger the transaction(Such as the price rose by 3.5 percent).
- Method : What to do while the signal being triggered(buy/sell).

## About this strategy
- It's a trend following and day trading strategy.
- Back-test on Taiwan futures market(Code:TX).

## About the data
- Period : 2018/12/10 ~ 2021/06/16
- Frequency : 1min

## Strategy description
- If he price rose by 0.3 percent in 1min(1 candlestick), long 1 position.
- Stop the loss at 20 point, close the position.
- If doesn't stop the loss, then close the position at the end of each day.
- Maximum 1 time transaction each day(just for convenience).

## Result
Sum: 246  
Win: 67  
Lose: 179  
Odds: 0.27235772357723576  
Cum: 1882.0  
PF: 1.4280191039345007  
MDD: 367.0  

![Figure 2023-02-09 002922](https://user-images.githubusercontent.com/34659552/217591381-591efa46-821c-45aa-ba19-2fdce3065edf.png)
