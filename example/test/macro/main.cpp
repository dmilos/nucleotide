#include <cstdlib>
#include <iostream>
#include <iomanip>

using namespace std;

int main( int argc, char *argv[] )
 {
 #ifdef HELLO_WORLD
  cout << "Hello World" << endl;
#else
  cout << "Hello!" << endl;
#endif
  return EXIT_SUCCESS;
 }
