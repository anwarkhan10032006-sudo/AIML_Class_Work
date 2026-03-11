# Import Required Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# Load Iris Dataset
iris = load_iris()

# Create DataFrame
df = pd.DataFrame(iris.data, columns=[
    "Sepal Length",
    "Sepal Width",
    "Petal Length",
    "Petal Width"
])
df["Class"] = iris.target


# -----------------------------
# SAMPLE INPUT DISPLAY
# -----------------------------
print("\nSample Input")

print("\nDataset Used")
print("Iris Dataset")

print("\nFeatures:")
print("• Sepal Length")
print("• Sepal Width")
print("• Petal Length")
print("• Petal Width")

print("\nTarget Classes:")
print("• Setosa")
print("• Versicolor")
print("• Virginica\n")

print(df.head(3))

print("\nWhere:")
print("• 0 = Setosa")
print("• 1 = Versicolor")
print("• 2 = Virginica")


# -----------------------------
# MODEL TRAINING
# -----------------------------
X = iris.data
y = iris.target

# Split Dataset (70% Training, 30% Testing)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

# Create Decision Tree Model
model = DecisionTreeClassifier(max_depth=3, random_state=1)

# Train Model
model.fit(X_train, y_train)

# Predict Test Data
y_pred = model.predict(X_test)


# -----------------------------
# MODEL EVALUATION
# -----------------------------
accuracy = accuracy_score(y_test, y_pred)

print("\n\nSample Output:\n")

print("Model Evaluation")
print("Accuracy: {:.4f}".format(accuracy))

print("\nClassification Report\n")

print(classification_report(
    y_test,
    y_pred,
    target_names=["Setosa", "Versicolor", "Virginica"]
))

print("\nOverall Accuracy = {:.2f}%".format(accuracy * 100))

print("\nConfusion Matrix\n")

cm = confusion_matrix(y_test, y_pred)
print(cm)


# -----------------------------
# CONFUSION MATRIX VISUALIZATION
# -----------------------------
plt.imshow(cm, cmap="Blues")
plt.title("Confusion Matrix")
plt.colorbar()

plt.xticks([0,1,2], iris.target_names)
plt.yticks([0,1,2], iris.target_names)

plt.xlabel("Predicted")
plt.ylabel("Actual")

for i in range(len(cm)):
    for j in range(len(cm)):
        plt.text(j, i, cm[i][j], ha="center", va="center")

plt.show()
