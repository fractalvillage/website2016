from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from fractalvillage.crud.models import *

class StaffInline(admin.StackedInline):
    model = Staff
    can_delete = False
    verbose_name_plural = 'staff'

class StaffAdmin(BaseUserAdmin):
    inlines = (StaffInline,)

# Register your models here.
admin.site.register(Village)
admin.site.register(VillageDocs)
admin.site.register(Camp)

admin.site.unregister(User)
admin.site.register(User, StaffAdmin)
