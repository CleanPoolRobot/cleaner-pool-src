#ifndef PINOUT_HPP
#define PINOUT_HPP

#include "bcm2835.h"

namespace
{
  const int POWER_SUPPLY_1 = RPI_V2_GPIO_P1_02;
  const int POWER_SUPPLY_2 = RPI_V2_GPIO_P1_04;

  const int MUX_PRESSURE = RPI_V2_GPIO_P1_07;
  const int MUX_ENGINE = RPI_V2_GPIO_P1_40;

  const int PRESSURE_B1 = RPI_V2_GPIO_P1_38;
  const int PRESSURE_B2 = RPI_V2_GPIO_P1_37;
  const int PRESSURE_B3 = RPI_V2_GPIO_P1_36;
  const int PRESSURE_B4 = RPI_V2_GPIO_P1_35;
  const int PRESSURE_B5 = RPI_V2_GPIO_P1_33;
  const int PRESSURE_B6 = RPI_V2_GPIO_P1_32;
  const int PRESSURE_B7 = RPI_V2_GPIO_P1_31;
  const int PRESSURE_B8 = RPI_V2_GPIO_P1_29;
  
  const int BRIDGE_H1_ENGINE = RPI_V2_GPIO_P1_11;
  const int BRIDGE_H2_ENGINE = RPI_V2_GPIO_P1_12;

  const int ENGINE_CONTROL = RPI_V2_GPIO_P1_13;

  const int AG_SDA1_I2C = RPI_V2_GPIO_P1_03;
  const int AG_SCL1_I2C = RPI_V2_GPIO_P1_05;
}

#endif // PINOUT_HPP
