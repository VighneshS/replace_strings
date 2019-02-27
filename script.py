import json
from sys import argv

templateFileName = argv[1]
with open('params.json') as f:
    data = json.load(f)


def append_it(filename, append_value):
    return "{0}-{2}.{1}".format(*filename.rsplit('.', 1) + [append_value])


appended_file_name = append_it(templateFileName, "replaced")

with open(templateFileName, "rt") as source:
    with open(appended_file_name, "wt") as dest:
        for line in source:
            lineReplace = line
            for d in data:
                lineReplace = lineReplace.replace(d, data[d])
            dest.write(lineReplace)
