#include <iostream>
#include <vector>

using namespace std;

// Function to generate prime numbers up to a given limit using the Sieve of Eratosthenes
void generatePrimes(int limit) {
    vector<bool> isPrime(limit + 1, true);
    isPrime[0] = isPrime[1] = false; // 0 and 1 are not prime numbers

    for (int i = 2; i * i <= limit; ++i) {
        if (isPrime[i]) {
            // Mark multiples of i as not prime
            for (int j = i * i; j <= limit; j += i) {
                isPrime[j] = false;
            }
        }
    }

    // Print all prime numbers
    cout << "Prime numbers up to " << limit << " are:\n";
    for (int i = 2; i <= limit; ++i) {
        if (isPrime[i]) {
            cout << i << " ";
        }
    }
    cout << endl;
}

int main() {
    int limit;
    cout << "Enter the upper limit to find prime numbers: ";
    cin >> limit;

    generatePrimes(limit);

    return 0;
}
