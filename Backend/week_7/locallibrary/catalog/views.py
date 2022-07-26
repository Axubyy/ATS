from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required


# Create your views here.


# class HomeView(TemplateView):
#     template_name = "catalog/index.html"

from .models import Book, Author, BookInstance, Genre


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    book = Book.objects.all()
    num_books = book.count()
    num_instances = BookInstance.objects.all().count()
    num_genres = Genre.objects.count()
    # num_book_words = book.filter('i')
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_visits': num_visits,

        # 'num_book_word': num_book_words
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(ListView):
    model = Book
    paginate_by = 2


class BookDetailView(DetailView):
    model = Book


class AuthorDetailView(DetailView):
    model = Author


class AuthorListView(ListView):
    model = Author


class LoanedBooksByUserListView(LoginRequiredMixin, ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
