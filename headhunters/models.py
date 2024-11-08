

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Model for HeadHunter (using custom authentication)
class HeadHunter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='headhunter')
    company = models.CharField(max_length=255)
    permissions = models.JSONField(default=dict)  # Stores specific permissions for the HeadHunter
    
    def __str__(self):
        return f"{self.user.username} - {self.company}"


# Model for Search Filter
class SearchFilter(models.Model):
    headhunter = models.ForeignKey(HeadHunter, on_delete=models.CASCADE)
    skills = models.JSONField()  # Skills to filter by
    experience = models.CharField(max_length=100)
    language_level = models.CharField(max_length=50)
    sector = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    availability = models.CharField(max_length=100)
    vehicle = models.BooleanField(default=False)
    disability = models.BooleanField(default=False)
    search_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Search by {self.headhunter.user.username} - {self.search_date}"

# Model for Job Offer
class JobOffer(models.Model):
    headhunter = models.ForeignKey(HeadHunter, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('open', 'Open'), ('closed', 'Closed')])
    
    def __str__(self):
        return self.title

# Model for Action Agenda
class ActionAgenda(models.Model):
    headhunter = models.ForeignKey(HeadHunter, on_delete=models.CASCADE)
    date = models.DateTimeField()
    task = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('completed', 'Completed')])
    comments = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"Agenda of {self.headhunter.user.username} - {self.task} - {self.date}"

# Model for Candidate Actions
class CandidateActions(models.Model):
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    result = models.CharField(max_length=255)
    date = models.DateTimeField()
    
    def __str__(self):
        return f"Action {self.action} for {self.candidate.name} - {self.date}"

# Model for Job Offer Notification
class JobOfferNotification(models.Model):
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE)
    job_offer = models.ForeignKey(JobOffer, on_delete=models.CASCADE)
    sent_date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Notification for {self.job_offer.title} to {self.candidate.name}"

# Model for Saved Search
class SavedSearch(models.Model):
    headhunter = models.ForeignKey(HeadHunter, on_delete=models.CASCADE)
    filter = models.ForeignKey(SearchFilter, on_delete=models.CASCADE)
    saved_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Saved search by {self.headhunter.user.username} - {self.saved_date}"

# Model for Virtual Assistant Follow-up
class VirtualAssistant(models.Model):
    headhunter = models.ForeignKey(HeadHunter, on_delete=models.CASCADE)
    task = models.CharField(max_length=255)
    scheduled_date = models.DateTimeField()
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('completed', 'Completed')])
    
    def __str__(self):
        return f"Assistant of {self.headhunter.user.username} - {self.task}"

