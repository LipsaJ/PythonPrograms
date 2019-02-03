#variables first
name = "Lipsa"
age = 27
print(name + ' : ' + str(age))
#(name + age) java automatically converts in print case , from int age to string age, python doesn’t do that (in a way its good you wont have weird errors because of type conversion)
a = 9
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b) #this is float
print(a//b) #this is whole number

parrot = 'Indian blue tota'
print(parrot)
print(parrot[8])
print(parrot[-1]) #starts from the right side
print(parrot[0:5]) #starting from 0 to 5 , first five letters
print(parrot[:6]) #print till 6th letter
print(parrot[6:]) #print from 7th letter
print(parrot[-4:2]) #this wont print anything as it cant go from one direction to other
print(parrot[-4:-5]) #this wont print anything , direction should be form left to right
print(parrot[-4:-1]) #this prints as direction is from left to right
print(parrot[-11:8]) #this prints as its correct from left to right direction
print(parrot[0:10:1])#o is starting 10 is ending one is difference
print(parrot[0:10:2])#o is starting 10 is ending one is difference
print(parrot[0:-2])#o is starting 10 is ending one is difference

numbers = "9,223,456,657,678,987,237,908,897"
print(numbers[1::4])
