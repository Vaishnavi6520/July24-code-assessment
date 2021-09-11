import json,requests
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from donors.serializer import DonorSerializer
from django.http.response import JsonResponse
from django.http.response import HttpResponse
from donors.models import Donorapp1


def register(request):
    return render(request,'register.html')

def login(request):
    return render(request, 'login.html')

def search(request):
    return render(request,"search.html")

def update(request):
    return render(request,"update.html")

def viewdonor(request):
    fetchdata=requests.get("http://127.0.0.1:8000/donors/viewdonars/").json()
    return render(request,"view.html",{"data":fetchdata})

@csrf_exempt
def donor(request):
    if(request.method=="POST"):
        mydata=JSONParser().parse(request)
        Donor_Serializer= DonorSerializer(data=mydata)
        if(Donor_Serializer.is_valid()):
            Donor_Serializer.save()
            
            return JsonResponse(Donor_Serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("No get method",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def login_check(request):
    try:
        getUsername=request.POST.get("username")
        getpassword =request.POST.get("password")

        getUsers =Donorapp1.objects.filter(username=getUsername, password = getpassword)
        donor_serializer = DonorSerializer(getUsers, many=True)
        print(donor_serializer.data)
        if (donor_serializer.data):
            for i in donor_serializer.data:
                getID = i["id"]
                getName = i["name"]
                getUsername =i["username"]
            #session
            request.session['uid']=getID
            request.session['uname'] =getName
            return render(request,"view.html")
        else:
            return HttpResponse("Invalid")

    except Donorapp1.DoesNotExist:
        return HttpResponse("Invalid username or password", status=status.HTTP_404_NOT_FOUND)

    except:
        return HttpResponse("Something went wrong")



@csrf_exempt
def donor_list(request):
    if(request.method == "GET"):
        donors = Donorapp1.objects.all()
        Donor_Serializer= DonorSerializer(donors, many=True)
        return JsonResponse(Donor_Serializer.data, safe=False)


@csrf_exempt
def donordetail(request,id):
    try:
        donors=Donorapp1.objects.get(bloodgroup=id)
        if(request.method == "GET"):
            Donor_Serializer=DonorSerializer(donors)
            return JsonResponse(Donor_Serializer.data, safe=False, status=status.HTTP_200_OK)

        if(request.method=="DELETE"):
            donors.delete()
            return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)

        if(request.method == "PUT"):
            mydata=JSONParser().parse(request)
            Donor_Serializer = DonorSerializer(donors,data=mydata)
            if(Donor_Serializer.is_valid()):
                Donor_Serializer.save()
                return JsonResponse(Donor_Serializer.data,status=status.HTTP_200_OK)

            else:
                return HttpResponse("Error in serialization")

    except Donorapp1.DoesNotExist:
        return HttpResponse("Invalid donor bloodgroup",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def updatesearchapi(request):
    try:
        getusername=request.POST.get("id")
        getStudent=Donorapp1.objects.filter(username=getusername)
        Donor_Serializer=DonorSerializer(getStudent,many=True)
        return render(request,"update.html",{"data":Donor_Serializer.data})
        
    except Donorapp1.DoesNotExist:
        return HttpResponse("Invalid data",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("invalid")

@csrf_exempt
def update_data_read(request):

    getid=request.POST.get("newid")
    getname=request.POST.get("newname")
    getaddress=request.POST.get("newaddress")
    getbloodgroup=request.POST.get("newbloodgroup")
    getmob=request.POST.get("newmob")
    getusername=request.POST.get("newusername")
    getpassword=request.POST.get("newpassword")
    mydata={'name':getname,'id':getid,'address':getaddress,'name':getname,'bloodgroup':getbloodgroup,'mob_num':getmob,'username':getusername,'password':getpassword}
    jsondata=json.dumps(mydata)
    print(jsondata)
    Apilink="http://localhost:8000/donor/viewdonor/"+getid
    requests.put(Apilink,data=jsondata)
    return redirect(donor_list)

    