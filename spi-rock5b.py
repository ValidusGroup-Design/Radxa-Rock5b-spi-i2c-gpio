
# * SPDX-License-Identifier: MIT OR LGPL-3.0-or-later
# *
#* Copyright (c) 2025 Fred Fisher
#* www.validusgroup.com
#*
#* This file is dual-licensed under the MIT and LGPL-3.0-or-later licenses.
#* You may choose to use it under either license.
#

import spidev
import time
import argparse
#loopback connect pins 19 & 21 radxa rock5b
# Default SPI device
SPI_BUS = 0  # Change to 1 if using SPI1
SPI_DEVICE = 0    # Change to 1 if using SPI1 CS1

# Default SPI parameters
DEFAULT_SPEED_HZ = 500000  # 500 kHz
DEFAULT_BITS = 8
DEFAULT_MODE = 0b00  # SPI Mode 0 (CPOL=0, CPHA=0)
DEFAULT_DELAY = 0

# Default SPI transfer data (same as C code)
DEFAULT_TX = [
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0x40, 0x00, 0x00, 0x00, 0x00, 0x95,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xF0, 0x0D
]

def hex_dump(data, prefix="RX"):
    """Print data in hex format."""
    print(f"{prefix} | " + " ".join(f"{byte:02X}" for byte in data))

def spi_transfer(tx_data, speed=DEFAULT_SPEED_HZ, bits=DEFAULT_BITS, mode=DEFAULT_MODE, delay=DEFAULT_DELAY):
    """Perform SPI transfer and return received data."""
    spi = spidev.SpiDev()
    spi.open(SPI_BUS, SPI_DEVICE)  # Open SPI device
    spi.max_speed_hz = speed
    spi.bits_per_word = bits
    spi.mode = mode

    print(f"SPI Mode: {mode}")
    print(f"Bits per Word: {bits}")
    print(f"Max Speed: {speed} Hz ({speed // 1000} KHz)")

    rx_data = spi.xfer2(tx_data)  # Corrected: Removed unsupported arguments
    spi.close()

    return rx_data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SPI Transfer Utility")
    parser.add_argument("-s", "--speed", type=int, default=DEFAULT_SPEED_HZ, help="Max speed (Hz)")
    parser.add_argument("-b", "--bits", type=int, default=DEFAULT_BITS, help="Bits per word")
    parser.add_argument("-m", "--mode", type=int, default=DEFAULT_MODE, help="SPI mode (0-3)")
    parser.add_argument("-d", "--delay", type=int, default=DEFAULT_DELAY, help="Delay (usec)")
    parser.add_argument("-p", "--payload", type=str, help="Hex payload (e.g., 'FF 00 AA')")
    args = parser.parse_args()

    # Parse payload if provided
    if args.payload:
        tx_data = [int(x, 16) for x in args.payload.split()]
    else:
        tx_data = DEFAULT_TX

    print("Sending SPI data...")
    hex_dump(tx_data, "TX")

    rx_data = spi_transfer(tx_data, speed=args.speed, bits=args.bits, mode=args.mode, delay=args.delay)

    print("Received SPI data...")
    hex_dump(rx_data, "RX")
