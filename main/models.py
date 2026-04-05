from django.db import models
from django.utils.text import slugify

class Program(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.TextField()
    full_description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='programs/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class PartnershipInquiry(models.Model):
    organization_name = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    partnership_type = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.organization_name


class VolunteerApplication(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    area_of_interest = models.CharField(max_length=120)
    availability = models.CharField(max_length=120)
    skills = models.TextField()
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    
class Donation(models.Model):
    DONATION_TYPE_CHOICES = [
        ('one-time', 'One-Time Donation'),
        ('monthly', 'Monthly Support'),
        ('campaign', 'Campaign Support'),
    ]

    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    donation_type = models.CharField(max_length=20, choices=DONATION_TYPE_CHOICES, default='one-time')
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.amount}"
    
    
class Partner(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='partners/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class NewsPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    summary = models.TextField()
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

class SuccessStory(models.Model):
    STORY_TYPE_CHOICES = [
        ('beneficiary', 'Beneficiary Story'),
        ('volunteer', 'Volunteer Story'),
        ('partner', 'Partner Story'),
        ('supporter', 'Supporter Story'),
        ('community', 'Community Story'),
    ]

    name = models.CharField(max_length=150)
    title = models.CharField(max_length=200)
    story_type = models.CharField(max_length=30, choices=STORY_TYPE_CHOICES, default='beneficiary')
    short_quote = models.CharField(max_length=255)
    full_story = models.TextField()
    photo = models.ImageField(upload_to='stories/photos/', blank=True, null=True)
    video = models.FileField(upload_to='stories/videos/', blank=True, null=True)
    is_featured = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class GalleryItem(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class TeamMember(models.Model):
    ROLE_GROUP_CHOICES = [
        ('leadership', 'Leadership'),
        ('staff', 'Staff'),
        ('board', 'Board Member'),
        ('volunteer', 'Volunteer Coordinator'),
    ]

    full_name = models.CharField(max_length=150)
    role_title = models.CharField(max_length=150)
    role_group = models.CharField(max_length=30, choices=ROLE_GROUP_CHOICES, default='leadership')
    bio = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='team/', blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    is_featured = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name