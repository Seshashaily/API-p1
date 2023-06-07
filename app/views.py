from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from app.models import *
from rest_framework.response import Response
from app.serializers import *
from rest_framework.status import HTTP_200_OK

@api_view()
def employee(request):
    EMS=Employee.objects.all()
    ESD=EmployeeMS(EMS,many=True)
    return Response(ESD.data,status=HTTP_200_OK)

