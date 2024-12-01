#pragma once
#include<vector>
#include<string>
#include "Repository.h"


using namespace std;


class Service
{
private:
	Repository repo;
public:
	void initialiseRepositry();
	bool addProtein(string organism, string name, string sequence);
	vector<Protein> showAll();
	
};