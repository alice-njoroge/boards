from django.shortcuts import render

from .models import Board


def home(request):
    boards = Board.objects.all()
    return render(request, 'boards_app/home.html', {'boards': boards})
