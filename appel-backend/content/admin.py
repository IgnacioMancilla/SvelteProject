from django.contrib import admin
from .models import Slide

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('id','alt','order','is_active','updated')
    list_editable = ('order','is_active')
    search_fields = ('alt','caption')
