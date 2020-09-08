from django.contrib import admin
from .models import user
from .models import admin as evtAdmin
from .models import invoice
from .models import payment

# Register your models here.
admin.site.register(user)
admin.site.register(evtAdmin)
admin.site.register(invoice)
admin.site.register(payment)
