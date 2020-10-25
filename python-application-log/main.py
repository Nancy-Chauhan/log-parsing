import re


def generate_dicts(log_fh):
    currentDict = {}
    for line in log_fh:
        if line.startswith(match_date(line)):
            if currentDict:
                yield currentDict
            currentDict = {"date": line.split("__")[0][:19], "type": line.split("-", 5)[3],
                           "text": line.split("-", 5)[-1]}
        else:
            currentDict["text"] += line
    yield currentDict


def match_date(line):
    matchThis = ""
    matched = re.match(r'\d\d\d\d-\d\d-\d\d\ \d\d:\d\d:\d\d', line)
    if matched:
        # matches a date and adds it to matchThis
        matchThis = matched.group()
    else:
        matchThis = "NONE"
    return matchThis


if __name__ == '__main__':
    with open("test.log") as f:
        listNew = list(generate_dicts(f))
        print(listNew)
