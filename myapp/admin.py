from django.contrib import admin
from myapp.models import Bookings, Contact, Register, Manager, Orders

# Register your models here.
admin.site.register(Bookings)
admin.site.register(Contact)
admin.site.register(Register)
admin.site.register(Manager)
admin.site.register(Orders)
