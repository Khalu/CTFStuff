A common CTF or Wargame challenge is to have a service that requires a PIN to be
entered over the network, often with netcat.  This script automates the submitting of
the PIN and prints the PIN and text sent back from the service when the reject text is not
returned.


## Arguments

--url     The url or IP with the service

--port    The port the service is on

--pin     The length of the PIN maximum of 8 default="4"

--reject  The text returned when the incorrect PIN is entered default="WRONG"


## Example
```
[Dev@DevMachine PINBrute]$ python3 ./PINBrute.py --url challenges.url --port 30229 --pin 4
FOUND PIN
0411
CORRECT
flag{flagtxt}


```

## Dependencies
socket, argparse
