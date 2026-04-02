from django import forms
from .models import ContactMessage, PartnershipInquiry


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