from django.shortcuts import render, redirect
from .forms import NewWatch
from .models import Watch

# Create your views here.


def index(request):
    return render(request, 'index.html')


def show_post(request):
    watches = Watch.objects.all()
    return render(request, 'show_post.html', {
        'watches': watches
    })


def create_post(request):
    if request.method == 'POST':
        form = NewWatch(request.POST)
        # Validate form fields
        if form.is_valid():
            form.save()
            print("Successfully saved")
            return redirect(index)
        else:
            # store error message
            pass
    form = NewWatch()
    return render(request, 'create_post.html', {
        'form': form
    })
