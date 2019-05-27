from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Message, MessageModelForm
from .forms import MessageForm


# Create your views here.
def index(request):
    d = {
        'messages': Message.objects.all(),
    }
    return render(request, 'index.html', d)

def new(request):
    f = MessageForm()
    return render(request, 'new.html', {'form1': f} )

def add(request):
    m1 = Message()
    m = MessageModelForm(request.POST, instance=m1)
    if m.is_valid():
        print("データを保存します")
        m1 = m.save(commit=False)
        m1.save()
    else:
        print("データを保存しません")
        print(m.errors)
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    message = get_object_or_404(Message, pk=id)
    message.delete()
    return HttpResponseRedirect(reverse('index'))