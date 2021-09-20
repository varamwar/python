'''print types'''
# print("hello world")
# print('hello world')
# print('''hello world''')
# print("""hello world""")
# print("hello","world")
# print("hello "+"world")
# print('hello''world')
# print("hello""world")
# print("hello ""world")
# print('hello '+'world ')
# print("hello""world")
# print("hello"" world")
# print("""hello """ """world""")
# print("""hello""" """ world""")
# print("hello","world",sep=" ")




'''end method'''

# a="varam"
# b="prasad"
# print(a,b,end=".")
# a="varaprasad"
# b="ramatenki"
# C="@gmail"
# print(a,b,C,end=".com",sep="")

# print(a)




'''Separate method'''





# a="varam"
# b="war"
# c="00"
# print(a,b,c,sep=".")
# print(a,b,c,sep="_")
# print("hello","world",sep=" ")



'''combination of end and sep'''


# a="varaprasad"
# b="ramatenki"
# C="@gmail"
# print(a,b,C,end=".com",sep="")

'''Escape Sequences'''
# print("hell \nworld")
# print("varam\nwar")
# print("varam\bwar")
# print("varam \bwar")
# print("varam  \bwar")
# print("varam \twar")
# print("varam\twar")
# print("\tvaramwar")
# print("vara\t mwar")
# print("\u0001")
# print("\u0002")
# print("\u0003")
# print("\u0004")
# print("\u0005")
# print("\u0006")
# print("\U0001f601")
# print("\U0001f602")
# print("\U0001f603")
# print("\U0001f604")
# print("\U0001f605")
# print("\U0001f606")
# print("\U0001f611")
# print("kjhfkjsdfhkdhfkfhwk\
# iohfiwfhweifhw")
# print("ramatenki\'varaprasad")
# print("ramatenki\"varaprasad")
# print("ramatenki\\varaprasad")
# print("C:\\Users\\Josh\\Desktop\\incline\\inline>")



'''Variables'''
'''first way'''
# a=1   
# A=2
# _b=3
# _1=4
# c_a=5
# v_2=464
# # print(a)
# # print(_b)
# # print(_1)
# # print(c_a)
# # print(v_2)
# # print(a,_1,v_2,sep="@"
# print(a),print(A),print(_b),print(c_a)



'''second way'''
# a=12;b=46;_1=211
# print(a,b,_1)

'''third way'''
# a,b,c,d=1,2,3,4
# print(a)
# print(b)
# print(c)
# print(d)
# print(a,b,c,d)
'''fourth way'''
# a=b=2;c=d=e=25
# print(a)
# print(b)
# print(c,d,e)

'''Format specifier'''
'''%d'''
# a=5  #int,%d,%i
# b=5.5  #float %f
# c="varam"  #string %s
# d=555     # int %d,%i
# print("the value of a is %d"%a)
# print("the value of b is %f"%a)
# e=print("the value of d is %s"%d)
# e=print("the value of d is %s"%d)
# print(type(e))

'''INDEX VALUES'''
# war='varam'
# print(war[0]) #v
# print(war[1]) #a
# print(war[2]) #r
# print(war[3]) #a
# print(war[4]) #m
# print(war[5])  #string index out of range

'''Type conversion  '''
'''int to float and string'''
# a=5
# print(a,type(a)) #5 <class 'int'>
# b=float(a)
# print(b,type(b)) #5.0 <class "float">
# war=str(a)
# print(war,type(war))

'''float to int and string'''
# c=5.0
# print(c,type(c))
# v=int(c)
# print(v,type(v))
# m=str(c)
# print(m,type(m))

'''string to int and float'''
# a="varam"
# print(a,type(a))
# b=int(a)
# print(b,type(b))
# c=float(a)
# print(c,type(c))

'''string values to int and float'''
# a="123456"
# print(a,type(a))
# b=int(a)
# print(b,type(b))
# c=float(a)
# print(c,type(c))


'''string values in float to float and int '''


# a="555.00"
# print(a,type(a))
# b=int(a)
# print(b,type(b))
# c=float(a)
# print(c,type(c))
# d=int(c)
# print(d,type(d))


'''INPUT TYPES'''


# a=input("")
# print("my pubg ID is :"+a)
# print("My pubg ID is ",a)
# a=int(input(""))
# print("my name is",a,type(a))


'''int'''

# a=int(input(""))
# print("my id is",a)
# print("my id is",a,type(a))

