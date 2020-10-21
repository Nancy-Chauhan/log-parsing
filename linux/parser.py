# Fetch which applications print how many lines of log
import re
from collections import Counter
regex = r"^\w+\s+\d+\s+\d+\:\d+\:\d+ \w+ ([^\(\[\:]+).*"
count = Counter()

with open("Linux_2k.log", 'r') as file:
    for line in file:
        match = re.match(regex, line)
        if not match:
            print(line)
            continue 
        application = match.group(1)
        count[application] += 1

for application, lines in count.items():
    print(application,lines)
