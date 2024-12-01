#include<iostream>
#include<vector>
#include<string>
#include"Domain.h"
#include "Repository.h"
#include "Service.h"
#include"Ui.h"


using namespace std;

int main()
{
	Repository repo;
	Service service;
	Ui ui(service);
	service.initialiseRepositry();
	ui.run();
	return 0;
}