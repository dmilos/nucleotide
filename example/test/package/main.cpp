#include <cstdlib>
#include <iostream>
#include <iomanip>
//#include <boost/thread.hpp>

using namespace std;

 
 class BankAccount
 {
  public:
    int Withdraw(int){ return -1;}
    void Deposit(int){ }
 };

BankAccount JoesAccount;

void bankAgent()
{
    for (int i =10; i>0; --i) {
        //...
        JoesAccount.Deposit(500);
        //...
    }
}

void Joe() {
    for (int i =10; i>0; --i) {
        //...
        int myPocket = JoesAccount.Withdraw(100);
        std::cout << myPocket << std::endl;
        //...
    }
}

int main() {
    /*
    boost::thread thread1(bankAgent); // start concurrent execution of bankAgent
    boost::thread thread2(Joe); // start concurrent execution of Joe
    thread1.join();
    thread2.join();*/
    return 0;
}