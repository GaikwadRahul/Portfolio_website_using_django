from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    
    return render(request, 'home.html')



def projects(request):
    
    return render(request, 'projects.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        ins = Contact(name=name, email=email, message=message)
        ins.save()
        


    return render(request, 'contact.html')

def Photo(request):
    return render(request, 'photos.jpg')