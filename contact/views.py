from django.shortcuts import render,redirect
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
            return redirect('homepage')

        else:
            return redirect('contactpage')

    else:
        return redirect('contactpage')














