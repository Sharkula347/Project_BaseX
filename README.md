# Project_BaseX
This project provides module with functions for encoding binary data to printable ASCII characters and decoding such encodings back to binary data.

## How to work via module
1. Make shure that you have installed Python 3.9
2. Make shure that you have installed modules that listed in requirements.txt (use `pip install -r [PATH_TO_FILE]/requirements.txt` to get the modules)
3. Run a console
4. Type next command:

`python o_base.py`

5. Enjoy in use.

## Details
Programming language: Python 3.9

This software can encode all bytes-like objects (for example: files). Also it provides to choose encoding of encoded text and alphabet (from availabe alphabets in module or custom). Encoded file with new encoded name saves in the same dir where placed source file.

## Calculations
The growing % of outer text depends on the length of choosen alphabet. You can predict % of growing size by following formula:

`% = 8/log[2](N) - 1`, where N - length of choosen alphabet, 8 - bits in byte.

### Example

For Base64 we have:

`% = 8/log[2](64) - 1 = 8/6 = 1/3`

So, outer text will be longer by 1/3 than input sequence

## This software was developed for educational purposes
