


inputfile = open("lab3poem.txt", "r", encoding="utf-8")


#for i in inputfile:
 #   print(i)

lines = inputfile.readlines()
for line in lines:
    print(line)

inputfile.close()
