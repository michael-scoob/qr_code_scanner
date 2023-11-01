# Barcode Scanner Reader Repository
## Overview

This repository contains a Python script designed to read and interpret barcode scanner input. The script translates the input from a barcode scanner, which is connected via USB and emulates keyboard input, into a readable string. The data is then logged, and the barcode value is returned for further processing or display. This utility is particularly useful in retail, warehousing, and other environments where barcode scanning is a common requirement.
Key Features

### Barcode Reading: 
- Converts the input from a barcode scanner into a readable string.
- Logging: Logs every barcode scanned to bc_log.log, facilitating debugging and tracking of scanning history.
- Compatibility: Developed and tested on Linux-based systems, with potential to be adapted for other operating systems.

## Getting Started

Please refer to the Installation and Usage sections of this README for guidance on setting up and running the script.
Contributing
Contributions to enhance the functionality, improve compatibility, or fix issues are welcome. Please feel free to fork the repository, 
make your changes, and submit a pull request. For major changes or new features, please open an issue first to discuss what you would like to add or change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Supported Operating Systems

This script has been developed and tested on Linux-based systems. Due to its dependency on the `evdev` library, which is specific to Linux, the script might not work out-of-the-box on Windows or MacOS. If you are using a different operating system, you may need to find an alternative library or adjust the code to accommodate the equivalent input handling mechanisms on your system.

For Linux users, the script should work with any distribution, but you need to ensure that your user has the necessary permissions to read input devices. You may need to add your user to the `input` group or adjust the device permissions accordingly.

# Usage

    Clone this repository or download the Python code to your local machine.

    Make sure your barcode scanner is connected to your computer.

    Run the script:

    bash

    python barcode_reader.py

    Scan a barcode, and the read string will be displayed in the console.

    The scanned data will also be logged to bc_log.log.

## Logging

The script logs every barcode scanned to bc_log.log with a DEBUG level. This is useful for troubleshooting and tracking scanning history.

## Troubleshooting

If the script is not detecting the barcode scanner, ensure that the device is properly connected and recognized by your system. You may need to adjust the device path in the script (currently set to /dev/input/event0) to match your system's configuration.
