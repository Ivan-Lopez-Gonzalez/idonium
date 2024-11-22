from django.contrib import admin
from .models import StatusCandidate, CandidateProfile, JobOffer, HeadHunterUser, Action, Schedule, ManagementCandidates, StatusAction, TypeAction, JobOfferNotification 

# Register your models here.
admin.site.register(HeadHunterUser)
admin.site.register(StatusCandidate)
admin.site.register(CandidateProfile)
admin.site.register(JobOffer)
admin.site.register(Action)
admin.site.register(Schedule)
admin.site.register(ManagementCandidates)
admin.site.register(StatusAction)
admin.site.register(TypeAction)
admin.site.register(JobOfferNotification)