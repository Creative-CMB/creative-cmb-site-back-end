from django.contrib import admin
from .models import user
from .models import admin as evtAdmin
from .models import emp_details,department,dept_employee,dept_manager,dept_supervisor,salary
from .models import equipment

# Register your models here.
admin.site.register(user)
admin.site.register(evtAdmin)
admin.site.register(emp_details)
admin.site.register(department)
admin.site.register(dept_employee)
admin.site.register(dept_manager)
admin.site.register(dept_supervisor)
admin.site.register(salary)
admin.site.register(equipment)
