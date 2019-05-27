from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloworld(request):
    return HttpResponse("Hello World!")

def send_words(request):
    word_list = ["cat", "dog", "cow"]
    return render(request, 'receive_words.html', {'list': word_list})