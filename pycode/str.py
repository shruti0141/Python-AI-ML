"""marks=int(input("enter the value"))
#b=20
#print(a+b)
if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"
   
   
print("grade of the student is", grade)

nesting if
marks=[90.1,"shru",31]
marks[0]="shru"
print(marks)"""

info ={
    "name"    :"shru",
    "subjects":["java","manual",10.2],
 
    "college" :"stjit",
    "topics": ("sql","selenium",12),
    "age"     :31

}
print(type(info))
      
   #with the help of key value we can access the value
print(info["topics"])   
info["name"]="sadhu"    
print(info)