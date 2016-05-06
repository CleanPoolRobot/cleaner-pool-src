#include "communication.hpp"

namespace IO
{
  const int SIZE_BUFFER = 50;

  int start_arduino()
  {
    int id_device = open( DEVICE, O_RONLY );
    int id = 0;

    if( id_device != NOT_OPEN )
    {
      // Nothing to do.
    } else
    {
      std::cout << "Unable to open Arduino communication port..." << std::end;
    }

    return id_device;
  }
}
