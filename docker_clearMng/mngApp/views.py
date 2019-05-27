from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Song, SongModelForm
from .forms import SongForm, UploadFileForm
import logging
from io import TextIOWrapper, StringIO
import csv

logger = logging.getLogger('development')

# Create your views here.
def index(request):
    f = UploadFileForm()
    d = {
        'songs': Song.objects.all(),
    }
    return render(request, 'index.html', d)

def new(request):
    f = SongForm()
    return render(request, 'new.html', {'form1': f} )

def deleteAll(request):
    for song in Song.objects.all():
        song.delete()
    return render(request, 'index.html')

def add(request):
    m1 = Song()
    m = SongModelForm(request.POST, instance=m1)
    if m.is_valid():
        print("データを保存します")
        m1 = m.save(commit=False)
        m1.save()
    else:
        print("データを保存しません")
        print(m.errors)
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    song = get_object_or_404(Song, pk=id)
    song.delete()
    return HttpResponseRedirect(reverse('index'))

def upload(request):
    if 'csv' in request.FILES:
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data, delimiter='\t')
        for line in csv_file:
            song, created = Song.objects.get_or_create(name=line[1])

            song.no = line[0]
            song.name = line[1]

            song.bLv = line[2]
            song.eLv = line[4]
            song.mLv = line[6]
            song.hLv = line[8]
            song.cLv = line[10]

            song.bRes = line[3]
            song.eRes = line[5]
            song.mRes = line[7]
            song.hRes = line[9]
            song.cRes = line[11]

            song.save()
        return HttpResponseRedirect(reverse('index'))

    else:
        return render(request, 'upload.html')

def misc(request):
    return render(request, 'misc.html')