#Fail2ban: Print ip address if it has 3 or more SSH authentication failures

import re
from collections import Counter
regex = r".*Failed password.*from (\d+\.\d+\.\d+\.\d+) port .*"
ip_addresses = Counter()
with open("SSH_2k.log",'r') as file:
    for line in file:
        match = re.match(regex, line)
        if not match:
            continue
        ip_address = match.group(1)
        ip_addresses[ip_address] += 1 
        if ip_addresses[ip_address] == 3:
            print(ip_address)
