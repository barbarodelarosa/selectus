from core.models import AthleteProfile, ExecutiveProfile, Group, ProfessorProfile, Profile, User
from django.contrib import admin

admin.site.register(Group)
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(AthleteProfile)
admin.site.register(ProfessorProfile)
admin.site.register(ExecutiveProfile)

# Register your models here.
