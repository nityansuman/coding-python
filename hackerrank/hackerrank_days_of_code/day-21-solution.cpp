#include <iostream>
#include <vector>
#include <string>

using namespace std;

template<typename Element>

// Void function with template
void printArray(vector<Element> arr) {
    for (int i = 0; i < arr.size(); i++)
        cout << arr[i] << endl;
}

int main() {
	// Read input integer from stdin
	int n;
	cin >> n;

	// Create a integer vector of size n
	vector<int> int_vector(n);

	// Iteratively put data into vector
	for (int i = 0; i < n; i++) {
		// Read input integer from stdin
		int value;
		cin >> value;
		int_vector[i] = value;
	}

	// Again
	// Read integer input from stdin
	cin >> n;

	// Create a string vector of size n
	vector<string> string_vector(n);

	// Iteratively put data into vector
	for (int i = 0; i < n; i++) {
		// Read input string from stdin
		string value;
		cin >> value;
		string_vector[i] = value;
	}

	// Print integer vector
	printArray<int>(int_vector);

	// Print string vector
	printArray<string>(string_vector);

	return 0;
}
