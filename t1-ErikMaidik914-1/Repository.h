#pragma once
#include<vector>
#include<string>
#include "Domain.h"

using namespace std;

class Repository
{
private:
	vector<Protein> allProtein{};
public:
	bool addProtein(Protein protein);
	vector<Protein> showAll();
};