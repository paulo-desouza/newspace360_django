from django.contrib import admin
from basic_user.models import BasicUser



class UserAdmin(admin.ModelAdmin):
    
    fields = ["email", "password", "is_active", "is_staff", "is_superuser"]
    
    
admin.site.register(BasicUser, UserAdmin)

