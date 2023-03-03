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

## Functions update

### Adjust long & short timing to make the transatcions more reasonable

- Long : Use highest price as long price
- Stop loss : Use (long_price - stop_loss_point) as short price, so the profit will be the value of given stop_loss_point

### Adjust the calculation of volatility at preprocessing part

- Original : The distance between close price and last close price
- New : The distance between highest price and last lowest price

### Consider the cost of fee and slippage

- Slippage : 2 points each transaction
- Fee : 1 point each selling transaction  

### Without the limit on transaction times
Without the limit on transaction times in a day, but still only holding 1 position at a time.

### Seems that making multiple transactions in a day is not a good idea

Sum: 617   
Win: 114    
Lose: 503  
Odds: 0.1847649918962723  
Cum: -2156.0  
PF: 0.8288209606986899  
MDD: 2862.0

![Figure 2023-03-02 220922](https://user-images.githubusercontent.com/34659552/222451948-05e5aca9-c0c3-40e2-914f-c0bb3eabbf25.png)


### Finding profitable parameters using for loop

- Top 5 performance parameters   
- Find the whole performance record at 'performance.pkl'    

|  | stop loss | threshold |
| --- | --- | --- |
| 0 | 25 | 0.028 |
| 1 | 30 | 0.028 |
| 2 | 35 | 0.028 |
| 3 | 40 | 0.028 |
| 4 | 45 | 0.028 |

The result of setting parameters as stop_loss:25, threshold:0.0028

Sum: 5  
Win: 2  
Lose: 3  
Odds: 0.4  
Cum: 556.0  
PF: 7.177777777777778  
MDD: 60.0  

![Figure 2023-03-03 114041](https://user-images.githubusercontent.com/34659552/222625866-68e672f0-6258-42a1-a0c7-9d0053aee677.png)

We can see that the total number of transaction only 5 times.  
Although they're extreamly profitable, that's not stable enough.

Also we can found that the profitable performance always be made while the parameter 'threshohd' being set over 0.01. 
But this condiction doesn't appear frequently in just 1 minute.
In other word, this signal might not be very good. 

In my opinion, maybe there's still some way to save this strategy :
-  Change the time which threshold is considered from 1 minute to 3 min, 5 min, or maybe other longer time to find the rising trend more clearly.  
-  Allow holding multiple positions at a time to increase the total times of transactions.
-  Go back to the time we just make 1 transaction, and tune the parameters.
