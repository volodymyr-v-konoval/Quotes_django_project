from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
from .utils import get_cursor
from .models import Author, Quote
from .forms import AuthorForm, QuoteForm

def main(request, page=1):
    pg_cursor = get_cursor()
    pg_cursor.execute("SELECT * FROM quotes_quote;")
    rows = pg_cursor.fetchall()
    columns = [desc[0] for desc in pg_cursor.description]
    quotes = [dict(zip(columns, row)) for row in rows]
    per_page = 10
    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.get_page(page)
    return render(request, 'quotes/index.html', context={'quotes':quotes_on_page})


def profile(request, id):
    author = get_object_or_404(Author, id=id)
    return render(request, 'quotes/author.html', context={'author':author})


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AuthorForm()

    return render(request, 'quotes/add_author.html', {'form': form})


def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = QuoteForm()

    return render(request, 'quotes/add_quote.html', {'form': form})
