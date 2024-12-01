#pragma once
#include<vector>
#include<string>
#include "Service.h"


using namespace std;

class Ui
{
private:
	Service& service;
	void addProtein();
	void showAll();
	int getChoice();

public:
	Ui(Service& service):service(service){}
	void run();
};