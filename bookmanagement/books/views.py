from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Book
from .forms import BookForm

# Create your views here.

def signup(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'books/signup.html', {'form':form})

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books':books})

@login_required
def book_create(request):
    form = BookForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        book = form.save(commit=False)
        book.created_by = request.user
        book.save()
        return redirect('bool_list')
    return render(request, 'books/book_form.html', {'form':form})

@login_required
def book_update(request, id):
    book = get_object_or_404(Book, id=id)
    form = BookForm(request.POST or None, request.FIELS or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'books/book_form.html', {'form':form})

@login_required
def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('bool_list')
        