#include <iostream>
#include <iomanip>

using namespace std;

int main( int argc, char *argv[] )
 {
  cout << "aaaaa" << endl;

  return EXIT_SUCCESS;
 }

#ifdef __MSVC__
__declspec( dllexport ) 
#endif
int 
f()
 {
  return 0;   
 }