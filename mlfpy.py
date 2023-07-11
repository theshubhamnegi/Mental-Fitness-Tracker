from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np


import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')


df1 = pd.read_csv('mental-and-substance-use-as-share-of-disease.csv')
df2 = pd.read_csv("prevalence-by-mental-and-substance-use-disorder.csv")

df1.head()

df2.head()


data = pd.merge(df1, df2)
data.head()


data.isnull().sum()


data.drop('Code', axis=1, inplace=True)


data.size, data.shape


data.set_axis(['Country', 'Year', 'Schizophrenia', 'Bipolar_disorder', 'Eating_disorder', 'Anxiety',
              'drug_usage', 'depression', 'alcohol', 'mental_fitness'], axis='columns', inplace=True)


data.head()


plt.figure(figsize=(12, 6))
sns.heatmap(data.corr(), annot=True, cmap='Greens')
plt.plot()


sns.jointplot(data, x="Schizophrenia",
              y="mental_fitness", kind="reg", color="m")
plt.show()


sns.jointplot(data, x='Bipolar_disorder',
              y='mental_fitness', kind='reg', color='blue')
plt.show()


sns.pairplot(data, corner=True)
plt.show()


mean = data['mental_fitness'].mean()
mean


fig = px.pie(data, values='mental_fitness', names='Year')
fig.show()


fig = px.bar(data.head(10), x='Year', y='mental_fitness',
             color='Year', template='ggplot2')
fig.show()


fig = px.line(data, x="Year", y="mental_fitness", color='Country', markers=True,
              color_discrete_sequence=['red', 'blue'], template='plotly_dark')
fig.show()


df = data.copy()
df.head()


df.info()


l = LabelEncoder()
for i in df.columns:
    if df[i].dtype == 'object':
        df[i] = l.fit_transform(df[i])

X = df.drop('mental_fitness', axis=1)
y = df['mental_fitness']

xtrain, xtest, ytrain, ytest = train_test_split(
    X, y, test_size=0.2, random_state=2)

X = df.drop('mental_fitness', axis=1)
y = df['mental_fitness']

xtrain, xtest, ytrain, ytest = train_test_split(
    X, y, test_size=0.2, random_state=2)


print("xtrain: ", xtrain.shape)
print("xtest: ", xtest.shape)
print("ytrain: ", ytrain.shape)
print("ytest: ", ytest.shape)


lr = LinearRegression()
lr.fit(xtrain, ytrain)


ytrain_pred = lr.predict(xtrain)
mse = mean_squared_error(ytrain, ytrain_pred)
rmse = (np.sqrt(mean_squared_error(ytrain, ytrain_pred)))
r2 = r2_score(ytrain, ytrain_pred)

print("The model performance for training set")
print("--------------------------------------")
print('MSE is {}'.format(mse))
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))
print("\n")


ytest_pred = lr.predict(xtest)
mse = mean_squared_error(ytest, ytest_pred)
rmse = (np.sqrt(mean_squared_error(ytest, ytest_pred)))
r2 = r2_score(ytest, ytest_pred)

print("The model performance for testing set")
print("--------------------------------------")
print('MSE is {}'.format(mse))
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))


rf = RandomForestRegressor()
rf.fit(xtrain, ytrain)


ytrain_pred = rf.predict(xtrain)
mse = mean_squared_error(ytrain, ytrain_pred)
rmse = (np.sqrt(mean_squared_error(ytrain, ytrain_pred)))
r2 = r2_score(ytrain, ytrain_pred)

print("The model performance for training set")
print("--------------------------------------")
print('MSE is {}'.format(mse))
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))
print("\n")


ytest_pred = rf.predict(xtest)
mse = mean_squared_error(ytest, ytest_pred)
rmse = (np.sqrt(mean_squared_error(ytest, ytest_pred)))
r2 = r2_score(ytest, ytest_pred)

print("The model performance for testing set")
print("--------------------------------------")
print('MSE is {}'.format(mse))
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))
