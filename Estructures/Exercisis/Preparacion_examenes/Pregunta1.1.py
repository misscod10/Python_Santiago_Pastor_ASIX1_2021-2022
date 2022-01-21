"""
Programa que ordena tres nombres introduïts
per entrada estàndard.
"""
print("Primer?")
a = int(input())
print("Segon?")
b = int(input())
print("Tercer?")
c = int(input())
if a < b:
    if c < a:
        print("%s, %s i %s" % (c, a, b))
    elif c < b:
        print("%s, %s i %s" % (a, c, b))
    else:
        print("%s, %s i %s" % (a, b, c))
elif c < b:
    print("%s, %s i %s" % (c, b, a))
elif c < a:
    print("%s, %s i %s" % (b, c, a))
else:
    print("%s, %s i %s" % (b, a, c))