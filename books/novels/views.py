from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Novels

# Create your views here.
def novelsList(request):
    # template = loader.get_template('novelsList.html')
    # return HttpResponse(template.render())
    novel = Novels.objects.all();
    context={
        'novel': novel
    }
    return render(request, 'novelsList.html',context)

def add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        author = request.POST.get('author')

        bookNovel = Novels(
            nName = name,
            nAuthor = author
        )
        bookNovel.save()
        return redirect('home')
    return render(request, 'novelsList.html')

def edit(request):
    novel = Novels.objects.all();
    context={
        'novel': novel
    }
    return redirect(request,'novelsList.html',context)    

def update(request,id):
    if request.method == "POST":
        name = request.POST.get('name')
        author = request.POST.get('author')

        bookNovel = Novels(
            id = id,
            nName = name,
            nAuthor = author
        )
        bookNovel.save()
        return redirect('home') 
    return render(request, 'novelsList.html')

    
def delete(request,id):
    bookNovel = Novels.objects.filter(id = id)
    bookNovel.delete()
    return redirect('home')