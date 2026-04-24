from typing import Any, List, Tuple
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from . models import *


#create own age filter
class AgeFiletr(admin.SimpleListFilter):
    title = "Age Filter"
    parameter_name = "age"


    def lookups(self, request, model_admin):
        return [
            ('below_30', 'Below 30'),
            ('30_to_50', '30 to 50'),
            ('above_50', 'Above 50'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'below_30':
            return queryset.filter(age__lt=30)
        if self.value() == '30_to_50':
            return queryset.filter(age__gte=30, age__lte=50)
        if self.value() == 'above_50':
            return queryset.filter(age__gt=50)
        return queryset
    
#admin action for making the record active or inactive
@admin.action(description="Mark as Inactive")
def mark_inactive(modeladmin, request, queryset):
    queryset.update(is_active=False)

@admin.action(description="Mark as Active")
def mark_active(modeladmin, request, queryset):
    queryset.update(is_active=True)

# Register your models here.
@admin.register(Application)
# admin.site.register(Application) another method for model registration
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ["applicant_name", "add_code", "phone_no", "age", "email", "is_active"]
    empty_value_display = "None"
    list_display_links = ["applicant_name", "add_code", "phone_no", "email"] #to make all the fields clickable
    list_filter = ["is_active",AgeFiletr]
    list_per_page = 10 #data per page
    ordering = ["age"] #order by
    search_fields = ["applicant_name"]
    #register actions to mark as active and inactive
    actions = [mark_inactive, mark_active]
    #to show only some fields
    # fields = ["applicant_name", "phone_no", "age", "email"]

    #fieldsets to show the fields headingwise
    fieldsets = (
        (
            "Personal Information", {"fields": ["applicant_name", "phone_no", "age"]}
        ),
        (
            "Other Info", {"fields": ["email", "is_active"],
                           "classes": ["collapse"]} #to show or hide the section
        )
    )
    #this can be added as field in list display
    @admin.display()
    def add_code(self, obj):
        return ("+977"+ obj.phone_no)
    
