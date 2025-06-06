from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage_view(request):
    # return HttpResponse("<h1>Hello World</h1>")   #string of html code
    return render(request, 'home.html', {})
def contact_view(request):
    # return HttpResponse("<h1>Contact Page</h1>")
    return render(request, 'contact.html', {})
def about_view(request):
    # return HttpResponse("<h1>About Page</h1>")
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list" : [123, 4457, 2445]
    }
    return render(request, 'about.html', my_context)