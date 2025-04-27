# Ligawo 6518868 HDMI Matrix Switch RS232 Integration

This Home Assistant integration allows you to control the **Ligawo 6518868 PRO HDMI Matrix 4x4 Switch** via **RS232** communication.

## Features

- Configure the serial **port** and **baud rate** easily through the Home Assistant **UI** (config flow).
- Automatically creates **four `select` entities** — one for each output — allowing you to select any of the four HDMI inputs.
- Automatically updates the status of all outputs **every 30 seconds** to reflect any changes made directly on the device.
- Local communication (no cloud connection required).

## Special Thanks

Huge thanks to [@targor](https://github.com/targor/lgwo_6518868_reverseEngineered) for reverse engineering the RS232 codes for the Ligawo 6518868 matrix switch!

---

## Installation

1. Copy the `hdmi_matrix` folder into your Home Assistant `custom_components/` directory.
2. Restart Home Assistant.
3. Add the Ligawo HDMI Matrix via **Settings → Devices & Services → Add Integration** and search for "**Ligawo HDMI Matrix**".
4. Enter your serial **port** and **baud rate** when prompted.

## Configuration Example (if needed manually)

```yaml
# Normally not required if using the UI
hdmi_matrix:
  port: "/dev/ttyUSB0"
  baudrate: 19200
```

---

## Requirements

- A working RS232 connection to the matrix switch.
- `pyserial` is automatically handled via Home Assistant (no manual installation required).
