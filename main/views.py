from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Program
from .forms import ContactMessageForm, PartnershipInquiryForm, VolunteerApplicationForm, DonationForm
from .models import Program, PartnershipInquiry, VolunteerApplication, Donation, Partner, NewsPost, FAQ, SuccessStory, GalleryItem, TeamMember, AboutPageContent, HeroSection, HeroImage


def index(request):
    programs = Program.objects.all()[:4]
    partners = Partner.objects.all()[:8]
    latest_news = NewsPost.objects.order_by('-created_at')[:3]
    faqs = FAQ.objects.order_by('-created_at')[:6]
    gallery_items = GalleryItem.objects.order_by('-created_at')[:6]
    hero_content = HeroSection.objects.first()
    hero_images = HeroImage.objects.order_by('-created_at')



    total_programs = Program.objects.count()
    total_volunteers = VolunteerApplication.objects.count()
    total_partnerships = PartnershipInquiry.objects.count()
    total_donations = Donation.objects.count()

    context = {
        'programs': programs,
        'partners': partners,
        'latest_news': latest_news,
        'faqs': faqs,
        'hero_section': hero_content,
        'hero_images': hero_images,
        'gallery_items': gallery_items,
        'total_programs': total_programs,
        'total_volunteers': total_volunteers,
        'total_partnerships': total_partnerships,
        'total_donations': total_donations,
    }

    return render(request, 'main/index.html', context)

def about(request):
    team_members = TeamMember.objects.filter(is_featured=True).order_by('role_group', '-created_at')
    about_content = AboutPageContent.objects.first()

    context = {
        'team_members': team_members,
        'about_content': about_content,
    }

    return render(request, 'main/about.html', context)

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
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you. Your donation pledge has been submitted successfully.')
            return redirect('donate')
    else:
        form = DonationForm()

    return render(request, 'main/donate.html', {'form': form})


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


def volunteer(request):
    if request.method == 'POST':
        form = VolunteerApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your volunteer application has been submitted successfully.')
            return redirect('volunteer')
    else:
        form = VolunteerApplicationForm()

    return render(request, 'main/volunteer.html', {'form': form})

def program_detail(request, slug):
    program = get_object_or_404(Program, slug=slug)
    return render(request, 'main/program_detail.html', {'program': program})

def news_list(request):
    news_posts = NewsPost.objects.order_by('-created_at')
    return render(request, 'main/news_list.html', {'news_posts': news_posts})


def news_detail(request, slug):
    news_post = get_object_or_404(NewsPost, slug=slug)
    return render(request, 'main/news_detail.html', {'news_post': news_post})

def stories_list(request):
    stories = SuccessStory.objects.order_by('-created_at')
    return render(request, 'main/stories_list.html', {'stories': stories})


def story_detail(request, pk):
    story = get_object_or_404(SuccessStory, pk=pk)
    return render(request, 'main/story_detail.html', {'story': story})

def gallery(request):
    gallery_items = GalleryItem.objects.order_by('-created_at')
    return render(request, 'main/gallery.html', {'gallery_items': gallery_items})