from django.contrib import admin

import App_Payment

from App_Payment.models import BillingAddress

# Register your models here.
admin.site.register(BillingAddress)
