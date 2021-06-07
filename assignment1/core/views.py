from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    cards = {
        "Name": "Narathit Panichsombat",
        "Work": "Developer",
        "GitHub": "https://github.com/narathit",
        "Linkedin": "https://www.linkedin.com/in/narathit-panichsombat-4448878/",
    }
    str = ""
    for c in cards:
        str = str + "<b>" + c + ":</b>&nbsp;" + cards[c] + "<br/>"
    return HttpResponse(str)
