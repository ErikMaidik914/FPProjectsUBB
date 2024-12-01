#include<vector>
#include<string>
#include "Service.h"


using namespace std;


bool Service::addProtein(string organism, string name, string sequence)
//the service version of the add protein function creates a protein object with the recieved input from the user
//and returns true or false depending on what the add function from the repo returneg
//input paramerers: 3 strings
{
	Protein protein(organism, name, sequence);
	return repo.addProtein(protein);
}




void Service::initialiseRepositry()
{
	this->addProtein("Human", "Myosin-2", "QWER");
	this->addProtein("Human", "Keratin", "DHJSDKJ");
	this->addProtein("Mouse", "Keratin", "DDD");
	this->addProtein("E_Coil", "tufA", "QWER");
	this->addProtein("E_Coil", "cspE", "GGGG");
}


vector<Protein> Service::showAll()
{
	return repo.showAll();
}