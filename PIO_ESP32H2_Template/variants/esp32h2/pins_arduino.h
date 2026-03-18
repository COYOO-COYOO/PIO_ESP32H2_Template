#ifndef Pins_Arduino_h
#define Pins_Arduino_h

#include <stdint.h>

// Minimal ESP32-H2 variant shim for PlatformIO's Arduino build.
// UART0 defaults come from the SDK and match the documented ROM pins.
static const uint8_t TX = 1;
static const uint8_t RX = 3;

#endif
