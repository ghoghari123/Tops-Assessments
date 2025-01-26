#include <iostream>
#include <string>

using namespace std;

int main()
{
    string s1, s2;
    int n1, n2;
    const double costPerHour = 20.00;
    const double costPerPerson = 20.70;
    const double depositPercentage = 0.25;

    // Get Input From The User
    cout << "****Event Management System****" << endl<< endl;
    cout << "Enter The Name Of The Event: " << endl;
    getline(cin, s1);
    cout << "Enter The Clint First & Last Name: " << endl;
    getline(cin, s2);
    cout << "Enter The Number Of Guests: " << endl;
    cin >> n1;
    cout << "Enter The Number Of Minutes In The Event: " << endl;
    cin >> n2;

    // Calculate The Event Costs
    int numServers = n1 / 20;
    double serverCost = numServers * costPerHour * (n2 / 60.0);
    double foodCost = n1 * costPerPerson;
    double totalCost = serverCost + foodCost;
    double deposit = totalCost * depositPercentage;

    // Display The Event Estimate
    cout << "\n==========Event Estimate For: " << s2 << "==========" << endl;
    cout << "Number Of Servers: " << numServers << endl;
    cout << "The Cost For Servers: " << serverCost << endl;
    cout << "The Cost For Food is: " << foodCost << endl;
    cout << "Average Cost Per Person: " << costPerPerson << endl<< endl;
    cout << "Total Cost Is: " << totalCost << endl;
    cout << "Please Deposit A 25% Deposit To Reserve The Event" << endl;
    cout << "The Deposit Needed Is: " << deposit << endl;

    return 0;
}