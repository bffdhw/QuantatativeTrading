# QuantitativeTrading

For quantitative trading strategies backup.

Some trading strategies back-testing on Taiwan futures market. 

## 3 Step to ideate a quantitative trading strategy
- Indicator : What kind of information about the data we want to use for trading(Such as price, KD, MACD etc.).
- Signal : What kind of condition will trigger the transaction(Such as the price rose by 3.5 percent).
- Method : What to do while the signal being triggered(buy/sell).


## How to start

- Collect your own data and preprocess it to fit the following structure

|  | date | time | o | h | l | c | 
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 2018/12/20 | 08:46:00 | 9640 | 9640 | 9630 | 9630 |
| 1 | 2018/12/20 | 08:47:00 | 9630 | 9640 | 9630 | 9640 |
| 2 | 2018/12/20 | 08:48:00 | 9640 | 9640 | 9630 | 9640 |
| 3 | 2018/12/20 | 08:49:00 | 9640 | 9650 | 9640 | 9650 |
| 4 | 2018/12/20 | 08:50:00 | 9640 | 9650 | 9640 | 9640 |

- These trading strategies are developed for Taiwan futures market, but you can still collect any kind of data to apply these strategies.
- Run strategies code 
