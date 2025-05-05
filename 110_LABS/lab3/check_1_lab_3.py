
s1 = "spam"
s2 = "ni!"

print("The Knights who say, " + s2)
# The Knights who say, ni!

print(3 * s1 + 2 * s2)
# spamspamspamni!ni!

print(s1[1])
# p

print(s1[1:3])
# pa

print(s1[2] + s2[:2])
# ani

print(s1 + s2[-1])
# spam!

print(s2.upper())
# NI!

print(s2.upper().ljust(4) * 3)
# NI! NI! NI! 

print()
print()

print(s2[0:2].upper())

print((s1.capitalize() + " " + s2.capitalize() + " ") * 3)

print(s1)

characters = s1.split("a")
      
print(characters)

print(s1[0:2]+s1[3:4])
