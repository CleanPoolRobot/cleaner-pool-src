#include "communication.hpp"
#include <termios.h>
#include <unistd.h>
#include <iostream>
using namespace std;
namespace IO
{
  const int SIZE_BUFFER = 50;

  int start_arduino()
  {
    int id_device = open( DEVICE, O_RDWR | O_CREAT );

    if( id_device != NOT_OPEN )
    {
      std::cout << "Abri o arquivo " << std::endl;
      /*struct termios options;

      tcgetattr( id_device, &options );

      options.c_cflag = B9600 | CS8 | CLOCAL | CREAD;   //<Set baud rate
      options.c_iflag = IGNPAR;
      options.c_oflag = 0;
      options.c_lflag = 0;

      tcflush( id_device, TCIFLUSH );
      tcsetattr( id_device, TCSANOW, &options );*/
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
      std::cout << "Estou lendo aqui o arquivo .. " << std::endl;
      // Nothing to do
      if(buffer[0] == 'A')
        std::cout << "EHHH PEGUEI UM A NO ARQUIVO" << std::endl;
    } else
    {
      std::cout << "Unable to read arduino..." << std::endl;
    }

    return check;
  }

  int write_arduino( int id_device )
  {
    char buffer[ SIZE_BUFFER ];
    buffer[0] = 'A';
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