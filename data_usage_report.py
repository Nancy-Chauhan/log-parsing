# Bandwidth consumption of a Web server
#
# Apache logs are stored in a format called Common Log Format. In order to keep log files in reasonable sizes, we use a program called logrotate which splits a log file into parts in hourly/daily/weekly cycles.
#
# We need to investigate the data transferred per IP address.
#
# Given: a folder containing apache logs in CLF format.
#
# Design a script to parse the logs in all the log files in the given folder and print the data transferred to each unique IP address (in bytes)
#
# Sample invocation:
#
# python3 data_usage_report.py /var/log/apache2
#
# Output:
#
# 1.1.1.1: 4444444
# 2.2.2.2: 333344
# 3.3.3.3: 44444


import csv
import os
import re
import sys

regex = r"(\d+\.\d+\.\d+\.\d+) - \S+ \[.*\] \".*?\" \d+ (\d+).*"


def data_usage_report(directory):
    store_dict = {}
    for f in os.listdir(directory):
        if not f.endswith(".log"):
            continue
        with open(os.path.join(directory, f), 'r') as file:
            for line in file:
                match = re.match(regex, line)
                if match:
                    ip = match.group(1)
                    value = int(match.group(2))
                    if ip not in store_dict:
                        store_dict[ip] = 0
                    store_dict[ip] += value
                else:
                    print("line did not match", line)
    return store_dict


def write_csv(data_by_ip, output):
    fieldnames = ["ip", "bytes_sent"]
    with open(output, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for ip, value in data_by_ip.items():
            writer.writerow({"ip": ip, "bytes_sent": value})


def main():
    write_csv(data_usage_report(sys.argv[1]), sys.argv[2])


if __name__ == "__main__":
    main()
