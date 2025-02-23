# SPI Loopback Test Script

## Overview
This Python script facilitates SPI communication testing on the Radxa Rock5B by sending a predefined payload and receiving the response using a loopback connection. The script allows users to configure SPI settings such as speed, mode, and bit width via command-line arguments.

### Loopback Connection
For testing, connect the SPI pins:
- **MOSI (Pin 19) to MISO (Pin 21)**

## Prerequisites
Before running the script, ensure that SPI is enabled on your system and the required Python package is installed.

### Install Required Dependencies
The script requires the `spidev` module, which can be installed using:

```sh
pip install spidev
```

## Usage
Run the script with optional parameters for SPI settings:

```sh
python spi_loopback.py [-s SPEED] [-b BITS] [-m MODE] [-d DELAY] [-p PAYLOAD]
```

### Arguments
- `-s, --speed` : SPI speed in Hz (default: 500000 Hz)
- `-b, --bits` : Bits per word (default: 8)
- `-m, --mode` : SPI mode (0-3, default: 0)
- `-d, --delay` : Delay in microseconds (default: 0)
- `-p, --payload` : Hexadecimal payload (e.g., 'FF 00 AA')

### Example Usage
Send a custom payload at 1 MHz SPI speed in mode 1:

```sh
python spi_loopback.py -s 1000000 -m 1 -p "DE AD BE EF"
```

## License
```plaintext
SPDX-License-Identifier: MIT OR LGPL-3.0-or-later
Copyright (c) 2025 Fred Fisher
www.validusgroup.com
This file is dual-licensed under the MIT and LGPL-3.0-or-later licenses.
You may choose to use it under either license.
```

