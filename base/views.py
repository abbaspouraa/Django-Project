from django.shortcuts import render
from django.http import HttpResponse

rooms = [
    {'id': 1, 'name': "Let\'s learn python"},
    {'id': 2, 'name': "Let\'s learn java"},
    {'id': 3, 'name': "Let\'s learn C++"}
]


def home(request):
    return render(request, 'home.html', {'rooms': rooms})


def room(request):
    return render(request, 'room.html')
