from django.shortcuts import render


def homepage(request):
    bio = "Hi, my name is John Gaitho, a freelancer software developer " \
          "from Nairobi,Kenya with 3+ years of experience. I make websites " \
          "and desktop apps using Python(Django) and Java respectively. " \
          "I am passionate to coding and ready to work under pressure to have" \
          " the deadline met. I value my clients and i will involve you during " \
          "the entire development process to ensure that what you get is exactly " \
          "what you wanted. Feel free to contact me at anytime, any day for enquiries or concern"
    return render(request, 'home.html',{'bio' :bio})
















