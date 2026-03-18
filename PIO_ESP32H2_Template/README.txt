1) Open the project in VS Code / PlatformIO
2) Let PlatformIO resolve the pinned packages from `platformio.ini`
3) Run `python scripts/patch_platform.py` if your local `platform-espressif32` still needs the ESP32-H2 builder patch
4) Run `pio run -t clean`
5) Run `pio run`

This revision now relies on:
- `build.f_flash = 48m` in the custom board definition
- a repo-local `variants/esp32h2/bootloader.bin` so PlatformIO does not look for a missing `bootloader_qio_48m.elf`
- a pinned `espressif/toolchain-riscv32-esp @ 12.2.0+20230208` to avoid the incompatible `14.2.0+20251107` toolchain
- a minimal repo-local `variants/esp32h2/pins_arduino.h` shim for Arduino ESP32 3.0.2
