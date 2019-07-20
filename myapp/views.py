import logging

from django.contrib.auth import logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from myapp.forms import SignupForm
from myapp.models import Genre, Member

logger = logging.getLogger()


# Create your views here.


def hello_world(request):
    return HttpResponse("Hello World!")


def genres(request):
    if request.user.is_authenticated:
        return
    errors = []
    if request.method == 'POST':
        genre_name = request.POST.get('name')
        if not genre_name:
            errors.append('name is a required field')
        else:
            Genre.objects.create(name=genre_name)
    all_genres = Genre.objects.all()
    return render(request, "genres.html", {
        "genres": all_genres,
        "errors": errors
    })


@login_required
def get_genre(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)

    if request.method == 'POST':
        request_type = request.POST['type']
        if request_type == 'delete':
            genre.delete()
            return HttpResponseRedirect(reverse('genres'))
        if request_type == 'update':
            genre_name = request.POST.get('name')
            genre.name = genre_name
            genre.save()
    return render(request, "genre.html", {
        "genre": genre
    })


def signup(request):
    if request.method == "GET":
        form = SignupForm()

    else:
        form = SignupForm(data=request.POST)

        if form.is_valid():
            form.save()

    return render(request, "signup.html", {
        'form': form
    })


def logout_view(request):
    user = authenticate(username, password)
    try:
    except Exception as e:
        logger.exception(e, exc_info=True)
    if user:
    # Success
    else:
    # Error
    return render(request, 'logout.html')
