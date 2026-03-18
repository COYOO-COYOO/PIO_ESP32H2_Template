#include <Arduino.h>

void setup() {
  Serial.begin(115200);
  delay(1200);
  Serial.println();
  Serial.println("ESP32-H2 PlatformIO custom board test");
  Serial.printf("Chip model: %s\n", ESP.getChipModel());
  Serial.printf("CPU freq: %u MHz\n", getCpuFrequencyMhz());
  Serial.printf("Flash size: %u bytes\n", ESP.getFlashChipSize());
}

void loop() {
  static uint32_t last = 0;
  if (millis() - last > 1000) {
    last = millis();
    Serial.printf("Uptime: %lu ms\n", millis());
  }
}
