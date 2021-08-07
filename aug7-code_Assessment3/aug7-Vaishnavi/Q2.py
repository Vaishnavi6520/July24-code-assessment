import re,sys,json,smtplib
# try:
header=['total','name','rollno','admno','college','parentname','mobilenumber','emailid','sub1mark','sub2mark','sub3mark','sub4mark','sub5mark']
studentlist=[]
class Studentdetail:
    def addStudent(self,name,rollno,admno,college,parentname,mobilenumber,emailid):
        self.name=name
        self.rollno=rollno
        self.admno=admno
        self.college=college
        self.parentname=parentname
        self.mobilenumber=mobilenumber
        self.emailid=emailid
class Marks:
    def mark (self,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark):
        self.sub1mark=sub1mark
        self.sub2mark=sub2mark
        self.sub3mark=sub3mark
        self.sub4mark=sub4mark
        self.sub5mark=sub5mark
    def addStudentdetail(self,total,name,rollno,admno,college,parentname,mobilenumber,emailid,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark):
        total=sub1mark+sub2mark+sub3mark+sub3mark+sub4mark+sub5mark
        dict={"total":total,"name":name,"rollno":rollno,"admno":admno,"college":college,"parentname":parentname,"mobilenumber":mobilenumber,"emailid":emailid,"sub1mak":sub1mark,"sub2mark":sub2mark,"sub3mark":sub3mark,"sub4mark":sub4mark,"sub5mark":sub5mark}
        studentlist.append(dict)
    def validation(name,rollno,admno,college,parentname,mobilenumber,emailid,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark):
        validation=re.match(r'([a-zA-Z])\D*([a-zA-Z])$',name)
        validation1=re.match(r'^[1-9]',rollno)
        validation2=re.match(r'^[1-9]',admno)
        validation3=re.match(r'/([A-Z][^\s,.]+[.]?\s[(]?)(University|Institute|College)[^,\d](?=,|\d)/',college)
        validation4=re.match(r'([a-zA-Z])\D*([a-zA-Z])$',parentname)
        validation5=re.match(r"(0|91)?[7-9][0-9]{9}",mobilenumber)
        validation6=re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',emailid)
        validation7=re.match(r'^[0-3]{1}[0-9]{1}|40$',sub1mark)
        validation8=re.match(r'^[0-3]{1}[0-9]{1}|40$',sub2mark)
        validation9=re.match(r'^[0-3]{1}[0-9]{1}|40$',sub3mark)
        validation10=re.match(r'^[0-3]{1}[0-9]{1}|40$',sub4mark)
        validation11=re.match(r'^[0-3]{1}[0-9]{1}|40$',sub5mark)
        if validation:
            return name
        else:
            print("you had enter wrong input")
        
        if validation1:
            return int(rollno)
        else:
            print("you had enter wrong input")
        
        if validation2:
            return int(admno)
        else:
            print("you had enter wrong input")
        
        if validation3:
            return college
        else:
            print("you had enter wrong input")
        if validation4:
            return parentname
        else:
            print("you had enter wrong input")
        if validation5:
            return int(mobilenumber)
        else:
            print("you had enter wrong input")
        if validation6:
            return emailid
        else:
            print("you had enter wrong input")

        if validation7:
            return int(sub1mark)
        else:
            print("you had enter wrong input")

        if validation8:
            return int(sub2mark)
        else:
            print("you had enter wrong input")

        if validation9:
            return int(sub3mark)
        else:
            print("you had enter wrong input")
            
        if validation10:
            return int(sub4mark)
        else:
            print("you had enter wrong input")
        if validation11:
            return int(sub5mark)
        else:
            print("you had enter wrong input")

    obj=Studentdetail()
    while(True):
        print("1. Add Students -")
        print("2. Display student details Like API - ")
        print("3. Search student by Rollno - ")
        print("4. Ranking - ")
        print("5. Exit - ")
        choice=int(input("Enter your choice :"))
        if choice==1:
            name = input("enter the name of student : ")
            rollno=input("enter the Rollno : ")
            admno=input('enter the admin no :  ')
            college=input("enter the college name : ")
            parentname=input("enter the parent name : ")
            mobilenumber=input("enter the mobile number: ")
            emailid=input("enter the email id : ")
            sub1mark=input("enter the subject1 mark: ")
            sub2mark=input("enter the subject2 mark: ")
            sub3mark=input("enter the subject3 mark: ")
            sub4mark=input("enter the subject4 mark: ")
            sub5mark=input("enter the subject5 mark: ")
        obj=Studentdetail(name,rollno,admno,college,parentname,mobilenumber,emailid,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark)
        if choice==2:
            print(studentlist)
            myjson=json.dumps(studentlist)
            with open('json1.json','w',encoding='UTF-8') as f:
                f.write(myjson)
        if choice==3:
            searchroll=int(input("Enter roll number to search :"))
            # print(list(filter(lambda i:i["rollnum"]==searchroll,studentlist)))
            data=(sorted(studentlist,key=lambda i:i["totalmarks"],reverse=True))
            print(data)
            jdata=json.dumps(data)
            with open("json2".json,"w+",encoding="utf-8") as fi:
                fi.write(jdata)        
        if choice==4:
            for i in studentlist:
                if i['totalmarks']<100:
                    message=str(i)
                    print(message)
                    connection=smtplib.SMTP("smtp.gmail.com",587)
                    connection.starttls()
                    connection.login("vaishnavi.p6521@gmail.com","Priy@6521")
                    connection.sendmail("vaishnavi.p6521@gmail.com","vaishnavihajela6520@gmail.com",message)
                    connection.quit
                    print("Mail sent")
            # print(sorted(studentlist,key=lambda i:i["total"],reverse=True))
        if choice==5:
            break
# except Exception:
#     print("Wrong input")
# finally:
#     print("Thank You!")