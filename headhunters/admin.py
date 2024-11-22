from django.contrib import admin

from profile_cv.models import Profile_CV
from .models import StatusCandidate, JobOffer, HeadHunterUser, Action, Schedule, ManagementCandidates, StatusAction, TypeAction, JobOfferNotification 

# Register your models here.
admin.site.register(HeadHunterUser)
admin.site.register(StatusCandidate)
admin.site.register(Profile_CV)
admin.site.register(JobOffer)
admin.site.register(Action)
admin.site.register(Schedule)
admin.site.register(ManagementCandidates)
admin.site.register(StatusAction)
admin.site.register(TypeAction)
admin.site.register(JobOfferNotification)