import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

dt = pd.read_csv("play_outside.csv")
dt.dropna(inplace=True)

x = dt.iloc[:, 0:5]   
y = dt.iloc[:, -1]    

x = pd.get_dummies(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
dt_model = DecisionTreeClassifier(random_state=0)

dt_model.fit(x_train, y_train)
y_pred_train = dt_model.predict(x_train)
y_pred_test = dt_model.predict(x_test)

train_acc = accuracy_score(y_train, y_pred_train)
test_acc = accuracy_score(y_test, y_pred_test)

print("Train Accuracy:", train_acc)
print("Test Accuracy:", test_acc)
cm = confusion_matrix(y_test, y_pred_test)
print(cm)



