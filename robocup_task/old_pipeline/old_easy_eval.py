import sys

argv = sys.argv
if len(argv) < 2:
    print('Need logfile as parameter')
    exit('1')
logfile_name = argv[1]

logfile = open(logfile_name, 'r')
lines = logfile.readlines()

for each in lines:
    if 'memorized' in each:
        print(each)