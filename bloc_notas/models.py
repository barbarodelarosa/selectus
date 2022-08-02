import os
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from core.utils import ResizeImageMixin


User = get_user_model()


def image_directory_path(instance, filename):

    img_path = 'owner_{0}/note_bloc_{1}'.format(instance.owner.username, filename)
    full_path = os.path.join(settings.MEDIA_ROOT, img_path)
    if os.path.exists(full_path):
        os.remove(full_path)
    return img_path

class NoteImageContent(models.Model, ResizeImageMixin):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='note_bloc_content_owner', blank=True, null=True)
    file = models.FileField(upload_to= image_directory_path)
    posted = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.resize(self.file, (350, 350))

        super().save(*args, **kwargs)

class NoteBloc(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    note=models.TextField()
    images=models.ManyToManyField(NoteImageContent, related_name='note_bloc_images', blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

