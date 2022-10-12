import os, os.path, time, datetime

a = (os.listdir())
path = 'consistfolder.txt'

f = open(path, "w+")

for i in a:
    isDir = os.path.isdir(i)
    if isDir == True:

        pos = i.split('_')

        dirdata = time.ctime(os.path.getctime(i))
        dirdata = datetime.datetime.strptime(dirdata, "%a %b %d %H:%M:%S %Y")
        dirdata = dirdata.strftime('%d.%m.%Y')

        if len(pos) == 2:
            f.writelines(i + "_" + '' + '_' + dirdata + "_" + "NAME" + "_" + "ADRESS" + "\n")
        if len(pos) == 3:
            f.writelines(i + "_" + dirdata + "_" + "NAME" + "_" + "ADRESS" + "\n")

f.close()