from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from patients.serializer import PatientsSerializer
from django.http.response import JsonResponse
from django.http.response import HttpResponse
from patients.models import Patientsapp

def addpatient(request):
    return render(request,'patient.htm')

@csrf_exempt
def patient(request):
    if(request.method=="POST"):
        patientdata=JSONParser().parse(request)
        Patients_Serializer=PatientsSerializer(data=patientdata)
        if(Patients_Serializer.is_valid()):
            Patients_Serializer.save()
            return JsonResponse(Patients_Serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in seialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("Error",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def patient_list(request):
    if(request.method=="GET"):
        patients=Patientsapp.objects.all()
        Patients_Serializer=PatientsSerializer(patients, many=True)
        return JsonResponse(Patients_Serializer.data, safe=False)

@csrf_exempt
def patientcode(request,patient_code):
    patients=Patientsapp.objects.get(patient_code=patient_code)
    if(request.method=="GET"):
        Patients_Serializer=PatientsSerializer(patients)
        return JsonResponse(Patients_Serializer.data,safe=False, status=status.HTTP_200_OK)
    else:
        return HttpResponse("Invalid patient code")



@csrf_exempt
def patientdetail(request,id):
    try:
        patients=Patientsapp.objects.get(id=id)
        if(request.method=="GET"):
            Patients_Serializer=PatientsSerializer(patients)
            return JsonResponse(Patients_Serializer.data,safe=False, status=status.HTTP_200_OK)

        if(request.method=="DELETE"):
            patients.delete()
            return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)

        if(request.method=="PUT"):
            patientsdata=JSONParser().parse(request)
            Patients_Serializer=PatientsSerializer(patients,data=patientsdata)
            if(Patients_Serializer.is_valid()):
                Patients_Serializer.save()
                return JsonResponse(Patients_Serializer.data,status=status.HTTP_200_OK)
            else:
                return HttpResponse("Error in seialization")
    except Patientsapp.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
