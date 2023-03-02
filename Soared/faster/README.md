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
