from django.contrib import admin
from.models import category
from.models import Supplier
from.models import Product
from.models import Admin
from.models import Customer
from.models import Payment
from.models import feedback
admin.site.register(category)
admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Admin)
admin.site.register(Customer)

admin.site.register(Payment)

admin.site.register(feedback)
