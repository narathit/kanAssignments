from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import ProfileForm, SubscriberForm
from .models import Profile, Subscriber

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

class IndexView(View):
    def get(self, request):
        name = "Narathit Panichsombat"
        work = "Developer"
        github = "https://github.com/narathit"
        linkedin = "https://www.linkedin.com/in/narathit-panichsombat-4448878/"
        return render(
            request,
            "index.html",
            {
                "name": name,
                "work": work,
                "github": github,
                "linkedin": linkedin,
            },
        )

    def post(self, request):
        print(request.POST)
        form = ProfileForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print(form.cleaned_data)
            print("name:" + form.cleaned_data.get("name"))
            print("email:" + form.cleaned_data.get("email"))
            print("work:" + form.cleaned_data.get("work"))
            print("github:" + form.cleaned_data.get("github"))
        profile = Profile.objects.create(
            name = form.cleaned_data.get("name"),
            email = form.cleaned_data.get("email"),
            work = form.cleaned_data.get("work"),
            github = form.cleaned_data.get("github"),
        )
        print(profile)
        return render(
            request,
            "index.html",
            {
                "name": profile.name,
                "email": profile.email,
                "work": profile.work,
                "github": profile.github,
            },
        )

class SubscriberView(View):
    def get(self, request):
        print(request.POST.get("email"))
        if request.POST.get("email"):
            message = request.POST.get("email") + " is successfully subscribed."
        else:
            message = ""
        return render(
            request,
            "subscriber.html",
            {
                "message": message,
            },
        )

    def post(self, request):
        print(request.POST)
        form = SubscriberForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print(form.cleaned_data)
            print("email:" + form.cleaned_data.get("email"))
        subscriber = Subscriber.objects.create(
            email = form.cleaned_data.get("email"),
        )
        return render(
            request,
            "subscriber.html",
            {
                "message": subscriber.email + " is successfully subscribed.",
            },
        )
