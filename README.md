# Morse Code
Encodes or Decodes Morse code

## Requirements
Language Used = Python3<br />
Modules/Packages used:
* datetime
* optparse
* colorama
* time

## Input
It either takes input from a file or through its runtime.
### File Input
To give it a file to encode or decode, we can use the arguments "--encode" and "--decode" or '-e' or '-d' respectively.<br />
For example:<br />
* To encode
```bash
python morse_code.py --encode file_from_which_data_is_to_be_encoded
```
* To decode
```bash
python morse_code.py --decode file_from_which_data_is_to_be_decoded
```
### Runtime Input
If no file is specified, then the user will be asked to select an option to Encode or Decode a string.<br />
Then after specifying we have to provide the required string to be encoded or decoded.<br />
Finally the result would be displayed on the Command Line Interface.