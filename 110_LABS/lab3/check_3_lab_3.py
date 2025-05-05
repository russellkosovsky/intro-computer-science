


inputfile = open("lab3poem.txt", "r", encoding="utf-8")

firstline = inputfile.readlines(1)

secondline = inputfile.readlines(2)

thirdline = inputfile.readlines(3)

print(firstline)
print(secondline)
print(thirdline)

line = inputfile.readlines()

print(line[1:4])

inputfile.close()
