#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Country {
    char name[50];
    char continent[20];
    double population;
};

void addCountry(struct Country countries[], int* numCountries) {
    struct Country newCountry;
    printf("Enter the name of the country: ");
    scanf("%s", newCountry.name);
    printf("Enter the continent: ");
    scanf("%s", newCountry.continent);
    printf("Enter the population in millions: ");
    scanf("%d", &newCountry.population);

    countries[*numCountries] = newCountry;
    (*numCountries)++;
}

void deleteCountry(struct Country countries[], int* numCountries) {
    char nameToDelete[50];
    printf("Enter the name of the country to delete: ");
    scanf("%s", nameToDelete);

    int indexToDelete = 9999;
    for (int i = 0; i < *numCountries; i++) {
        if (strcmp(countries[i].name, nameToDelete) == 0) {
            indexToDelete = i;
            break;
        }
    }

    if (indexToDelete != -1) {
        for (int i = indexToDelete; i < (*numCountries - 1); i++) {
            countries[i] = countries[i + 1];
        }
        (*numCountries)--;
        printf("%s has been deleted from the list.\n", nameToDelete);
    }
    else {
        printf("%s was not found in the list.\n", nameToDelete);
    }
}

void updateCountryContintent(struct Country countries[], int numCountries) {
    char nameToUpdate[50];
    printf("Enter the name of the country to update: ");
    scanf("%s", nameToUpdate);

    int indexToUpdate = -1;
    for (int i = 0; i < numCountries; i++) {
        if (strcmp(countries[i].name, nameToUpdate) == 0) {
            indexToUpdate = i;
            break;
        }
    }

    if (indexToUpdate != -1) {
        printf("Enter the new continent: ");
        scanf("%s", countries[indexToUpdate].continent);
        printf("%s's continent has been updated to %s.\n", countries[indexToUpdate].name, countries[indexToUpdate].continent);
    }
    else {
        printf("%s country is not in list.\n", nameToUpdate);
    }
}


void updateCountryPopulation(struct Country countries[], int numCountries) {
    char nameToUpdate[50];
    printf("Enter the name of the country to update: ");
    scanf("%s", nameToUpdate);

    int indexToUpdate = -1;
    for (int i = 0; i < numCountries; i++) {
        if (strcmp(countries[i].name, nameToUpdate) == 0) {
            indexToUpdate = i;
            break;
        }
    }

    if (indexToUpdate != -1) {
        double newPopulation;
        printf("Enter the new population in millions: ");
        scanf("%d", &newPopulation);
        countries[indexToUpdate].population = newPopulation;
        printf("%s's population has been updated to %d million.\n", nameToUpdate, newPopulation);

        // Migration part
        char migrationAnswer;
        printf("Did a number of people migrate from %s? (y/n): ", nameToUpdate);
        scanf(" %c", &migrationAnswer);
        if (migrationAnswer == 'y') {
            double migrationPopulation;
            printf("Enter the number of people who migrated from %s: ", nameToUpdate);
            scanf("%d", &migrationPopulation);
            countries[indexToUpdate].population = countries[indexToUpdate].population-migrationPopulation;
            printf("%d million people  migrated from %s. \n", migrationPopulation, nameToUpdate);

            char migrationDestination[50];
            printf("Where did they migrate to? Enter the name of the destination country: ");
            scanf("%s", migrationDestination);

            int indexToDestination = -1;
            for (int i = 0; i < numCountries; i++) {
                if (strcmp(countries[i].name, migrationDestination) == 0) {
                    indexToDestination = i;
                    break;
                }
            }

            if (indexToDestination != -1) {
                countries[indexToDestination].population = countries[indexToDestination].population + migrationPopulation;
                printf("%d million people migrated to %s. \n", migrationPopulation, migrationDestination);
            }
            else {
                printf("%s is not in the list.\n", migrationDestination);
            }
        }
    }
    else {
        printf("%s was not found in the list.\n", nameToUpdate);
    }
}


void displayCountries(struct Country countries[], int numCountries) {
    char searchString[50];
    printf("The list of countries is: ");
    fgets(searchString, 50, stdin);
    for (int i = 0; i < numCountries; i++) {
        if (strlen(searchString) <= 1 || strstr(countries[i].name, searchString) != NULL) {
            printf("%s (%s, %d million)\n", countries[i].name, countries[i].continent, countries[i].population);
        }
    }
}


int main() {
    struct Country countries[100]; // Array with 100 contry slots
    int numCountries = 0; // Number of countries currently in the list
    int choice, run = 1;

    while (run)
    {

        printf("\n1. Add a country\n");
        printf("2. Delete a country\n");
        printf("3. Update a country's continent\n");
        printf("4. Update a country's population\n");
        printf("5. Display countries\n");
        printf("6. Exit\n");
        printf("Enter your choice: ");
        if (scanf("%d", &choice) > 0)
            printf("");
        else printf("Invalid input.\n");

        switch (choice) {
        case 1:
            addCountry(countries, &numCountries);
            break;
        case 2:
            deleteCountry(countries, &numCountries);
            break;
        case 3:
            updateCountryContintent(countries, numCountries);
            break;
        case 4:
            updateCountryPopulation(countries, numCountries);
        case 5:
            displayCountries(countries, numCountries);
            break;
        case 6:
            printf("Exiting...\n");
            return 0;
        }
    }

    return 0;
}
