print("--------STUDENT MARKS MANAGEMENT SYSTEM--------\n")
stuName=[]
stuRoll=[]
stuEng=[]
stuMath=[]
stuScience=[]
Pass=[]
#entering names of 5 students
stuName.append(input("Enter name of student 1:"))
stuName.append(input("Enter name of student 2:"))
stuName.append(input("Enter name of student 3:"))
stuName.append(input("Enter name of student 4:"))
stuName.append(input("Enter name of student 5:"))
print("Student names:",stuName)
#entering roll numbers of 5 students
stuRoll.append(int(input("Enter roll no of student 1:")))
stuRoll.append(int(input("Enter roll no of student 2:")))
stuRoll.append(int(input("Enter roll no of student 3:")))
stuRoll.append(int(input("Enter roll no of student 4:")))
stuRoll.append(int(input("Enter roll no of student 5:")))
print("Students roll no:",stuRoll)
#entering marks in English
stuEng.append(int(input(f"Enter marks {stuName[0]} in English:")))
stuEng.append(int(input(f"Enter marks {stuName[1]} in English:")))
stuEng.append(int(input(f"Enter marks {stuName[2]} in English:")))
stuEng.append(int(input(f"Enter marks {stuName[3]} in English:")))
stuEng.append(int(input(f"Enter marks {stuName[4]} in English:")))
print("Students english marks:",stuEng)
#entering marks of Math
stuMath.append(int(input(f"Enter marks {stuName[0]} in Maths:")))
stuMath.append(int(input(f"Enter marks {stuName[1]} in Maths:")))
stuMath.append(int(input(f"Enter marks {stuName[2]} in Maths:")))
stuMath.append(int(input(f"Enter marks {stuName[3]} in Maths:")))
stuMath.append(int(input(f"Enter marks {stuName[4]} in Maths:")))
print("Students maths marks:",stuMath)
#entering marks of Science
stuScience.append(int(input(f"Enter marks {stuName[0]} in Science:")))
stuScience.append(int(input(f"Enter marks {stuName[1]} in Science:")))
stuScience.append(int(input(f"Enter marks {stuName[2]} in Science:")))
stuScience.append(int(input(f"Enter marks {stuName[3]} in Science:")))
stuScience.append(int(input(f"Enter marks {stuName[4]} in Science:")))
print("Students science marks:",stuScience)
#total of 5 students in each subject
total_stu1=stuEng[0]+stuMath[0]+stuScience[0]
total_stu2=stuEng[1]+stuMath[1]+stuScience[1]
total_stu3=stuEng[2]+stuMath[2]+stuScience[2]
total_stu4=stuEng[3]+stuMath[3]+stuScience[3]
total_stu5=stuEng[4]+stuMath[4]+stuScience[4]
#percentage marks of 5 students
per_stu1=total_stu1/300*100
per_stu2=total_stu2/300*100
per_stu3=total_stu3/300*100
per_stu4=total_stu4/300*100
per_stu5=total_stu5/300*100
#pass status of student 1
if(stuEng[0]>=35 and stuMath[0]>=35 and stuMath[0]>=35):
    Pass.append("Pass")
else:
    Pass.append("Fail")
#pass status of student 2
if(stuEng[1]>=35 and stuMath[1]>=35 and stuScience[1]>=35):
    Pass.append("Pass")
else:
    Pass.append("Fail")
#pass status of student 3
if(stuEng[2]>=35 and stuMath[2]>=35 and stuScience[2]>=35):
    Pass.append("Pass")
else:
    Pass.append("Fail")
#pass status of student 4
if(stuEng[3]>=35 and stuMath[3]>=35 and stuMath[3]>=35):
    Pass.append("Pass")
else:
    Pass.append("Fail")
#pass status of student 5
if(stuEng[4]>=35 and stuMath[4]>=35 and stuMath[4]>=35):
    Pass.append("Pass")
else:
    Pass.append("Fail")
print("--------------------------------REPORT OF 5 STUDENTS GENERATED--------------------------------\n")
print("Status=True:student is Pass, Status=False:student is failed")
print("-----------------------------------------------------------------------------------------------\n")
print(f"Name:{stuName[0]}=>RollNo:{stuRoll[0]}=>Marks:{total_stu1}=>Percent:{per_stu1:.2f}=>Status={Pass[0]}")
print(f"Name:{stuName[1]}=>RollNo:{stuRoll[1]}=>Marks:{total_stu2}=>Percent:{per_stu2:.2f}=>Status={Pass[1]}")
print(f"Name:{stuName[2]}=>RollNo:{stuRoll[2]}=>Marks:{total_stu3}=>Percent:{per_stu3:.2f}=>Status={Pass[2]}")
print(f"Name:{stuName[3]}=>RollNo:{stuRoll[3]}=>Marks:{total_stu4}=>Percent:{per_stu4:.2f}=>Status={Pass[3]}")
print(f"Name:{stuName[4]}=>RollNo:{stuRoll[4]}=>Marks:{total_stu5}=>Percent:{per_stu5:.2f}=>Status={Pass[4]}")

