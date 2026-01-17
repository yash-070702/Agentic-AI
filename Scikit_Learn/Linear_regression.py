import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

dt=pd.read_csv('car.csv')

dt.dropna(inplace=True)


x=dt.iloc[:,1:8]
y=dt.iloc[:,0]

x=pd.get_dummies(x)
reg=LinearRegression()
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
scale=StandardScaler()
x_train=scale.fit_transform(x_train)
x_test=scale.transform(x_test)


reg.fit(x_train,y_train)

m=reg.coef_
c=reg.intercept_

y_pred_train=reg.predict(x_train)
y_pred_test=reg.predict(x_test)

r1_s=r2_score(y_train,y_pred_train)
r2_s=r2_score(y_test,y_pred_test)

print(r1_s,r2_s)

