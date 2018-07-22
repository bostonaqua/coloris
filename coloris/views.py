from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Note

def index(request):
    notes_list = Note.objects.order_by('-uniq_count')[0:]
    context = {'notes_list': notes_list}
    return render(request, 'coloris/notes.html', context)

def add_note(request):
    n = Note()
    if request.POST['text']:
        n.text_field = request.POST['text']
        list_of_words = n.text_field.split()
        clean_words = map(lambda x: x.strip('.,!@#$%^&*()-_=+\'"{}[]\\?|'), list_of_words)
        n.uniq_count = len(set(clean_words))
        n.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def delete_entrys(request):
    print(request)
    Note.objects.all().delete()
    return HttpResponseRedirect('/')