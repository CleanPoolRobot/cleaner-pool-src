#ifndef PINOUT_HPP
#define PINOUT_HPP

#include "bcm2835.h"

namespace
{
  const int POWER_SUPPLY_1 = RPI_V2_GPIO_P1_02;
  const int POWER_SUPPLY_2 = RPI_V2_GPIO_P1_04;

  const int MUX_ENGINE = RPI_V2_GPIO_P1_11;

  const int BRIDGE_H0_ENGINE = RPI_V2_GPIO_P1_13;
  const int BRIDGE_H1_ENGINE = RPI_V2_GPIO_P1_15;

  const int WATER_PUMP = RPI_V2_GPIO_P1_12;

  const int AG_SDA1_I2C = RPI_V2_GPIO_P1_03;
  const int AG_SCL1_I2C = RPI_V2_GPIO_P1_05;

  const int ARDUINO_TX = RPIO_V2_GPIO_P1_08;
  const int ARDUINO_RX = RPIO_V2_GPIO_P1_10;

  const int FRONT_GATE = RPIO_V2_GPIO_P1_35;
  const int BACK_GATE = RPIO_V2_GPIO_P1_36;
  const int LEFT_GATE = RPIO_V2_GPIO_P1_37;
  const int RIGHT_GATE = RPIO_V2_GPIO_P1_38;
}

#endif // PINOUT_HPP
