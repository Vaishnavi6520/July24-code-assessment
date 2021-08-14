import validate as val
import logging,pymongo,smtplib,time
donor_list=[]
try:
    client=pymongo.MongoClient("mongodb://localhost:27017/") 
    mydatabase=client['BloodbankmgtDb'] 
    collection_name=mydatabase['Blood']
    class BloodBank:
        def donor(self,name,address,blood_group,pincode,mobile_number,emailid,last_donate_date,place):
            self.name=name
            self.address=address
            self.blood_group=blood_group
            self.pincode=pincode
            self.mobile_number=mobile_number
            self.last_donate_date=last_donate_date
            self.place=place
            self.emailid=emailid    
        def adddonordetail(self,name,address,blood_group,pincode,mobile_number,emailid,last_donate_date,place):
            current_time=time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())
            dict1={"name":name,"address":address,"blood_group":blood_group,"pincode":pincode,"mobile_number":mobile_number,"emailid":emailid,"last_donate_date":last_donate_date,"place":place,"AddOn":current_time,"delflag":0} 
            return dict1  

    obj=BloodBank()
    while True:
        print("*@*@*@*@*@*@* BloodBank Management System *@*@*@*@*@*@*")
        print("1.Add Donor ")
        print("2.Search Donors based on blood group ") 
        print("3.Search Donors based on blood group AND place ")
        print("4.Update all the donor details with their mobile number ")
        print("5.Delete the donor using mobile number ")
        print("6.Display the total number of donors on each blood group ")
        print("7.Immediate notification to all via email ")
        print("8.Exit")
        
        choice=int(input("Enter your option : "))
        if choice==1:
            name=input("Enter the DONOR NAME : ") 
            address=input("Enter the DONOR Address : ") 
            blood_group=input("Enter the DONOR Blood group : ") 
            pincode=input("Enter the DONOR Pincode : ")
            mobile_number=input("Enter the DONOR Mobile Number : ")
            emailid= input("Enter your emailid : ")
            last_donate_date=input("Enter the DONOR Last Donate Date : ")
            place=input("Enter the DONOR Place : ")
            data=obj.adddonordetail(val.val_name(name),address,blood_group,val.val_pincode(pincode),val.val_mobilenumber(mobile_number),val.val_emailid(emailid),last_donate_date,place) 
            donor_list.append(data)
            result=collection_name.insert_many(donor_list)
            print(result.inserted_ids)

        if choice==2:
            a = input('enter the blood group')
            result = collection_name.find({"blood_group":a})
            l = []
            for i in result:
                l.append(i)
                print(l) 

        if choice==3:
            blood_group=input("enter the blood_group - ")
            place=input("enter the place - ")
            result=collection_name.find({"$and":[{"blood_group":blood_group},{"place":place}]},{"delflag":0})
            for i in result:
                print(i)  

        if choice==4:
            
            m=input("enter the doner mobile no ")
            print("****@*@*enter the updated details*@*@****")

            name=input("Enter the DONOR updated NAME : ") 
            address=input("Enter the DONOR updated Address : ") 
            blood_group=input("Enter the DONOR updated Blood group : ") 
            pincode=input("Enter the DONOR updated Pincode : ")
            emailid= input("Enter the DONOR updated emailid ")
            last_donate_date=input("Enter the DONOR updated Last Donate Date : ")
            place=input("Enter the DONOR updated place : ")

            
            result=collection_name.update_many({'mobile_number':m},{"$set":{"name":name,"address":address ,"blood_group":blood_group,"pincode":pincode,"emailid":emailid,"last_donate_date":last_donate_date,"place":place}})
            print("data updated")

        if choice==5:
            mobile_number = input('enter mobile number -')
            result=collection_name.update_one({"$and":[{"mobile_number":mobile_number}]},{"$set": {'delflag':1}})

        if choice==6:
            result= collection_name.find({},{"_id":0}) 
            donor_list=[]
            for i in result:
                donor_list.append(i)
            print(donor_list)

        if choice==7:
            result=collection_name.find()
            hospital_name = input("enter the hospital name ")
            connection=smtplib.SMTP("smtp.gmail.com",587)
            connection.starttls()
            connection.login("vaishnavi.p6521@gmail.com","Priy@6521")
            for x in result:
                message="Immediately want A+ blood group in "+ hospital_name +' Hospital . \n THANK YOU!!'
                connection.sendmail("vaishnavi.p6521@gmail.com",x['emailid'], message)
            connection.quit()
            print("Message sended")
                
        if choice==8:
            break 
        if choice==9:
            result=collection_name.find()
            for x in result:
                print(x['mobile_number'])
except:
    logging.error("OOPS!! Something is wrong") 
finally:
    print("Thank you")