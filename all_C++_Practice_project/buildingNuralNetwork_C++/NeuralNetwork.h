#ifndef NEURAL_NETWORK_H
#define NEURAL_NETWORK_H

#include <iostream>
#include <ctime>
#include <cmath>
#include <random>

class NeuralNetwork {
public:
	
	NeuralNetwork() {
        srand(time(0));
	}

    double* CreateHiddenLayer(double inputData[],int inputDataSize,int numOfNeuron,int neuronInputNode = -1) {
        if (neuronInputNode == -1) {    //please specify how many input a neuron should have it should be same as the numOfNeuron in the last hiddenlayer 
            neuronInputNode = numOfNeuron; //this should be last hiddenLayer numOfNeuron not the current one
        }

        double* neuronsOutputs = new double[numOfNeuron];

        for (int i = 0; i < numOfNeuron; i++) {
            neuronsOutputs[i] = Neuron(neuronInputNode, inputData, inputDataSize);
        }

        return neuronsOutputs;
    }
private:
    double relu(double x) { //Activation Function use Sigmoid Activation Function for normalized value 
        return x > 0 ? x : 0;
    }
    double Neuron(int numOfInput = 1, double inputData[] = NULL, int sizeOfInputData = NULL) {
        /*srand(time(0));*/ //this will not work here because neuron will be called multiple times
        double* weight = new double[numOfInput];
        double bias = (double)rand() / RAND_MAX;
        double output = 0.0;

        //assign all the weight
        for (int i = 0; i < numOfInput; i++) {
            weight[i] = (double)rand() / RAND_MAX;
        }

        // Neuron computation
        for (int i = 0; i < numOfInput; i++) {
            for (int j = 0; j < sizeOfInputData; j++) {
                output += (weight[i] * inputData[j]);
                std::printf("Input[%d]: %lf, Weight[%d]: %lf, Bias: %lf, Output: %lf sizeOfInputData: %d \n", j, inputData[j], i, weight[i], bias, output, sizeOfInputData);
            }
        }
        output += bias;
        //Activation function in use is relu (x > 0 ? x : 0); //relu is from 0 to infinity no normalized value 
        output = relu(output); //for normalized value use other Activation functions like sigmoid and others

        std::cout << output << std::endl << std::endl;
        delete[] weight;
        return output;
    }

};

#endif // !NEURON_H
