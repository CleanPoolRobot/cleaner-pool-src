#include "communication.hpp"

using namespace IO;

int main (){
  
  int id = start_arduino();
  write_arduino(id);
  read_arduino(id);
  stop_arduino(id);

  return 0;
}
