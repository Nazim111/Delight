from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import FeedbackForm


def index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()


    form = FeedbackForm(request.POST or None)
    data = {
        'form': form,
    }
    return render(request, 'main/index.html', data)
