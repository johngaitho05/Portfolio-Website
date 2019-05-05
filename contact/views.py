from django.shortcuts import render
from .models import Message

def contactpage(request):
    return render(request,'contact/home.html')


def savemessage(request):
    name= request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    page = request.POST['page']
    if name !="" and email !="" and message != "":
        new_message= Message(name=name, email=email,message=message)
        new_message.save()
        if page == "home":
            return render(request, 'home.html')

        else:
            return render(request, 'contact/home.html')

    else:
        return render(request, 'home.html')














