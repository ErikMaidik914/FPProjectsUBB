#include<vector>
#include<string>
#include "Repository.h"
#include<algorithm>


using namespace std;

vector<Protein> Repository::showAll()
{
	//sort(allProtein.begin(), allProtein.end(), compareOrganism);
	return allProtein;
}

bool Repository::addProtein(Protein protein)
//the addProtein function in teh repo iterates through our list of all proteins and if it finds one that already exists it returns false else it uses
//push_back to add the new protein to the vector
{
	for (int i = 0; i < allProtein.size(); i++)
	{
		if (allProtein[i].getOrganism() == protein.getOrganism() && allProtein[i].getName() == protein.getName())
			return false;
	}
	allProtein.push_back(protein);
	return true;
}

//bool compareOrganism(Protein& protein1, Protein& protein2)
//{
	//if (protein1.getOrganism() == protein2.getOrganism())
	//{
	//	return true;
	//}
	//return false;
//}