'''float'''

# a=float(input())
# print("my salary is",a)     #my salary is 5555.0
# print("my salary is",a,type(a))  # my salary is 5555.0 <class 'float'>


'''WAY TO PRINT INPUT TYPES'''

# name=input("")
# age=int(input())
# height=float(input())


'''1st way'''
# print(name,age,height)

'''2nd way'''

# print("my name is",name,"my age is",age,"age height",height)

''' 3rd way'''

# print("my name is "+name,"my age is",age,"age height",height)

'''4th way'''

# print("my name is"+" "+name,"my age is",age,"age height",height)




'''5th way'''

# print("my name is %s"%name,"my age is %d"%age,"my height %.2f"%height)
# print("my name is %s my age is %d my height %.2f"%(name,age,height))


'''6th way'''

# print("my name is {} my age is {} and my height is {}".format(name,age,height))



'''7th way'''

# print("my name is {0} my name is {1} and my height {2}".format(name,age,height))


'''8th way'''


# print(f"my name is {name} my name is {age} and my height {height}")

'''OPERATOR'''
'''arthematic operators'''

# a=int(input(""))
# b=int(input(""))
# print(a+b)
# print(f"the value of {a}+{b} is {a+b}")
# print(f"the value of {a}*{b} is {a*b}")
# print(f"the value of {a}-{b} is {a-b}")
# print(f"the value of {a}%{b} is {a%b}")
# print(f"the value of {a}**{b} is {a**b}")
# print(f"the value of {a}/{b} is {a/b}")


# a=5
# b=2
# print(a+b)
# print(f"the value of {a}+{b} is {a+b}")
# print(f"the value of {a}*{b} is {a*b}")
# print(f"the value of {a}-{b} is {a-b}")
# print(f"the value of {a}%{b} is {a%b}")
# print(f"the value of {a}**{b} is {a**b}")
# print(f"the value of {a}/{b} is {a/b}")


'''assignment operator'''

# a=5
# b=4
# a+=4
# b+=50
# print(a,b)
# print(b)

# a=5
# a+=3
# print(a) #a=a+3  a=5+3  a=8


# a=5
# a-=2
# print(a)

# a=5
# a*=2
# print(a)


# a=5
# a/=2
# print(a)

# a=5
# a*=3
# print(a)

# a=5
# a**=3
# print(a)

# a=int(input(""))
# print(f'the value of a is {a}',type(a))


# a=1
# a+=2
# print("the value of a after a+=2 is {}".format(a))


# a=5
# a-=4
# print("the value of a after p-=4 is {}".format(a))


# a=5
# a*=4
# print("the value of a after p-=4 is {}".format(a))


# a=5
# a**=4
# print("the value of a after p-=4 is {}".format(a))




# a=5
# a/=4
# print("the value of a after p-=4 is {}".format(a))



'''RELATIONAL COMPARISION OPERATOR'''


# a=int(input())
# b=int(input())
# print(f"the value of {a}<{b} is {a<b}")
# print(f"the value of {a}>{b} is {a>b}")
# print(f"the value of {a}<={b} is {a<=b}")
# print(f"the value of {a}>={b} is {a>=b}")
# print(f"the value of {a}=={b} is {a==b}")
# print(f"the value of {a}!={b} is {a!=b}")


# a="RELATIONAL COMPARISION OPERATOR WITH SPECIFIERS"
# print(a.lower())




'''relational comparision operator with using specifiers'''


# a=5
# b=6
# print("the value of %d<%b=%d"%(a,b,a<b))
 

# a=int(input())
# b=int(input())
# print("the value of %d<%d=%d"%(a,b,a<b))                #the value of 1<2=1
# print("the value of a=%d,b=%d and a<b=%d"%(a,b,a<b))    #the value of a=1,b=2 and a<b=1 
# print("the value of a=%d,b=%d and a>b=%d"%(a,b,a>b))    #the value of a=1,b=2 and a>b=0 
# print("the value of a=%d,b=%d and a<=b=%d"%(a,b,a<=b))  #the value of a=1,b=2 and a<=b=1
# print("the value of a=%d,b=%d and a>=b=%d"%(a,b,a>=b))  #the value of a=1,b=2 and a>=b=0
# print("the value of a=%d,b=%d and a==b=%d"%(a,b,a==b))  #the value of a=1,b=2 and a==b=0
# print("the value of a=%d,b=%d and a!=b=%d"%(a,b,a!=b))  #the value of a=1,b=2 and a!=b=1



