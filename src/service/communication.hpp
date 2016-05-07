#ifndef COMMUNICATION_HPP
#define COMMUNICATION_HPP

#include <fcntl.h>    // Define some flags to open function.
#include <bcm2835.h>  // To access Raspberry Pi.
#include <cstdint>    // To use different width of int.

#define DEVICE "./dev/ttyACM0"
#define NOT_OPEN -1

#define YES true
#define NO false

namespace IO
{
    typedef char byte;

    bool is_bcm2835_init = NO;

    int start_arduino();
    int read_arduino( int );
    int write_arduino( int );
    int stop_arduino( int );

    byte* read_ag();

    int read_water_pump();
    int write_water_pump();

    int open_gate();

    int active_engine();


    void verify_bcm2835_init();
}

#endif // COMMUNICATION_HPP
