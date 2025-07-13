#include <iostream>
#include <ctime>
#include <cmath>
#include <string>
#include <vector>

#include "NeuralNetwork.h"
std::vector<std::string> stringToTokensVec(std::string stringText);
std::vector<double> stringToVector(std::string tokens);
int main() {
	double inputData[] = { 21.0, 0.25, 54.32, 48.69, 0.675, 0.29854, 3.14159 };
	int sizeOfInputData = sizeof(inputData) / sizeof(inputData[0]);

	const int neuronInLayer1 = 5;
	const int neuronInLayer2 = 3;

	std::cout << std::endl;
	for (int i = 0; i < sizeOfInputData; i++) {
		std::cout << "  |  " << inputData[i];
	}std::cout << std::endl << std::endl;

	NeuralNetwork network;
	double* hiddenLayer1stOutput = network.CreateHiddenLayer(inputData, sizeOfInputData, neuronInLayer1, 1);
	std::cout << std::endl;
	for (int i = 0; i < neuronInLayer1; i++) {
		std::cout << "  |  " << hiddenLayer1stOutput[i];
	}std::cout << std::endl << std::endl;

	double* hiddenLayer2ndOutput = network.CreateHiddenLayer(hiddenLayer1stOutput, neuronInLayer1, neuronInLayer2, neuronInLayer1);
	std::cout << std::endl;
	for (int i = 0; i < neuronInLayer2; i++) {
		std::cout << "  |  " << hiddenLayer2ndOutput[i];
	}std::cout << std::endl << std::endl;


	std::vector<std::string> vecTokens = stringToTokensVec("vector call here for string to vector of double for the input of hidden layer");



	delete[] hiddenLayer1stOutput;
	delete[] hiddenLayer2ndOutput;
	return 0;
}
std::vector<std::string> stringToTokensVec(std::string stringText) {
	int startString = 0, endString = 0;
	bool hasFirstIndex = false, hasLastIndex = false;
	std::vector<std::string> tokens;
	std::string token;

	for (int i = 0; i <= stringText.length(); i++) {
		if (stringText[i] != ' ' && stringText[i] != '\0') {
			if (!hasFirstIndex) {
				startString = i;
				hasFirstIndex = true;
				hasLastIndex = false;
			}
		}
		else {
			if (!hasLastIndex) {
				endString = i - 1;
				hasFirstIndex = false;
				hasLastIndex = true;

				for (int i = startString; i <= endString; i++) {
					token += stringText[i];
				}
				tokens.push_back(token);
				token.clear();
			}

		}
	}

	return tokens;
}
std::vector<double> stringToVector(std::string token) {
	int tokenLength = token.length();
	std::vector<double> tokenVec;
	
	for (int i = 0; i < tokenLength; i++) {		//last date : 13-07-2025 //havent touched it since
		tokenVec.push_back(token[i])		//maybe i will finish this project in the future
	}
}
