from django.contrib import admin
from .models import BoxDetails

# Register your models here.
@admin.register(BoxDetails)
class BoxDetailsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BoxDetails._meta.get_fields()]
    

