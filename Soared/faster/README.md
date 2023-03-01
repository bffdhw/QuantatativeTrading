## Result

### Original
Sum: 246  
Win: 67  
Lose: 179  
Odds: 0.27235772357723576  
Cum: 1882.0  
PF: 1.4280191039345007  
MDD: 367.0  

![Figure 2023-02-09 002922](https://user-images.githubusercontent.com/34659552/217591381-591efa46-821c-45aa-ba19-2fdce3065edf.png)

### Settlement date considered
Sum: 246  
Win: 66  
Lose: 180  
Odds: 0.2682926829268293  
Cum: 2004.0  
PF: 1.4547311095983662  
MDD: 358.0  

![Figure 2023-02-20 113821](https://user-images.githubusercontent.com/34659552/220004071-4ace9cb8-fd6b-48a6-8a91-97a616ecc897.png)


### Without the limit on transaction times
Without the limit on transaction times in a day, but still only holding 1 position at a time.

Sum: 338  
Win: 86  
Lose: 252  
Odds: 0.25443786982248523  
Cum: 4526.0  
PF: 1.6857575757575758  
MDD: 693.0  

![Figure 2023-02-20 114139](https://user-images.githubusercontent.com/34659552/220005031-656c9c82-6c82-46d4-82ce-d84b41daea9d.png)

### Adjust long & short timing to make the transatcions more reasonable

- Long : Use highest price as long price
- Stop loss : Use (long_price - stop_loss_point) as short price, so the profit will be the value of given stop_loss_point

Sum: 343  
Win: 68    
Lose: 275  
Odds: 0.19825072886297376  
Cum: 3076.0  
PF: 1.5627515550676911  
MDD: 544.0  

![Figure 2023-02-22 154421](https://user-images.githubusercontent.com/34659552/220555383-8ed8ec57-7861-451e-818b-305dc579c156.png)

### Adjust the calculation of volatility at preprocessing part

- Original : The distance between close price and last close price
- New : The distance between highest price and last lowest price

Sum: 909   
Win: 236    
Lose: 673  
Odds: 0.25962596259625964  
Cum: 16559.0  
PF: 2.237593423019432  
MDD: 1064.0  
![Figure 2023-02-22 160606](https://user-images.githubusercontent.com/34659552/220559828-fec55ab9-5b8a-41d7-b46c-fab8e7c16d3b.png)


### Consider the cost of fee and slippage

- Slippage : 2 points each transaction
- Fee : 1 point each selling transaction

Sum: 909  
Win: 235    
Lose: 674  
Odds: 0.2585258525852585  
Cum: 12014.0  
PF: 1.7174250567299654  
MDD: 1564.0  
![Figure 2023-02-22 161050](https://user-images.githubusercontent.com/34659552/220561051-fa7e509a-d3c5-4c39-8c88-dabd6f91249e.png)

### Visualize and trying to find the most profitable time in a day 
Trying to design a filter based on time to reduce non-profitable transaction in the next step.
![Figure 2023-02-23 202425](https://user-images.githubusercontent.com/34659552/220905566-5ef2a594-308d-41e1-b2eb-e8321aed4848.png)

![Figure 2023-02-23 232959](https://user-images.githubusercontent.com/34659552/220955731-b02a9ee7-91a9-46da-96af-0328c824b753.png)

Seems that time will be a great filter to pick the profitable transatcion.  

### Easy way using GA to find optimal parameters
- Pakage name : Scikit-opt
- Install : pip install sciket-opt
- Parameters : x point to stop loss, and y percentage the price rise for the long transaction signal.
- GA will be used here to find the optimal parameters. 
- Optimal parameter found : Stop_loss :38 , threshold : 0.00107685

Sum: 8671  
Win: 5564  
Lose: 3107  
Odds: 0.6416791604197901  
Cum: 291477.0  
PF: 4.471079989996785  
MDD: 2435.0  

![Figure 2023-02-27 150858](https://user-images.githubusercontent.com/34659552/221498044-863e24a0-791c-4aec-9cd3-f6581a5c4c33.png)


### Sometimes maybe just use the for loop
- Top 5 performance parameters   
- Find the whole performance record at 'performance.pkl'    

|  | stop loss | threshold |
| --- | --- | --- |
| 0 | 40 | 0.001 |
| 1 | 35 | 0.001 |
| 2 | 45 | 0.001 |
| 3 | 50 | 0.001 |
| 4 | 30 | 0.001 |

Parameters : stop_loss :40, threshold : 0.001  
Sum: 10254  
Win: 6620    
Lose: 3634  
Odds: 0.6456017164033548  
Cum: 331676.0  
PF: 4.5724779733310355  
MDD: 2204.0  

![Figure 2023-02-27 221729](https://user-images.githubusercontent.com/34659552/221587737-c43c56be-83fa-43d0-b001-90e98a4f0fbb.png)


# It must be something wrong

The result it too good to be true.
Still finding if there is some logical bug in the code.
