#pragma once
#include<vector>
#include<string>

using namespace std;

class Protein
{
private:
	string organism;
	string name;
	string sequence;
public:
	Protein(string organism, string name, string sequence);
	string getOrganism() const;
	string getName() const;
	string getSequence() const;
};