from django import forms
from .models import HeadHunter, CandidateProfile, JobOffer, ManagementCandidates, Schedule, JobOfferNotification

class HeadHunterForm(forms.ModelForm):
    class Meta:
        model = HeadHunter
        fields = '__all__'

class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        fields = '__all__'

class JobOfferForm(forms.ModelForm):
    class Meta:
        model = JobOffer
        fields = '__all__'

class ManagementCandidatesForm(forms.ModelForm):
    class Meta:
        model = ManagementCandidates
        fields = '__all__'

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'


class JobOfferNotificationForm(forms.ModelForm):
    class Meta:
        model = JobOfferNotification
        fields = '__all__'
