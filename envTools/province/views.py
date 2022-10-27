from django.shortcuts import render
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from province.models import Province, Amphoe, Tambol
from province.serializers import ProvinceSerializer, AmphoeSerializer, TambolSerializer

@csrf_exempt
def provinceApi_province(request,pk=0):
    if request.method == 'GET':
        if pk!=0 :
            province = Province.objects.filter(pCode=pk)
        else:
            province = Province.objects.all()

        serializer = ProvinceSerializer(province, many=True)
        return JsonResponse(serializer.data, safe=False)

def provinceApi_amphoeprovince(request,pk=0):
    if request.method == 'GET':
        if pk!=0 :
            amphoe = Amphoe.objects.filter(pCode=pk)
        else:
            amphoe = Amphoe.objects.all()

        serializer = AmphoeSerializer(amphoe, many=True)
        return JsonResponse(serializer.data, safe=False)

def provinceApi_tambolamphoe(request,pk=0):
    if request.method == 'GET':
        if pk!=0 :
            tambol = Tambol.objects.filter(aCode=pk)
        else:
            tambol = Tambol.objects.all()

        serializer = TambolSerializer(tambol, many=True)
        return JsonResponse(serializer.data, safe=False)

def provinceApi_amphoe(request,pk=0):
    if request.method == 'GET':
        if pk!=0 :
            amphoe = Amphoe.objects.filter(aCode=pk)
        else:
            amphoe = Amphoe.objects.all()

        serializer = AmphoeSerializer(amphoe, many=True)
        return JsonResponse(serializer.data, safe=False)

def provinceApi_tambol(request,pk=0):
    if request.method == 'GET':
        if pk!=0 :
            tambol = Tambol.objects.filter(tCode=pk)
        else:
            tambol = Tambol.objects.all()

        serializer = TambolSerializer(tambol, many=True)
        return JsonResponse(serializer.data, safe=False)
