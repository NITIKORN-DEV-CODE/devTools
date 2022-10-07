from django.contrib import admin

from province.models import Province
from province.models import Amphoe
from province.models import Tambol
from province.models import Pzone

admin.site.register(Province)
admin.site.register(Amphoe)
admin.site.register(Tambol)
admin.site.register(Pzone)