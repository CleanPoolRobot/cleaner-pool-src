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

  byte* read_ag()
  {
    verify_bcm2835_init();

    const uint8_t ADDRESS = 0x68; // TODO: Research about the address.
    const int SIZE_DATA = 50;

    byte* data_read = ( byte* )malloc( SIZE_DATA );

    if( bcm2835_i2c_begin() )
    {
      bcm2835_i2c_setSlaveAddress( ADDRESS );

      bcm2835_i2c_read( data_read, SIZE_DATA );

      bcm2835_i2c_end();
    } else
    {
      cout << "Unable to begin I2C..." << endl;
    }

    return data_read;
  }

  int active_water_pump()
  {
    verify_bcm2835_init();

    bcm2835_gpio_fsel( WATER_PUMP, BCM2835_GPIO_FSEL_INPT );
    bcm2835_gpio_write( WATER_PUMP, HIGH );
  }

  int deactive_water_pump()
  {
    verify_bcm2835_init();

    bcm2835_gpio_fsel( WATER_PUMP, BCM2835_GPIO_FSEL_INPT );
    bcm2835_gpio_write( WATER_PUMP, LOW );
  }

  int open_gate( int gate )
  {
    verify_bcm2835_init();

    uint8_t pin_gate = select_gate( gate );

    uint8_t gates[ 4 ] = { FRONT_GATE, BACK_GATE,
                           LEFT_GATE, RIGHT_GATE };


    for( int index = 0; index < 4; index++ )
    {
      if( gates[ index ] != pin_gate )
      {
        bcm2835_gpio_fsel( gates[ index ], BCM2835_GPIO_FSEL_INPT );
        bcm2835_gpio_write( gates[ index ], LOW );
      } else
      {
        bcm2835_gpio_fsel( gates[ index ], BCM2835_GPIO_FSEL_INPT );
        bcm2835_gpio_write( gates[ index ], HIGH );
      }
    }
  }

  uint8_t select_gate( int gate )
  {
    uint8_t pin_gate = 0;

    switch ( gate )
    {
      case 1:
        pin_gate = FRONT_GATE;
        break;
      case 2:
        pin_gate = BACK_GATE;
        break;
      case 3:
        pin_gate = LEFT_GATE;
        break;
      case 4:
        pin_gate = RIGHT_GATE;
        break;
      default:
        cout << "Unable find gate..." << endl; 
    }

    return pin_gate;
  }

  void verify_bcm2835_init()
  {
     if( is_bcm2835_init == YES )
    {
      // Nothing to do.
    } else
    {
      bcm2835_init();
    }
  }
}