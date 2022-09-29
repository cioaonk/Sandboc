import os
import time 
import re

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
invalid = True
path = ''


if os.name == 'nt':
   path = "C:/nmap_scans"
else:
   path = '~/nmap_scans'

exists = os.path.exists(path)

if exists == False:
   os.mkdir(path)


def check(ip):
   if(re.search(regex, ip)):
      # valid IP address (invalid = False)
      return False
   else:
      print("Invalid IP Address")
      # invalid = True
      return True

while invalid:
   ip = input("Enter your target IP \n")
   invalid = check(ip)

print("Which of the following scans would you like to perform:")
print("1. OS fingerprinting scan: -O")
print("2. Aggressive Scan: -A")
fl = input("1 or 2 \n")
# Verify input
while fl != "1" and fl != "2":
   fl = input("Please Enter valid input: 1 or 2 \n")
# scan options
if fl == "1":
   fl = "-O"
else:
   fl = "-A"
ts = str(time.time())

crafted_scan = "nmap {} {} -oN {}".format(fl, ip, path + "/scan_" + ts + ".txt")

print("Executing scan", crafted_scan)

time.sleep(3)
os.system(crafted_scan)
