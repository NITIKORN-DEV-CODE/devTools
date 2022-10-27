from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import HttpResponse

from customer.models import Customer, Order, Address, OrderProduct, ImageSlip,Product
from customer.serializers import CustomerSerializer,OrderSerializer, AddressSerializer, OrderProductSerializer, ImageSlipSerializer,ProductSerializer, CustomerProfileSerializer

@csrf_exempt
def customerApi_customer(request,pk=0):
    if request.method == 'GET':

        if pk!=0 :
            customer = Customer.objects.filter(id=pk,stat='A')
        else:
            customer = Customer.objects.filter(stat='A')

        serializer = CustomerSerializer(customer, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        customer_data = JSONParser().parse(request)
        isExist = 0
        isExist = Customer.objects.filter(custPhoneNumber=customer_data['custPhoneNumber'],stat='A').count()
        if(isExist>0):
            return JsonResponse("Dupplicat Phone number", safe=False)
        serializer = CustomerProfileSerializer(data=customer_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.data, self=False)
@csrf_exempt
def customerApi_profile(request,pk=0):
    if request.method == 'POST':
        profile_data = JSONParser().parse(request)
        profile = Customer.objects.filter(custPhoneNumber=profile_data['custPhoneNumber'],custPassword=profile_data['custPassword'])

        serializer = CustomerProfileSerializer(profile, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        profile_data = JSONParser().parse(request)
        profile_get = Customer.objects.get(id=profile_data['id'])
        serializer = CustomerProfileSerializer(profile_get, data=profile_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def orderApi_order(request,pk=0):
    if request.method == 'GET':
        if pk!=0 :
            order = Order.objects.filter(id=pk,stat='A')
        else:
            order = Order.objects.filter(stat='A')

        serializer = OrderSerializer(order, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        order = Order()
        customer = Customer.objects.get(id=request.POST.get('custID'))
        order.custID = customer
        order.orderName = request.POST.get('orderName')
        order.orderTotal = request.POST.get('orderTotal')
        order.updateDate = request.POST.get('updateDate')
        order.save()

        serializer = OrderSerializer(order)
        return JsonResponse(serializer.data, safe=False)
@csrf_exempt
def orderApi_orderproduct(request,pk=0):
    if request.method == 'POST':
        orderproduct = OrderProduct()
        order = Order.objects.get(id=request.POST.get('orderID'))
        product = Product.objects.get(id=request.POST.get('productID'))

        orderproduct.orderID = order
        orderproduct.productID = product
        orderproduct.orderProduct = request.POST.get('orderProduct')
        orderproduct.productQuantity = request.POST.get('productQuantity')
        orderproduct.updateDate = request.POST.get('updateDate')
        orderproduct.save()

        serializer = OrderProductSerializer(orderproduct)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def productApi_product(request,pk=0):
    if request.method == 'GET':

        if pk!=0 :
            product = Product.objects.filter(id=pk,stat='A')
        else:
            product = Product.objects.filter(stat='A')

        serializer = ProductSerializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def productApi_imageslip(request,pk=0):
    if request.method == 'GET':
        if pk!=0 :
            image = ImageSlip.objects.filter(id=pk,stat='A')
        else:
            image = ImageSlip.objects.filter(stat='A')

        serializer = ImageSlipSerializer(image, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        imageslip = ImageSlip()
        order = Order.objects.get(id=request.POST.get('orderId'))
        imageslip.orderId = order
        imageslip.imgName = request.POST.get('imgName')
        imageslip.imgUrl = request.FILES['imgUrl']
        imageslip.updateDate = request.POST.get('updateDate')
        imageslip.save()

        serializer = ImageSlipSerializer(imageslip)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def productApi_address(request,pk=0):
    if request.method == 'GET':
        if pk!=0 :
            address = Address.objects.filter(id=pk,stat='A')
        else:
            address = Address.objects.filter(stat='A')

        serializer = AddressSerializer(address, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        address = Address()
        order = Order.objects.get(id=request.POST.get('orderID'))
        address.orderID = order
        address.addrNameSent = request.POST.get('addrNameSent')
        address.addrDetail1 = request.POST.get('addrDetail1')
        address.addrProvinceName = request.POST.get('addrProvinceName')
        address.addrAmphoeName = request.POST.get('addrAmphoeName')
        address.addrTambolName = request.POST.get('addrTambolName')
        address.addrPostCode = request.POST.get('addrPostCode')
        address.updateDate = request.POST.get('updateDate')
        address.save()

        serializer = AddressSerializer(address)
        return JsonResponse(serializer.data, safe=False)
