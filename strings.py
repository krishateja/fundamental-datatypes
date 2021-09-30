a="sky is blue and  i'm block"
l=a.split()
print(l)
b="sky-is-blue-and-i'm-block"
l1=b.split('-',2)
print(l1)
print(l1[0])
l1=b.rsplit('-',2)
print(l1)
c="vinod is chandu is raju is srinivas is teja"
l2=c.rsplit('is',2)
print(l2)
d="welcome to srinivas"
print(len(d))
e=d.capitalize()
print(e)
f=d.title()
print(f)
g=d.upper()
print(g)
print(d.lower())
print(d)
print(e)
print(e.swapcase())
print(d)
print(d.islower())
print(g.isupper())
print(f.istitle())
print(d.isdigit())
print(d.index('w'))
print(d.index('srinivas'))
print(d.find('i'))
print(d.find('4'))#it will give different value i.e-1
t="teja"
print(t)
print(len(t))
j=t.center(10)
print(j)
print(len(j))
s=t.ljust(20,'@')
print(s)
print(len(s))
print(j)
z=j.strip()
print(z)
print(len(z))
print(j)
x=j.rstrip()
print(x)
print(len(x))
print(j)
print(j.count('e'))
print(t)
x=t.center(20,"@")
print(x)
print(t.strip('@'))
print(t.center(20,"@"))
print(x.rstrip("@"))
print(t)
print(t.isalpha())
print(t.isalnum())
#partition
s1="india is dubai russia india is capital"
print(s1.partition('russia'))
print(s1.partition('india'))
print(s1.rpartition('india'))
s3="iam teja and iam a badboy"
print(s3)
print(s3.replace("teja","raju"))
a="abc-def@gmail.com"
b=a.split('@')
print(b)
list=([a[0:3:1],a[4:7:1],a[8:18:1]])
print(list)
print(len(list[0]),len(list[1]),len(list[2]))
print('first name',list[0])
print('second name',list[1])
print('domain name',list[2])
print(b)
print(b[0])
print(b[1])
list1=b[0]
list2=list1.split('-')
print(list2)
print(list2[0])
print(list2[1])
print('first name',list2[0])
print('second name',list2[1])
print('domain name',b[1])
#replace
s="""I'm java developer,java is oops language,java is compiler based language,i love java"""
print(s)
print(s.replace('java','python'))
s1=s.split(',')
print(s1)
s2=(s1[0],s1[1],s1[2],s1[3].replace('java','python'))
print(s2)
s3=(s1[0], s1[1].replace('java','python'),s1[2].replace('java','python'),s1[3])
print(s3)
s="""I'm java developer,
     java is oops language,
     java is compiler based language 
     i love java"""
print(s)
print(s.replace("love java","love python"))
print(s.replace("java is","python is",2))
#arithmetic operators
a=input("enter any three values:")
print(a)
b=a.split()
print(b)
print(type(b[0]))
c=int(b[0])
d=int(b[1])
e=int(b[2])
print(c)
print(d)
print(e)
print(type(c))
print("addition of three numbers:",c+d+e)
print("subtraction of three numbers:",c-d-e)
print("multiplication of three numbers:",c*d*e)
print("division of three numbers:",c/d/e)
# students details
a=input("Enter student details")
b=a.split()
print(b)
print(b[0].isdigit(),b[1].isdigit(),b[2].isdigit,b[3].isdigit(),b[4].isdigit())
print(type(b[2]))
z=b[0]
x=b[1]
c=int(b[2])
d=int(b[3])
e=int(b[4])
print(type(c))
print("student name:",z)
print("student class:",x)
print("total marks(add all three subjects):",c+d+e)
print("average of three subjects:",(c+d+e)/3)
name= "krishnateja"
print("good morning",name)
print("good moring"+name)  #string +string= concatenation
a=1000
print("I have rupees",a)
# print("i have rupees"+a)  string can concatenate with string only not int
print("i have rupees"+str(a))
b=2000
print("#AAA=",a,end="\n")
print("#BBB=",b)
print("#AAA=",a)# by default it will take \n
print("#BBB=",b)
print("AAA=",a,end=" ")
print("BBB=",b)
print(a,b)
print(a,b,sep="\n")
print(a,b,sep="@@@@@@")
print("krishna:{} teja:{}".format(79,98))
str="my is country {}"
print(str)
print(str.format("india"))
#print("my country is "india"") in this code we given in between doble quotes again double quotes
print('my country is "india"' #in this code we given in between single quotes as double quotes
a=input("enter values:")
print(a)
#map for number of strings numbers to int
print(type(a[0]))
A=list(map(int,a.split()))
print(A)
print(type(A[0]))
a=input()# inbuild input have string format if u give any value in that by defult it will take string
b=input()#string+string=concatination
d=a+b
print(d)
a="10"
b="krishna"
c=b+a#string +string=both concatinate
print(c)
a=5
b=6
c=a+b #int adding to another int it will give result
print(c)
a=input("enter one number")
b=input("enter one number")
c=a+b#by default in input we have string so if we give any int it will convert string format so the ans will concatinate
print(c)
a=input("enter one number for operations")
b=input("enter second number for operations")
c=int(a)+int(b)
d=int(a)*int(b)
e=int(a)-int(b)
f=int(a)/int(b)
print("addition of two numbes:",c)
print("multiplication of two numbers:",d)
print("substraction of two numbers:",e)
print("divison of two numbers:",f)
a=5
b="teja"
c=a+b#can't add one string and one int
print(c)
a=input("enter one number for checking type")
b=input("enter another number for checking type")
print(type(a))
print(type(b))
print(id(a))#a in this string form so store in different memory location
print(id(b))
c=int(a)
d=int(b)
print(type(c),id(c)) #we convert a into int form  and assign in c so is int and store in different memory location
print(type(d),id(d))
marks="aa={},bb={},cc={},dd={}"
print(marks.format(7,5,6,5))
print("aa={i},bb={j},cc={k},dd={l}".format(j=85,i=65,l=85,k=55))



