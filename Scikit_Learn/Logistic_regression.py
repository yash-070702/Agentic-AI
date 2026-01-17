import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

dt=pd.read_csv('student.csv')

dt.dropna(inplace=True)

x=dt.iloc[:,0:2]
y=dt.iloc[:,-1]


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

scale=StandardScaler()
x_train=scale.fit_transform(x_train)
x_test=scale.transform(x_test)

log_reg=LogisticRegression()
log_reg.fit(x_train,y_train)

y_pred_train=log_reg.predict(x_train)
y_pred_test=log_reg.predict(x_test) 

train_acc = accuracy_score(y_train, y_pred_train)
test_acc = accuracy_score(y_test, y_pred_test)

print("Train Accuracy:", train_acc)
print("Test Accuracy:", test_acc)


cm = confusion_matrix(y_test, y_pred_test)
print(cm)

