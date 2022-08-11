#Author : Saurabh Malgave, 11th Aug 2022
import pandas
from pandas import DataFrame
import matplotlib.pyplot as plt
data = pandas.read_csv('/Users/saurabhmalgave/Downloads/cost_revenue_clean.csv')
DataDescribe = data.describe()
X = DataFrame(data,columns=['production_budget_usd'])
y = DataFrame(data,columns=['worldwide_gross_usd'])

plt.figure(figsize=(10,6))
plt.scatter(X,y)
plt.title('Film Cost vs Global Revenue')
plt.xlabel('Production Budget $')
plt.ylabel('Worldwide Gross$')
plt.ylim(0,3000000000)
plt.xlim(0,450000000)
plt.show()