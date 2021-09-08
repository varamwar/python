name=input("enter your name:")
age=int(input("enter your age:"))
height=float(input("enter your height"))

print(name,age,height)
print("my name is",name,"my age is",age,"my height is",height)
print("my name is "+name,"my age is",age,"my height is",height)
print("my name is"+" "+name,"my age is",age,"my height is",height)
print("my name is %s my age is %d my height is %.1f"%(name,age,height))
print("my name is {} my age is {} my height is {}".format(name,age,height))
print("my name is {2} my age is {1} my height is {0}".format(height,age,name))
print(f"my name is {name} my age is {age} my height is {height}")






