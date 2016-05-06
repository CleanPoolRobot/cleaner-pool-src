#ifndef COMMUNICATION_HPP
#define COMMUNICATION_HPP

#include <fcntl.h> // Define some flags to open function.

#define DEVICE "./teste.txt"
#define NOT_OPEN -1

namespace IO
{
    int start_arduino();
    int read_arduino( int );
    int write_arduino( int );
    int stop_arduino( int );

    int read_ag();
    int write_ag();

    int read_water_pump();
    int write_water_pump();

    int open_gate();

    int active_engine();
}

#endif // COMMUNICATION_HPP
