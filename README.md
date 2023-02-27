# Portfolio-Risk-Management

Submitted by: **NING YANG**

Time spent: **20** hours spent in total

Tools Used: Python (pandas, numpy, scipy, matplotlib and pypfopt)

This project is a part of Course CS7646-  Machine Learning for Trading in Georgia Institute of Technology.


## Description

The optimization.py code returns several portfolio statistics: stock allocations (allocs), cumulative return (cr), average daily return (adr), standard deviation of daily returns (sddr), and Sharpe ratio (sr). This project builds upon what we learned about portfolio performance metrics and optimizers to optimize a portfolio. That means that we will find how much of a portfolio’s funds should be allocated to each stock to optimize its performance. While a portfolio can be optimized for many different metrics, in this version of the assignment we will maximize the Sharpe Ratio. 

## Goal

Revise the code to implement a Python function named optimize_portfolio() in the file optimization.py that can find the optimal allocations for a given set of stocks. Optimize for maximum Sharpe Ratio taking long positions only.


## Lessons learned

In addition to the assignment requirements, I also measured expected value of losses by accessing Value at Risk (VaR) and Conditional Value at Risk (CVaR), run Monte Carlo simulation to predict uncertainty.I figured out the factors that are driving the portfolio returns, construct market-cap weighted equity portfolios, and forecast and hedge market risk via scenario generation.




## License

    Copyright [2023] [NING YANG]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
