from django.shortcuts import render
from listings.choices import price_choices,state_choices,bedroom_choices
from listings.models import Listing
from realtors.models import Realtor
# Create your views here.

def index(req):
    listings=Listing.objects.all()[:3]   
    context={
        'listings':listings,
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices
    }
    return render(req,'pages/index.html',context)

def about(req):
    realtors=Realtor.objects.all()
    mvp_realtors=Realtor.objects.all().filter(is_mvp=True)
    context={
        'realtors':realtors,
        'mvp_realtors':mvp_realtors
    }

    return render(req,'pages/about.html',context)
