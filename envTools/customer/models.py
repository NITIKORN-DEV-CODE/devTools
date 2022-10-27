from django.db import models

class Customer(models.Model):
    custName = models.CharField(max_length=100, default='')
    custPhoneNumber = models.CharField(max_length=11, default='')
    custEmail = models.CharField(max_length=100, default='')
    custPassword = models.CharField(max_length=20, default='')
    createdDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField()
    lastLoginDate = models.DateTimeField()
    stat = models.CharField(max_length=1, default='A')

    def __str__(self):
        return self.custName
class Product(models.Model):
    prodName = models.CharField(max_length=100, default='')
    prodDetail = models.CharField(max_length=250, default='')
    prodPrice = models.IntegerField(default='0')
    createdDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField()
    stat = models.CharField(max_length=1, default='A')

    def __str__(self):
        return self.prodName

class Order(models.Model):
    custID = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)
    orderName = models.CharField(max_length=20, default='')
    orderTotal = models.IntegerField(default='0')
    orderPaid = models.CharField(max_length=1, default='N')
    orderSent = models.CharField(max_length=1, default='N')
    orderRecept = models.CharField(max_length=1, default='N')
    createdDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField()
    stat = models.CharField(max_length=1, default='A')

    def __str__(self):
        return self.orderName

class Address(models.Model):
    orderID = models.ForeignKey(Order, related_name='address', on_delete=models.CASCADE)
    addrNameSent = models.CharField(max_length=150, default='')
    addrDetail1 = models.CharField(max_length=150, default='')
    addrProvinceName = models.CharField(max_length=100, default='')
    addrAmphoeName = models.CharField(max_length=100, default='')
    addrTambolName = models.CharField(max_length=100, default='')
    addrPostCode = models.CharField(max_length=5, default='')
    createdDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField()
    stat = models.CharField(max_length=1, default='A')

    def __str__(self):
        return self.addrNameSent

class OrderProduct(models.Model):
    orderID = models.ForeignKey(Order, related_name='orderproducts', on_delete=models.CASCADE)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE)
    orderProduct = models.CharField(max_length=20, default='')
    productQuantity = models.IntegerField(default='1')
    createdDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField()
    stat = models.CharField(max_length=1, default='A')

    def __str__(self):
        return self.orderProduct

def upload_des(instance, filename):
    return 'ImageSlip/{filename}'.format(filename=filename)

class ImageSlip(models.Model):
    orderId = models.ForeignKey(Order, related_name='imageslip', on_delete=models.CASCADE)
    imgName = models.CharField(max_length=100, default='')
    imgUrl = models.ImageField(upload_to=upload_des, blank=True, null=True)
    createdDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField()
    stat = models.CharField(max_length=1, default='A')

    def __str__(self):
        return self.imgName

def upload_des(instance, filename):
    return 'ImageProduct/{filename}'.format(filename=filename)

class ImageProduct(models.Model):
    prodID = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    imgName = models.CharField(max_length=100, default='')
    imgUrl = models.ImageField(upload_to=upload_des, blank=True, null=True)
    createdDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField()
    stat = models.CharField(max_length=1, default='A')

    def __str__(self):
        return self.imgName
