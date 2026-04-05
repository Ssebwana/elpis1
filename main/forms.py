from django import forms
from .models import ContactMessage, PartnershipInquiry, VolunteerApplication, Donation


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message', 'rows': 5}),
        }


class PartnershipInquiryForm(forms.ModelForm):
    class Meta:
        model = PartnershipInquiry
        fields = ['organization_name', 'contact_person', 'email', 'phone', 'partnership_type', 'message']
        widgets = {
            'organization_name': forms.TextInput(attrs={'placeholder': 'Organization Name'}),
            'contact_person': forms.TextInput(attrs={'placeholder': 'Contact Person'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'partnership_type': forms.TextInput(attrs={'placeholder': 'Partnership Type'}),
            'message': forms.Textarea(attrs={'placeholder': 'Tell us about your interest', 'rows': 5}),
        }


class VolunteerApplicationForm(forms.ModelForm):
    class Meta:
        model = VolunteerApplication
        fields = ['full_name', 'email', 'phone', 'area_of_interest', 'availability', 'skills', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'area_of_interest': forms.TextInput(attrs={'placeholder': 'Area of Interest'}),
            'availability': forms.TextInput(attrs={'placeholder': 'Availability e.g. Weekends, Full-time, Part-time'}),
            'skills': forms.Textarea(attrs={'placeholder': 'Tell us about your skills', 'rows': 4}),
            'message': forms.Textarea(attrs={'placeholder': 'Additional Message (Optional)', 'rows': 4}),
        }
        
class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['full_name', 'email', 'phone', 'amount', 'donation_type', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'amount': forms.NumberInput(attrs={'placeholder': 'Amount'}),
            'donation_type': forms.Select(),
            'message': forms.Textarea(attrs={'placeholder': 'Optional Message', 'rows': 4}),
        }