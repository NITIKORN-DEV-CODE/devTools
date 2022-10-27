from rest_framework import serializers
from province.models import Province, Amphoe, Tambol

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ('id','pCode','pName')

class AmphoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amphoe
        fields = ('id','aCode','aName')

class TambolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tambol
        fields = ('id','tCode','tName','postCode')                
