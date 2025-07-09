#include <stdio.h>  //trying to make a single neurone so i can make neuro network
#include <stdlib.h>
#include <SDL2/SDL.h>
//structure of neuron node use typedef to make node a datatype
typedef struct node{

    double inputStream;
    double weight;
    double bias;
    double *output;
        //01-01-2025 right now i dont know what i am doing but later on in few weeks
}node;
int main(){
        //i will finish building this neuron network if not in c then it will be in python
    node inputlayer[5];

    node node1;
    node nide2;
    node node3;
    node nide4;
    node node5;

    inputlayer[1] = node1;
    inputlayer[2] = node2;
    inputlayer[3] = node3;
    inputlayer[4] = node4;
    inputlayer[5] = node5;

    printf("%f",node1.bias);

}

/*  //well this how you make working AI without tranning in python with external libraby
    //this AI is just a AI it has not been trainned so its basically useless
    //but its a working AI

import tensorflow as tf
import numpy as np

# Define an untrained AI model with 3 hidden layers, each with 100 neurons
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(1000, input_shape=(1,), activation='relu'),  # Hidden layer 1
    tf.keras.layers.Dense(1000, activation='relu'),                   # Hidden layer 2
    tf.keras.layers.Dense(1000, activation='relu'),                   # Hidden layer 3
    tf.keras.layers.Dense(1000, activation='relu'),                   # Hidden layer 4
    tf.keras.layers.Dense(1000, activation='relu'),                   # Hidden layer 5
    tf.keras.layers.Dense(1, activation='linear')                    # Output layer
])
user_input_ascii = []

for i in range(100):
  user_input_ascii.clear()
  # User prompt for input
  user_input = input("Enter a single character (A-Z or a-z): ")

  # Convert character to ASCII value
  for j in range(len(user_input)):
    user_input_ascii.append(ord(user_input[j]))
    print(ord(user_input[j]))
    # Normalize input (reshape for model)
    normalized_input = np.array([[user_input_ascii[j]]])

    # Make a prediction
    prediction = model.predict(normalized_input)
    normalized_input = None
    print(prediction)

    # Convert prediction to ASCII value
    predicted_ascii = int(round(prediction[0][0]))  # Round to nearest integer

    # Check if predicted ASCII is a valid character
    if 32 <= predicted_ascii <= 126:  # Printable ASCII range
      predicted_char = chr(predicted_ascii)
      print(f"Untrained AI Prediction for '{user_input}': {predicted_char}")
    else:
      # If not a valid ASCII character, display raw output
      print(f"Untrained AI Prediction for '{user_input}': {prediction[0][0]}")

*/
