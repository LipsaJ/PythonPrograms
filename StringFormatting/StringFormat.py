age = 27
print("My age is: " + str(age))
print("My age is: {0}" .format(age))
print("There are {0} days in {1},{2},{3},{4},{5},{6} and {7}".format(31, "January","March","May","July","August","October","December"))
print("""Jan: {2}
feb: {0}
March: {2}
April: {1} 
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}
""".format(28,30,31))
#here can be used multiple times
print("My age is: %d" %age)
print("My age is: %d %s, %d %s" %(age, "years", 6 ,"months") )

for i in range (1,12):
    print("Number %2d square is %3d and cube is %4d"%(i,i**2,i**3))

print("Two Lines")
print("\n")
print("One Line")
print

for i in range(1,12):
    print("Number {0:2} square is {1:3} and cube is {2:4} ".format(i,i**2,i**3))
#so here its similary like line 9 and 10 but we are defining the width as well for example {0:2}
#0-first parameter,1-secnd,2-third

for i in range(1,12):
    print("Number {0:<2} square is {1:<3} and cube is {2:<4} ".format(i,i**2,i**3))
    #they are left formatted here.

print("Pi is approximatly %12f " % ( 22 / 7 ))

for i in range(1,12):
    print("Number {} square is {} and cube is {} ".format(i,i**2,i**3))

for i in range(1,12):
    print("Number {:2} square is {:3} and cube is {:4} ".format(i,i**2,i**3))