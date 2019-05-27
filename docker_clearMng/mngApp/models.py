from django.db import models
from django.forms import ModelForm

class Song(models.Model):
    no = models.CharField(blank=True, max_length=255)
    name = models.CharField('曲名', blank=True, max_length=255)
    
    bLv = models.CharField(blank=True, max_length=255)
    eLv = models.CharField(blank=True, max_length=255)
    mLv = models.CharField(blank=True, max_length=255)
    hLv = models.CharField(blank=True, max_length=255)
    cLv = models.CharField(blank=True, max_length=255)

    bRes = models.CharField(blank=True, max_length=255)
    eRes = models.CharField(blank=True, max_length=255)
    mRes = models.CharField(blank=True, max_length=255)
    hRes = models.CharField(blank=True, max_length=255)
    cRes = models.CharField(blank=True, max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.name)

class SongModelForm(ModelForm):
    class Meta:
        model = Song
        fields = ['name', 'bLv']