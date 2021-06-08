from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import ProfileForm, SubscriberForm
from .models import Profile, Subscriber

class IndexView(View):
    def get(self, request):
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
