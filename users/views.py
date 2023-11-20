from django.shortcuts import render, redirect
from .models import Book
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    book = Book.objects.all()
    if request.method == 'POST':
        # title = request.POST['title']
        # document = request.FILES['document']
        title = request.POST.get('title', '') 
        document = request.FILES.get('document')

        if document:
            fs = FileSystemStorage()
            fs.save(document.name, document)


        new_book = Book.objects.create(title=title, document=document)
        new_book.save()
            
        return redirect('/')


    return render(request, 'index.html', {'books': book})

def delete(request, pk):
    bk = Book.objects.get(id = pk)
    bk.delete()
    return redirect('/')
