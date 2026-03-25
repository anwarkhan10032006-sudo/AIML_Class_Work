# ann_tf.py

# 1. Import required libraries
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import Input

model = Sequential()

model.add(Input(shape=(4,)))   # better way
model.add(Dense(10, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(3, activation='softmax'))
# 2. Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Convert target to categorical (one-hot encoding)
y = to_categorical(y)

# Split dataset (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Data preprocessing (standardization)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. Define ANN model
model = Sequential()

# Input + Hidden layers
model.add(Dense(8, input_dim=4, activation='relu'))
model.add(Dense(8, activation='relu'))

# Output layer (3 classes → softmax)
model.add(Dense(3, activation='softmax'))

# 5. Compile model
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# 6. Train model
history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=16,
    verbose=0   # silent training
)

# 7. Evaluate model
train_loss, train_acc = model.evaluate(X_train, y_train, verbose=0)
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)

# 8. Display output in required format
print("\nModel Performance")

print("\n• Training Accuracy: {:.2f}%".format(train_acc * 100))
print("• Testing Accuracy: {:.2f}%".format(test_acc * 100))
print("• Training Loss: {:.4f}".format(train_loss))
print("• Testing Loss: {:.4f}".format(test_loss))

#use  py -3.10 ann_tf.py    to run