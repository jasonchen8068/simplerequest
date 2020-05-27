from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.
def test(request):
    return HttpResponse("hello,tester")

def login(request):
    if request.method == 'GET':
        return render_to_response('login.html')
    elif request.method == 'POST':
        return HttpResponse("hello,tester")