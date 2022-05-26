alphebet = "abcdefghijklmnopqrstuvwxyz"
corres = {}
alphebet = alphebet.upper()
for i in alphebet:
    corres[i] = alphebet.index(i) + 1

fin = open('ride.in', 'r')
fout = open('ride.out', 'w')

cometName = fin.readline().strip()
groupName = fin.readline().strip()

returnvalueComet = 1
returnvalueGroup = 1
for i in cometName:
    returnvalueComet *= corres[i]

for i in groupName:
    returnvalueGroup *= corres[i]

if returnvalueComet % 47 == returnvalueGroup % 47:
    fout.write("GO\n")
else:
    fout.write("STAY\n")

