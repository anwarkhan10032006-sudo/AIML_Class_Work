# Implementation of Decision tree
The experiment focuses on building a supervised machine learning model using a Decision Tree algorithm to classify flower species based on given input features. The model is trained on labeled data, tested on unseen data, and evaluated using performance metrics to measure its classification accuracy and effectiveness.
--- 

# Pseudocode 
```
BEGIN

1. Import required libraries for:
      - Data handling
      - Machine learning
      - Model evaluation

2. Load Iris dataset

3. Extract features and target:
      X ← dataset features
      y ← dataset target labels

4. Split dataset into training and testing sets:
      Training data = 80%
      Testing data = 20%

5. Create Decision Tree classifier model

6. Train the model using training data:
      Fit model using (X_train, y_train)

7. Predict class labels for test data:
      y_pred ← model prediction on X_test

8. Evaluate model performance:

      a. Compute Accuracy:
            Accuracy ← number of correct predictions / total predictions

      b. Generate Classification Report:
            Calculate precision, recall, and F1-score

      c. Generate Confusion Matrix:
            Compare actual vs predicted labels

9. Display:
      - Accuracy
      - Classification Report
      - Confusion Matrix

END


```