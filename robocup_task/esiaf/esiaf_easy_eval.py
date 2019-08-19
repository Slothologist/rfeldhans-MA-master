import sys

argv = sys.argv
if len(argv) < 2:
    print('Need logfile as parameter')
    exit('1')
logfile_name = argv[1]

logfile = open(logfile_name, 'r')
text = logfile.read()

speech = text.split('speechInfo')[1:]
print('number of speech recognitions: ' + str(len(speech)))
for each in speech:
    info = each.split('sslInfo')[0].split('\n')
    for i in range(0, len(info)):
        if 'finish' in info[i]:
            print(info[i+1].strip())

    lines = each.split('\n')
    values = []
    for line in lines:
        if 'recognizedSpeech' in line:
            print(line.split(':')[1].strip())
        if 'Horizontal' in line:
            values.append(float(line.split(':')[1]))
    print(sum(values)/len(values))
    print('')
