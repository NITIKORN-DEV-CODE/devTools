from rest_framework import serializers
from customer.models import Customer, Order, Address, OrderProduct, ImageSlip, Product, ImageProduct

class ImageProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageProduct
        fields = ('id','imgName','imgUrl','prodID','createdDate','updateDate','stat')

class ProductSerializer(serializers.ModelSerializer):
    images = ImageProductSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'prodName', 'prodDetail', 'prodPrice','images', 'createdDate', 'updateDate','stat')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'orderID', 'addrNameSent', 'addrDetail1','addrProvinceName','addrAmphoeName','addrTambolName','addrPostCode', 'createdDate', 'updateDate','stat')

class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ('id', 'orderID', 'productID', 'productQuantity', 'createdDate', 'updateDate','stat')

class ImageSlipSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageSlip
        fields = ('id', 'orderId', 'imgName', 'imgUrl', 'createdDate', 'updateDate','stat')

class OrderSerializer(serializers.ModelSerializer):
    orderproducts = OrderProductSerializer(many=True)
    address = AddressSerializer(many=True)
    imageslip =  ImageSlipSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'custID', 'orderTotal', 'orderproducts', 'address','imageslip', 'orderPaid','orderSent','orderRecept', 'createdDate', 'updateDate','stat')

class CustomerSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True)

    class Meta:
        model = Customer
        fields = ('id', 'custName', 'custPhoneNumber', 'custEmail','orders','custPassword', 'createdDate', 'updateDate','lastLoginDate','stat')

class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'custName', 'custPhoneNumber', 'custEmail','custPassword', 'createdDate', 'updateDate','lastLoginDate','stat')
