from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np 
import statsmodels as sm
import pickle

df_raw = pd.read_csv(r"C:\Users\GZNC3537\Downloads\new.csv")
print(f"Shape:{df_raw.shape}" )
df_raw.head(10)
df_raw.describe()
df_raw.info()

df = df_raw[["Calls Offered","HeadCount"]]
df.head(10)

df = df_raw[["Dates", "Calls Offered"]]
# df['Dates']= pd.to_datetime(df['Dates'])

df = df.set_index(["Dates"])
df = df.rename(columns = {"Calls Offered": "TotalCalls"})
df.head(10)
df['TotalCalls'].plot(figsize=(12,5))

train_data = df.iloc[:80,:]
test_data = df[-36:]
df_test = df.iloc[:90,:] 

train = plt.plot(train_data,color='blue', label = 'Train data')
test = plt.plot(test_data, color ='black', label = 'Test data')
plt.legend(loc='best') 
plt.title('Data division')
plt.xticks(rotation = 90)
plt.show(block=False)
from statsmodels.tsa.stattools import adfuller
def test_stationary(timeseries):
    rolmean = timeseries.rolling(window=12).mean()
    rolstd = timeseries.rolling(window=12).std()
    
    orig = plt.plot(timeseries,color='blue', label = 'Original')
    mean = plt.plot(rolmean, color ='red', label ='Rolling Mean')
    std = plt.plot(rolstd, color ='black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean and Standard Deviation')
    plt.show(block=False) 
 
    print('Results of Dickey Fuller Test:')
    dftest = adfuller(timeseries, autolag= 'AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print (dfoutput)

test_stationary(df_test)

from pmdarima import auto_arima

stepwise_fit = auto_arima(train_data, trace=True,
suppress_warnings=True)
from statsmodels.tsa.arima.model import ARIMA
import warnings
warnings.filterwarnings("ignore")
model=ARIMA(train_data,order=(1,0,0))
results=model.fit()
print(results.summary())


pred_arima = results.forecast(75)
predicted =plt.plot(pred_arima,label='forecast', color='orange')
Actual = plt.plot(df,label='Calls Offered',color ="blue" )
plt.legend(loc='best') 
plt.show(block=False)

df.tail(22)


pickle.dump(model,open("callModelTest.pkl","wb"))
