from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .models import Author, Genre, Language, BookInstance, Book
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def index_view(request):

    num_books = Book.objects.all().count()
    num_bookinstance = BookInstance.objects.all().count()
    num_instance_avail = BookInstance.objects.filter(status__exact='a').count()

    context = {
        'num_books': num_books,
        "num_bookinstance": num_bookinstance,
        "num_instance_avail": num_instance_avail
    }

    return render(request, 'catalog/index.html', context=context)


class BookCreate(LoginRequiredMixin, CreateView):  # book_form.html
    model = Book
    fields = "__all__"

    # success_url = reverse_lazy('catalog:book_detail')


class BookDetail(DetailView):
    model = Book


@login_required
def my_view(request):
    return render(request, 'catalog/my_view.html')


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "catalog/signup.html"


class CheckOurBooks(LoginRequiredMixin, ListView):
    model = BookInstance
    template_name = 'catalog/profile.html'
    paginate_by: int = 5

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user)
