#include <iostream>
#include <boost/lexical_cast.hpp>

int main()
{
  int value = boost::lexical_cast<int>("42");
  std::cout << value << '\n';
}