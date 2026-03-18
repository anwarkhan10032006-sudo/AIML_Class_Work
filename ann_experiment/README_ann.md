BEGIN

1. Import required libraries
   - TensorFlow / Keras
   - NumPy
   - Scikit-learn modules

2. Load dataset
   - Load Iris dataset
   - Extract features (X) and labels (y)

3. Split dataset
   - Divide data into training set (80%)
   - Divide data into testing set (20%)

4. Preprocess data
   - Apply standardization (scaling)
   - Fit scaler on training data
   - Transform both training and testing data

5. Build ANN model
   - Initialize Sequential model
   - Add input layer
   - Add hidden layer(s) with ReLU activation
   - Add output layer with Softmax activation

6. Compile model
   - Set optimizer = Adam
   - Set loss function = categorical/sparse categorical crossentropy
   - Set evaluation metric = accuracy

7. Train model
   - Train using training data
   - Set epochs = 50
   - Set batch size = 16
   - Validate using a portion of training data

8. Evaluate model
   - Test model using test dataset
   - Calculate test accuracy and loss

9. Display results
   - Print training accuracy
   - Print testing accuracy
   - Print loss values

10. (Optional)
    - Plot loss vs epochs graph

END