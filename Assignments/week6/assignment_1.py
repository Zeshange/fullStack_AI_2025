# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
from sklearn import tree
import os
from sklearn.model_selection import cross_val_score

# Step 1: Load the dataset with error handling
data=pd.read_csv('Assignments\\week6\\drug200.csv')
# Step 2: Preprocess the data
le_sex = LabelEncoder()
le_bp = LabelEncoder()
le_chol = LabelEncoder()
le_drug = LabelEncoder()

data['Sex'] = le_sex.fit_transform(data['Sex'])
data['BP'] = le_bp.fit_transform(data['BP'])
data['Cholesterol'] = le_chol.fit_transform(data['Cholesterol'])
data['Drug'] = le_drug.fit_transform(data['Drug'])

# Define features (X) and target (y)
X = data[['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']]
y = data['Drug']

# Step 3: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the Decision Tree model with pruning
clf = DecisionTreeClassifier(max_depth=3, max_leaf_nodes=8, random_state=42)
clf.fit(X_train, y_train)

# Step 5: Make predictions and evaluate the model
y_pred = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Detailed classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=le_drug.classes_))

# Confusion matrix
print("\nConfusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Cross-validation
scores = cross_val_score(clf, X, y, cv=5)
print("\nCross-validation scores:", scores)
print("Average CV score:", scores.mean())

# Feature importance
importances = clf.feature_importances_
feature_names = ['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']
print("\nFeature Importances:")
for name, importance in zip(feature_names, importances):
    print(f"{name}: {importance:.4f}")

plt.figure(figsize=(20, 6))  # Larger figure to spread nodes
tree.plot_tree(clf, 
               feature_names=feature_names, 
               class_names=le_drug.classes_, 
               filled=True, 
               rounded=True,
               fontsize=12,
               node_ids=True,
               proportion=True,
               impurity=False)
plt.title("Decision Tree for Drug Classification")
plt.savefig("decision_tree.png", dpi=300, bbox_inches='tight')
plt.show()