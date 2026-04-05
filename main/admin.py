from django.contrib import admin
from .models import Program, ContactMessage, PartnershipInquiry, VolunteerApplication, Donation, Partner, NewsPost, FAQ, SuccessStory, GalleryItem, TeamMember


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')


@admin.register(PartnershipInquiry)
class PartnershipInquiryAdmin(admin.ModelAdmin):
    list_display = ('organization_name', 'contact_person', 'email', 'partnership_type', 'created_at')
    search_fields = ('organization_name', 'contact_person', 'email', 'partnership_type')


@admin.register(VolunteerApplication)
class VolunteerApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'area_of_interest', 'availability', 'created_at')
    search_fields = ('full_name', 'email', 'phone', 'area_of_interest')
    
@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'amount', 'donation_type', 'created_at')
    search_fields = ('full_name', 'email', 'donation_type')

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    search_fields = ('title', 'category')
    prepopulated_fields = {'slug': ('title',)}
    
@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'created_at')
    search_fields = ('name',)
    
@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_at')
    search_fields = ('question',)
    
@admin.register(SuccessStory)
class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'story_type', 'is_featured', 'created_at')
    search_fields = ('title', 'name', 'story_type')
    list_filter = ('story_type', 'is_featured')
    
@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    
@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'role_title', 'role_group', 'is_featured', 'created_at')
    search_fields = ('full_name', 'role_title', 'role_group')
    list_filter = ('role_group', 'is_featured')