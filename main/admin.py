from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Image)
admin.site.register(Review)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(AppUser)
admin.site.register(Checkout)

admin.site.register(HighVoltageInverter)
admin.site.register(LowVoltageInverter)

admin.site.register(HighVoltageBattery)
admin.site.register(LowVoltageBattery)

admin.site.register(Accessories)
admin.site.register(Chargers)
admin.site.register(GridTieInverter)