'''LOGICAL OPERATOR'''


# a=int(input())
# b=int(input())
# print("the value of a<b and b>a is {}".format(a<b and b>a))      #the value of a<b and b>a is True 
# print("the value of a>b and b<a is {}".format(a>b and a<b))      #the value of a>b and b<a is False 
# print("the value of a!=b and b==a is {}".format(a!=b and a==b))  #the value of a!=b and b==a is False
# print("the value of a==b and b>a is {}".format(a==b or a>b))     #the value of a==b and b>a is False
# print("the value of a<b and b>a is {}".format(a!=b or b==a))     #the value of a<b and b>a is True 
# print("the value of a<b and b>a is {}".format(a,b, not a==b))    #the value of a<b and b>a is 1    
# print("the value of a<b and b>a is {}".format(a,b, not a!=b))    #the value of a<b and b>a is 1   #



'''BITWISE OPERATOR'''
# a=2;b=3
# a=int(input(""))
# b=int(input(""))
# # c=int(input(""))
# print("the value of {} & {} is {}".format(a,b,a&b))
# print("the value of {} | {} is {}".format(a,b,a|b))
# print("the value of {}~{} is {}".format(a,~a))
# # print("the value of {}~{} is {}".format(c,~c))          ***doubt***





'''IDENTITY OPERATOR'''

# a=5
# b=[5]
# c=6
# d=a
# e=5
# f=[5]
# print(f"the value of {a} is {b}={a is b}")          #the value of 5 is [5]=False   
# print(f"the value of {a} is {c}={a is c}")          #the value of 5 is 6=False
# print(f"the value of {a} is {d}={a is d}")          #the value of 5 is 5=True
# print(f"the value of {a} is {e}={a is e}")          #the value of 5 is 5=True
# print(f"the value of {e} is {a}={e is a}")          #the value of 5 is 5=True
# print(f"the value of {a} is not {b}=",a is not b)   #the value of 5 is not [5]= True 
# print(f"the value of {a} is not {c}=",a is not c)   #the value of 5 is not 6= True 
# print(f"the value of {a} is not {d}=",a is not d)   #the value of 5 is not 5= False 
# print(f"the value of {b} is not {f}=",b is not f)   #the value of [5] is not [5]= True

'''MEMBERSHIP OPERATOR'''

# n=[1,4.5,"python"]
# print(n,type(n))              # [1, 4.5, 'python'] <class 'list'>
# print(n[0],type(n[0]))        #1 <class 'int'>
# print(n[1],type(n[1]))        #4.5 <class 'float'>
# print(n[2],type(n[2]))        # python <class 'str'>
# print(n[3],type(n[3]))        #IndexError: list index out of range

# print(f"the value of {n[0]} in n is {n[0] in n }")    #the value of 1 in n is True
# print(f"the value of {n[1]} in n is {n[1] in n }")    #the value of 4.5 in n is True
# print(f"the value of {n[2]} in n is {n[2] in n }")    #the value of python in n is True
# print(f"the value of {n[3]} in n is {n[3] in n }")    #IndexError: list index out of ra



'''NUMBER SYSTEM'''


# a=5
# b=4.5
# print(a,type(a))                  #5 <class 'int'>
# print(b,type(b))                  #4.5 <class 'float'>
# print(isinstance(a,int))          #True
# print(isinstance(b,int))          #False
# print(isinstance(a,float))        #False
# print(isinstance(b,float))        #True
# print(isinstance(a,str))          #False
# print(isinstance(b,str))          #False              #
 
'''note :syntax isinstance (variable,datatype)'''

# c=2j
# print(c)                      #2j
# d=1+3j
# print(d,type(d))              #(1+3j) <class 'complex'>
# print(isinstance(d,complex))  # True 

# e=0+0j
# print(e)       #0j
# f=(1-3j)
# print(f)      #(1-3j)
# g=(0-3j)
# print(g)     #-3j
# h=(0+(-3j))
# print(h)      #-3j
# j="0.1"+"0.2"
# print(j)   #0.10.2
# k=float(j)
# n=float(0.1)+float(0.2)
# print(n)




'''Import Decimal'''
from decimal import Decimal as D
v=decimal(0.1)+decimal(0.2)
print(v)


