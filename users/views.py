from django.shortcuts import render

# Django
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.

def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # In case of success, redirect the user to the url which name is 'feed'
            return redirect('feed') 
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    return render(request, 'users/login.html')