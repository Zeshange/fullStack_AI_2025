import pandas as pd
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split 
from sklearn import metrics

# Load the data
df = pd.read_csv("Assignments/week_6/drug200.csv")

# Prepare features and target
X = df[['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']].copy()
X['Sex'] = X['Sex'].map({'F': 0, 'M': 1})
X['BP'] = X['BP'].map({'LOW': 0, 'NORMAL': 0, 'HIGH': 1})
X['Cholesterol'] = X['Cholesterol'].map({'NORMAL': 0, 'HIGH': 1})

y = df["Drug"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Train the model
clf = DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)

# Predict and evaluate
y_pred = clf.predict(X_test)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
