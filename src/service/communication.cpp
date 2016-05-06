#include "communication.hpp"
#include <termios.h>
#include <unistd.h>

namespace IO
{
  const int SIZE_BUFFER = 50;

  int start_arduino()
  {
    int id_device = open( DEVICE, O_RONLY );

    if( id_device != NOT_OPEN )
    {
      struct termios options;

      tcgetattr( id_device, &options );

      options.c_cflag = B9600 | CS8 | CLOCAL | CREAD;   //<Set baud rate
      options.c_iflag = IGNPAR;
      options.c_oflag = 0;
      options.c_lflag = 0;

      tcflush( id_device, TCIFLUSH );
      tcsetattr( id_device, TCSANOW, &options );
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

    return check;
  }

  int write_arduino( int id_device )
  {
    char buffer[ SIZE_BUFFER ];
    int check = write( id_device, (void *)buffer, sizeof( buffer ) );

    if( check != NOT_OPEN )
    {
      //Nothing to do
    } else
    {
      std::cout << "Unable to write arduino..." << std::endl;
    }

    return check;
  }

  int stop_arduino( int id_device )
  {
    int check = close( id_device );

    if ( check != NOT_OPEN )
    {
      // Nothing to do.
    } else
    {
      std::cout << "Unable to close arduino..." << std::endl;
    }
  } 
}
