from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from doctors.serializer import DoctorsSerializer
from django.http.response import JsonResponse
from django.http.response import HttpResponse
from doctors.models import Doctorsapp


def register(request):
    return render(request,'register.htm')

def login(request):
    return render(request,'login.html')

@csrf_exempt
def doctor(request):
    if(request.method=="POST"):
        doctordata=JSONParser().parse(request)
        Doctors_Serializer=DoctorsSerializer(data=doctordata)
        if(Doctors_Serializer.is_valid()):
            Doctors_Serializer.save()
            return JsonResponse(Doctors_Serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in seialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("Error",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def doctors_list(request):
    if(request.method=="GET"):
        doctors=Doctorsapp.objects.all()
        Doctors_Serializer=DoctorsSerializer(doctors, many=True)
        return JsonResponse(Doctors_Serializer.data, safe=False)

@csrf_exempt
def doctorcode(request,fetchid):
    doctors=Doctorsapp.objects.get(doctor_code=fetchid)
    if(request.method=="GET"):
        Doctors_Serializer=DoctorsSerializer(doctors)
        return JsonResponse(Doctors_Serializer.data,safe=False, status=status.HTTP_200_OK)
    else:
        return HttpResponse("Invalid doctor code")

@csrf_exempt
def doctordetail(request,id):
    try:
        doctors=Doctorsapp.objects.get(id=id)
        if(request.method=="GET"):
            Doctors_Serializer=DoctorsSerializer(doctors)
            return JsonResponse(Doctors_Serializer.data,safe=False, status=status.HTTP_200_OK)

        if(request.method=="DELETE"):
            doctors.delete()
            return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)

        if(request.method=="PUT"):
            doctorsdata=JSONParser().parse(request)
            Doctors_Serializer=DoctorsSerializer(doctors,data=doctorsdata)
            if(Doctors_Serializer.is_valid()):
                Doctors_Serializer.save()
                return JsonResponse(Doctors_Serializer.data,status=status.HTTP_200_OK)
            else:
                return HttpResponse("Error in seialization")
    except Doctorsapp.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
