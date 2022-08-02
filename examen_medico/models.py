from examen_medico.utils import indice_masa_corporal
import os
from core.utils import ResizeImageMixin
from django.conf import settings
from core.models import AthleteProfile, ProfessorProfile
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


def image_directory_path(instance, filename):

    img_path = 'owner_{0}/{1}'.format(instance.owner.username, filename)
    full_path = os.path.join(settings.MEDIA_ROOT, img_path)
    if os.path.exists(full_path):
        os.remove(full_path)
    return img_path

class ExamImageContent(models.Model, ResizeImageMixin):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exam_image_content_owner', blank=True, null=True)
    file = models.FileField(upload_to= image_directory_path)
    posted = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.resize(self.file, (350, 350))

        super().save(*args, **kwargs)


class IMC(models.Model):
    professor=models.ForeignKey(ProfessorProfile, on_delete=models.CASCADE, blank=True, null=True)
    athlete=models.ForeignKey(AthleteProfile, on_delete=models.CASCADE)
    imc_images = models.ManyToManyField(ExamImageContent, blank=True, related_name='imc_images')
    size=models.DecimalField(decimal_places=2, max_digits=5)
    weight=models.DecimalField(decimal_places=2, max_digits=5)
    result=models.DecimalField(decimal_places=2, max_digits=5, blank=True)
    note=models.TextField(blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.athlete.user.username

    def save(self):
        self.result = indice_masa_corporal(self.size, self.weight)
        super (IMC, self).save()
