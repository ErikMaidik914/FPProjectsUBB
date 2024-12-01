#include <iostream>
#include<vector>
#include<string>
#include"Ui.h"

using namespace std;

void Ui::run()
{
	while (true)
	{
		cout << "MENU" << endl;
		cout << "0-exit" << endl;
		cout << "1-add protein" << endl;
		cout << "2-display all proteins" << endl;
		cout << "3-number of proteins with a certian organism" << endl;
		int choice = getChoice();
		switch (choice)
		{
		case 0:
			return;
		case 1:
			addProtein();
			break;
		case 2:
			showAll();
			break;
		default:
			cout << "WRONG INPUT" << endl;
			break;


		}
	}
}


int Ui::getChoice()
{
	int choice;
	cout << "YOUR CHOICE: "<<endl;
	cin >> choice;
	return choice;
}


void Ui::addProtein()
{
	string organsim, name, sequence;
	cout << "organsim: ";
	cin >> organsim;
	cout << "name: ";
	cin >> name;
	cout << "sequence: ";
	cin >> sequence;
	if (service.addProtein(organsim, sequence, name))
	{
		cout << "PROTEIN ADDED CONFIRMED!" << endl;
	}
	else
	{
		cout << "PROTEIN ALREADY EXISTS. WE DONT ADD IT!" << endl;
	}
		

}


void Ui::showAll()
{
	vector<Protein> allProtein = service.showAll();
	for (auto& Protein : allProtein)
	{
		cout << Protein.getOrganism() << " " << Protein.getName() << " " << Protein.getSequence() << endl;
	}
}


