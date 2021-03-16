from django.shortcuts import render, redirect
from .forms import NewWatch

# Create your views here.


def index(request):
    return render(request, 'index.html')


def create_post(request):
    if request.method =='POST':
        form = NewWatch(request.POST)
        # Validate form fields
        if form.is_valid():
            form.save()
            print("Successfully saved")
            return redirect(index)
       
    form = NewWatch()
    return render(request, 'create_post.html', {
        'form': form
    })
