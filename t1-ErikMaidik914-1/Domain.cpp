#include<vector>
#include<string>
#include "Domain.h"


using namespace std;

Protein::Protein(string organism, string name, string sequence)
{
	this->organism = organism;
	this->name = name;
	this->sequence = sequence;
}

string Protein::getOrganism() const
{
	return this->organism;
}


string Protein::getName() const
{
	return this->name;
}


string Protein::getSequence() const
{
	return this->sequence;
}