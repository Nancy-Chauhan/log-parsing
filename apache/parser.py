# how many request are success( 200-299) and how many fail(500-529)
# CLient errors ( 400-499)
# Total data sent during the time 
import re

regex = r"\d+\.\d+\.\d+\.\d+ - \S+ \[.*\] \".*?\" (\d+) (\d+|-).*"
success = 0
fail = 0
client_error = 0 
redirect = 0
total_data = 0
with open("npcassoc.org.access.log", 'r') as file:
    for line in file:
        match = re.match(regex, line)
        if match:
            status_code = int(match.group(1))
            if status_code >= 200 and status_code <=299:
                success +=1
            elif status_code >= 500:
                fail += 1
            elif status_code >= 400 and status_code <= 499:
                client_error +=1 
            elif status_code >= 300 and status_code <=399:
                redirect +=1
            else:
                print("unknown status code: ", status_code)
            if match.group(2) != "-":
                size = int(match.group(2))
                total_data += size
        else:
            print("line did not match", line)

print("Total size is: ",total_data)
print("Total count of 2xx:", success)
print("Total count of 5xx:", fail)

