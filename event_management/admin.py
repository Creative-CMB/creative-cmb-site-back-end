from django.contrib import admin
from .models import user
from .models import admin as evtAdmin
from .models import equipment

# Register your models here.
admin.site.register(user)
admin.site.register(evtAdmin)
admin.site.register(equipment)
