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


### Consider the cost of fee and slippage
