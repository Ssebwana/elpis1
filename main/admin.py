from django.contrib import admin

# Register your models here.
from .models import Program, ContactMessage, PartnershipInquiry


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    search_fields = ('title', 'category')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')


@admin.register(PartnershipInquiry)
class PartnershipInquiryAdmin(admin.ModelAdmin):
    list_display = ('organization_name', 'contact_person', 'email', 'partnership_type', 'created_at')
    search_fields = ('organization_name', 'contact_person', 'email', 'partnership_type')