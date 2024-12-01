#include <stdio.h>

// function to read a vector of numbers from the console that takes each elemnt and adds it to the vector
void createVector(int* vector, int size) 
{
    for (int i = 0; i < size; i++) 
    {
        if (scanf("%d", &vector[i]) > 0)
            printf("");
        else printf("Invalid input.\n");
    }
}

//if there are any divisors of the number besides 1 and itself, the function returns 0, else it returns 1
int isPrime(int number)
{
    if (number <= 1) 
    {
        return 0;
    }
    for (int i = 2; i * i <= number; i++) {
        if (number % i == 0) {
            return 0;
        }
    }
    return 1;
}

void firstNTwinNumbers(int n)
{
    int p = 2; // initialize p as the first prime number
    int q = 3; // initialize q as the second prime number
    int foundTwin = 0; // initialize foundTwin to false

    for (int i = 1; i <= n; i++)
    {
        while (!foundTwin)
        {
            // check if p and q are "twin" prime numbers
            if (q - p == 2)
            {
                foundTwin = 1;
                printf("(%d, %d) ", p, q);
            }
            // if p and q are not twin prime numbers, search for the next prime p and q
            p++;
            while (!isPrime(p))
            {
                p++;
            }
            q = p + 1;
            while (!isPrime(q))
            {
                q++;
            }
        }
        foundTwin = 0; // move on to the next pair
    }
}




// This function iterates through the vector. If we find two neighboring elements that satisfy the condition:
//We increase the current length of the sequence and if it is higher than the highest sequence found yet we uptade it
//If the two neighboring elements don't satisfy the codintion, we reset the current length
//Once we have the size of thsi array we can find its terms from the initial vector whith: last_el_index + vec_size +i+1
void findLongestDecreasingSubsequence(int* vector, int vectorSize, int* LongestDecreasingSubsequence, int* decreasingVectorSize)
{
    int maxLength = 1;
    int currentLength = 1;
    int endIndex = 0;
    for (int i = 1; i < vectorSize; i++)
    {
        if (vector[i] < vector[i - 1])
        {
            currentLength++;
            if (currentLength > maxLength)
            {
                maxLength = currentLength;
                endIndex = i;
            }
        }
        else
        {
            currentLength = 1;
        }
    }

    *decreasingVectorSize = maxLength;
    for (int i = 0; i < maxLength; i++)
    {
        LongestDecreasingSubsequence[i] = vector[endIndex - maxLength + i + 1];
    }
}

int main() {
    int choice,run = 1, vectorSize = 0, decreasingVectorSize = 0, n;
    int vector[100];
    int LongestDecreasingSubsequence[100] = { 0 };

    while (run) 
    {
        // display each instruction of the menu
        printf("Menu:\n");
        printf("1--> Read a vector of numbers\n");
        printf("2--> Find the longest decreasing contiguous subsequence\n");
        printf("3--> Determine the first n pairs of twin numbers\n");
        printf("4--> Exit\n");
        printf("Enter your choice: ");
        if (scanf("%d", &choice) > 0)
            printf("");
        else printf("Invalid input.\n");

        switch (choice) {
            case 1:
                printf("The vector sizze is: ");
                if (scanf("%d", &vectorSize) > 0)
                    printf("");
                else printf("Invalid input.\n");
                createVector(vector, vectorSize);
                printf("Current vector: ");
                for (int i = 0; i < vectorSize; i++) {
                    printf("%d ", vector[i]);
                }
                printf("\n");
                break;
            case 2:
                findLongestDecreasingSubsequence(vector, vectorSize, LongestDecreasingSubsequence, &decreasingVectorSize);
                printf("The longest decreasing contiguous subsequence is: ");
                for (int i = 0; i < decreasingVectorSize; i++) {
                    printf("%d ", LongestDecreasingSubsequence[i]);
                }
                printf("\n");
                break;
            case 3:
                printf("Enter the value of n: ");
                if (scanf("%d", &n) > 0)
                    printf("");
                else printf("Invalid input.\n");
                printf("The first %d pairs of twin prime numbers are:\n", n);
                firstNTwinNumbers(n);
                break;
            case 4:
                return 0;
            return 0;
        }
    }
}