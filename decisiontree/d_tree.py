# Import Required Libraries
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load Iris Dataset
iris = load_iris()

# Create DataFrame (for displaying sample input)
df = pd.DataFrame(iris.data, columns=[
    "Sepal Length",
    "Sepal Width",
    "Petal Length",
    "Petal Width"
])
df["Class"] = iris.target

print("\nSample Input\n")
print(df.head(3))

# Separate Features and Target
X = iris.data
y = iris.target

# Split Dataset (70% Training, 30% Testing)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

# Create Decision Tree with Limited Depth (Prevents 100% accuracy)
model = DecisionTreeClassifier(max_depth=3, random_state=1)

# Train Model
model.fit(X_train, y_train)

# Predict Test Data
y_pred = model.predict(X_test)

# Evaluate Model
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Evaluation")
print("Accuracy: {:.4f}".format(accuracy))
print("\nOverall Accuracy = {:.2f}%".format(accuracy * 100))

print("\nClassification Report\n")
print(classification_report(
    y_test,
    y_pred,
    target_names=["Setosa", "Versicolor", "Virginica"]
))

print("\nConfusion Matrix\n")
print(confusion_matrix(y_test, y_pred))