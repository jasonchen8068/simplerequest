from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def test(request):
    return HttpResponse("hello,tester")

@login_required
def index(request):
    return render_to_response('index.html', {'username': request.user.username})

def login(request):
    if request.method == 'GET':
        return render_to_response('login.html')
    elif request.method == 'POST':
        username = request.POST.get('account')
        password = request.POST.get('password')
        user = auth.authenticate(username = username, password = password)
        if user:
            auth.login(request, user)
            return render_to_response('index.html', {'username': username})
        else:
            return render_to_response('login.html', {'errors': "invalid username or password!"})