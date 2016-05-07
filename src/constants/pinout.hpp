#ifndef PINOUT_HPP
#define PINOUT_HPP

#include "bcm2835.h"

namespace
{
  const uint8_t MUX_ENGINE = RPI_V2_GPIO_P1_11;

  const uint8_t BRIDGE_H0_ENGINE = RPI_V2_GPIO_P1_13;
  const uint8_t BRIDGE_H1_ENGINE = RPI_V2_GPIO_P1_15;

  const uint8_t WATER_PUMP = RPI_V2_GPIO_P1_12;

  const uint8_t AG_SDA1_I2C = RPI_V2_GPIO_P1_03;
  const uint8_t AG_SCL1_I2C = RPI_V2_GPIO_P1_05;

  const uint8_t ARDUINO_TX = RPI_V2_GPIO_P1_08;
  const uint8_t ARDUINO_RX = RPI_V2_GPIO_P1_10;

  const uint8_t FRONT_GATE = RPI_V2_GPIO_P1_35;
  const uint8_t BACK_GATE = RPI_V2_GPIO_P1_36;
  const uint8_t LEFT_GATE = RPI_V2_GPIO_P1_37;
  const uint8_t RIGHT_GATE = RPI_V2_GPIO_P1_38;
}

#endif // PINOUT_HPP
