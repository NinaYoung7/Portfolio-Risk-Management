""""""  		  	   		  		 			  		 			     			  	 
"""MC1-P2: Optimize a portfolio.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		  		 			  		 			     			  	 
Atlanta, Georgia 30332  		  	   		  		 			  		 			     			  	 
All Rights Reserved  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
Template code for CS 4646/7646  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		  		 			  		 			     			  	 
works, including solutions to the projects assigned in this course. Students  		  	   		  		 			  		 			     			  	 
and other users of this template code are advised not to share it with others  		  	   		  		 			  		 			     			  	 
or to make it available on publicly viewable websites including repositories  		  	   		  		 			  		 			     			  	 
such as github and gitlab.  This copyright statement should not be removed  		  	   		  		 			  		 			     			  	 
or edited.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
We do grant permission to share solutions privately with non-students such  		  	   		  		 			  		 			     			  	 
as potential employers. However, sharing with other current or future  		  	   		  		 			  		 			     			  	 
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		  		 			  		 			     			  	 
GT honor code violation.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
-----do not edit anything above this line---  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
Student Name: Ning Yang 		  	   		  		 			  		 			     			  	 
GT User ID: nyang76 		  	   		  		 			  		 			     			  	 
GT ID: 903860974 		  	   		  		 			  		 			     			  	 
"""  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
import datetime as dt  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
import numpy as np  		  	   		  		 			  		 			     			  	 
import matplotlib  
matplotlib.use("TKAgg")			  	   		  		 			  		 			     			  	 
import matplotlib.pyplot as plt
	  	   		  		 			  		 			     			  	 
import pandas as pd  	
import scipy.optimize as spo	  	   		  		 			  		 			     			  	 
from util import get_data, plot_data  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
def sharpe_func(allocs,prices):
    normed = prices/prices.iloc[0,:]
    alloced = normed*allocs
    start_val=100000
    portfolio = alloced * start_val
    portfolio = portfolio.sum(axis=1)
    #lag
    daily_return=(portfolio/portfolio.shift(1))-1
    mean = daily_return.mean()
    std = daily_return.std()
    risk = 0
    sr = (-1)*np.sqrt(252) * ((mean- risk)/std)
    return sr

def cal_metrics(prices,allocs):
    normed = prices/prices.iloc[0,:]
    alloced = normed*allocs
    start_val=1
    port = alloced * start_val
    portfolio = port.sum(axis=1)
    #lag
    daily_return=(portfolio/portfolio.shift(1))-1
    adr = daily_return.mean()
    sddr = daily_return.std()
    risk = 0
    sr = (-1)*np.sqrt(252) * ((adr - risk)/ sddr)
    cr = portfolio[-1] / portfolio[0]
    return cr, adr, sddr, sr, portfolio


def optimize_portfolio(  		  	   		  		 			  		 			     			  	 
    sd=dt.datetime(2008, 6, 1),  		  	   		  		 			  		 			     			  	 
    ed=dt.datetime(2009, 6, 1),  		  	   		  		 			  		 			     			  	 
    syms=['IBM', 'X', 'GLD', 'JPM'],  		  	   		  		 			  		 			     			  	 
    gen_plot=False,  
):  
    dates = pd.date_range(sd, ed)  
    prices_all = get_data(syms, dates)  
    prices = prices_all[syms]   
    prices_SPY = prices_all["SPY"]  
    prices_SPY = prices_SPY / prices_SPY.iloc[0]
    # initial guess
    l=len(syms)
    #allocs = np.random.dirichlet(np.ones(l),size=1)
    allocs = [1/l]*l
    bounds = [(0,1)]*l
    #make sure the sum=1
    #eq for equality
    constraints = ({ 'type': 'eq', 'fun': lambda inputs: 1 - np.sum(inputs) }) 
    min_result = spo.minimize(sharpe_func, allocs, args = prices,bounds=bounds, method='SLSQP', constraints=constraints, options={'disp': True})
    final_allocs = min_result.x

    cr, adr, sddr, sr, port_val = cal_metrics(prices,final_allocs)
  		  	   		  		 			  		 			     			  	 
    if gen_plot:  		  	   		  		 			  		 			     			  	 
        		  	   		  		 			  		 			     			  	 
        df_temp = pd.concat([port_val, prices_SPY], keys=["Portfolio", "SPY"], axis=1) 
        ax = df_temp.plot(title="Daily portfolio value and SPY", fontsize=12)  		  	   		  		 			  		 			     			  	 
        ax.set_xlabel("Date")  		  	   		  		 			  		 			     			  	 
        ax.set_ylabel("Prices")
        plt.grid(linestyle='dotted')
        plt.legend(loc="upper left") 
        plt.savefig('Figure1.png')

    return final_allocs, cr, adr, sddr, sr 
    		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
def test_code():  		  	   		  		 			  		 			     			  	 
 	   		  		 			  		 			     			  	 
    start_date = dt.datetime(2008, 6, 1)  		  	   		  		 			  		 			     			  	 
    end_date = dt.datetime(2009, 6, 1)  		  	   		  		 			  		 			     			  	 
    symbols = ['IBM', 'X', 'GLD', 'JPM']  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    # Assess the portfolio  		  	   		  		 			  		 			     			  	 
    allocations, cr, adr, sddr, sr = optimize_portfolio(  		  	   		  		 			  		 			     			  	 
        sd=start_date, ed=end_date, syms=symbols, gen_plot=True  		  	   		  		 			  		 			     			  	 
    )  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    # Print statistics  		  	   		  		 			  		 			     			  	 
    print(f"Start Date: {start_date}")  		  	   		  		 			  		 			     			  	 
    print(f"End Date: {end_date}")  		  	   		  		 			  		 			     			  	 
    print(f"Symbols: {symbols}")  		  	   		  		 			  		 			     			  	 
    print(f"Allocations:{allocations}")  		  	   		  		 			  		 			     			  	 
    print(f"Sharpe Ratio: {sr}")  		  	   		  		 			  		 			     			  	 
    print(f"Volatility (stdev of daily returns): {sddr}")  		  	   		  		 			  		 			     			  	 
    print(f"Average Daily Return: {adr}")  		  	   		  		 			  		 			     			  	 
    print(f"Cumulative Return: {cr}")  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
if __name__ == "__main__":  		  	   		  		 			  		 			     			  	 
    # This code WILL NOT be called by the auto grader  		  	   		  		 			  		 			     			  	 
    # Do not assume that it will be called  		  	   		  		 			  		 			     			  	 
    test_code()  		  	   		  		 			  		 			     			  	 
