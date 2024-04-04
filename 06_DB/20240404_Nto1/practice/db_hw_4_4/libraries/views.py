from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, Review
from .forms import BookForm, ReviewForm

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'libraries/index.html', context)

def create(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            return redirect('libraries:index')
    else:
        book_form = BookForm()
    context = {
        'book_form' : book_form,
    }
    return render(request, 'libraries/create.html', context)

def detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    review_form = ReviewForm()
    reviews = Review.objects.all()
    context = {
        'book': book,
        'review_form' : review_form,
        'reviews' : reviews,
    }
    return render(request, 'libraries/detail.html', context)

@login_required
def create_review(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    review_form = ReviewForm(request.POST)
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.user = request.user
        review.book = book
        review.save()
        return redirect('libraries:detail', book_pk)
    context = {
        'book' : book,
        'review' : review,
    }
    return render(request, 'libraries/detail.html', context)

@login_required
def delete_review(request, book_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    if review.user == request.user:
        review.delete()
    return redirect('libraries:detail', book_pk)