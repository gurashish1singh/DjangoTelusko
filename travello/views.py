from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):

    dest1 = Destination()
    dest2 = Destination()
    dest3 = Destination()

    # context = {
    #     'dest1' : dest1,
    #     'dest2' : dest2,
    # }
 
    dest1.name = 'Delhi'
    dest1.desc = 'Best food'
    dest1.price = 1000
    dest1.img = 'destination_1.jpg'
    dest1.offer = False

    dest2.name = 'Kingston'
    dest2.desc = 'Panda Place'
    dest2.price = 500
    dest2.img = 'destination_2.jpg'
    dest2.offer = True

    dest3.name = 'New Jersey'
    dest3.desc = 'Bunny Place'
    dest3.price = 800
    dest3.img = 'destination_3.jpg'
    dest3.offer = False

    dests = [dest1,dest2,dest3]
    
    context = {
        'dests' : dests,
    }

    return render(request, 'index.html', context)

 