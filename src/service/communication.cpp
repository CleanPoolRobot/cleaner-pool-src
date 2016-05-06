#include "communication.hpp"
#include <termios.h>

namespace IO
{
  const int SIZE_BUFFER = 50;

  int start_arduino()
  {
    int id_device = open( DEVICE, O_RONLY );

    if( id_device != NOT_OPEN )
    {
      struct termios options;

      tcgetattr(uart0_filestream, &options);

      options.c_cflag = B9600 | CS8 | CLOCAL | CREAD;   //<Set baud rate
      options.c_iflag = IGNPAR;
      options.c_oflag = 0;
      options.c_lflag = 0;

      tcflush(uart0_filestream, TCIFLUSH);
      tcsetattr(uart0_filestream, TCSANOW, &options);
    } else
    {
      std::cout << "Unable to open Arduino communication port..." << std::endl;
    }

    return id_device;
  }

  int read_arduino( int id_device )
  {
    char buffer[ SIZE_BUFFER ];
    int check = read( id_device, (void *)buffer, sizeof( buffer ) );

    if( check != NOT_OPEN )
    {
      // Nothing to do
    } else
    {
      std::cout << "Unable to read arduino..." << std::endl;
    }
  }
}
