# NMAP Scans with SCAN.PY 

### This script is a framework made for users that need to perform an NMAP scan but do not have knowledge or experience in using the command line very much. It provides prompts and questions to help craft an NMAP scan that will work for the user. The results are also saved in a local directory.

Once the script is run, it will asks the user for a target IP Address

```
Enter your target IP
```
If an invalid IP address is entered, the script will loop and continue to prompt for an accurate IP address.
```
Invalid IP Address
Enter your target IP
```

Once a valid IP address is given, the script will prompt for a scan type, and its corresponding flags.
```
Which of the following scans would you like to perform?
1. OS fingerprinting scan: -O
2. Aggressive Scan: -A
3. UDP Scan only: -sU
4. TCP SYN Stealth Scan: -sS
```
The script will then prompt the user to enter a number
```
Enter a number, 1-4
```
If an invalid input is given (numbers outside of 1-4, or anything else), the script will loop and continue to prompt for a valid input.

Once an option is selected, the script will output a notification that the scan has executed, and the actual nmap command that is run, with the user input included. The script will then output a notification that gives the path to the directory where the scans are stored.

```
Executing scan: nmap [FLAGS] [IPADDRESS] -oN [FILEPATH]
Scan stored at /nmap_scans
```

The script then executes the scan and records the nmap scan to the indicated file.