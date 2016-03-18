#include <cstdlib>
#include <iostream>
#include <iomanip>

using namespace std;

int & f()
 {
   int i=0;
  return i;
 }

int main( int argc, char *argv[] )
 {
  cout << "Hello World" << endl;
  cout << f() << endl;

  return EXIT_SUCCESS;
 }
