from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

from random_username.generate import generate_username

class User(AbstractUser):
    is_executive = models.BooleanField(default=False)
    is_professor = models.BooleanField(default=False)
    is_athlete = models.BooleanField(default=False)

    def get_executive_profile(self):
        aexecutive_profile = None
        if hasattr(self, 'executiveprofile'):
            aexecutive_profile = self.executiveprofile
        return aexecutive_profile

    def get_athlete_profile(self):
        athlete_profile = None
        if hasattr(self, 'athleteprofile'):
            athlete_profile = self.athleteprofile
        return athlete_profile

    def get_professor_profile(self):
        professor_profile = None
        if hasattr(self, 'professorprofile'):
            professor_profile = self.professorprofile
        return professor_profile



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()
    active=models.BooleanField(default=True)
    aprovate=models.BooleanField(default=True)


    def __str__(self):
        return self.user.username


class AthleteProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_athlete_images')
    bio = models.TextField(blank=True)
    active=models.BooleanField(default=True)
    aprovate=models.BooleanField(default=True)

    def save(self, *args, **kwargs):       
        self.user.is_athlete = True
        self.user.save()
        super(AthleteProfile,self).save(*args, **kwargs)
        
    def __str__(self):
        return self.user.username

class ProfessorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_professor_images')
    bio = models.TextField(blank=True)
    active=models.BooleanField(default=False)
    aprovate=models.BooleanField(default=False)

    def save(self, *args, **kwargs):       
        self.user.is_professor = True
        self.user.save()
        super(ProfessorProfile,self).save(*args, **kwargs)
        
    def __str__(self):
        return self.user.username

class ExecutiveProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_executive_images')
    bio = models.TextField(blank=True)
    active=models.BooleanField(default=False)
    aprovate=models.BooleanField(default=False)

    def save(self, *args, **kwargs):       
        self.user.is_executive = True
        self.user.save()
        super(ExecutiveProfile,self).save(*args, **kwargs)
        
    def __str__(self):
        return self.user.username


class Group(models.Model):
    professors=models.ManyToManyField(ProfessorProfile, related_name='professors')
    profesor_active=models.ForeignKey(ProfessorProfile, on_delete=models.PROTECT, related_name='professor_active')
    athletes=models.ManyToManyField(AthleteProfile)
    image=models.ImageField(upload_to='groups', blank=True, null=True)
    name=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name