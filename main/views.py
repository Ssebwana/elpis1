from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Program
from .forms import ContactMessageForm, PartnershipInquiryForm


def home(request):
    programs = Program.objects.all()[:4]
    return render(request, 'main/home.html', {'programs': programs})


def about(request):
    return render(request, 'main/about.html')


def programs(request):
    all_programs = Program.objects.all()
    return render(request, 'main/programs.html', {'programs': all_programs})


def partnerships(request):
    if request.method == 'POST':
        form = PartnershipInquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your partnership inquiry has been submitted successfully.')
            return redirect('partnerships')
    else:
        form = PartnershipInquiryForm()

    return render(request, 'main/partnerships.html', {'form': form})


def donate(request):
    return render(request, 'main/donate.html')


def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully.')
            return redirect('contact')
    else:
        form = ContactMessageForm()

    return render(request, 'main/contact.html', {'form': form})