from django.contrib import admin
from customers.models import CustomerProfile

#
# class CustomerProfile(admin.ModelAdmin):
#     pass
#

admin.site.register(CustomerProfile)
