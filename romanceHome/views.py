from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .models import slide,mustKnow,globalQuality,downloadApp,Community,Customer,Members,YourOrder,communityService,Hasad,Services,TitleForPageChoice,locationBranch,offers,news,About,lastOffers
from django.shortcuts import redirect

def index(request):
    slides = slide.objects.all()
    last_offer = lastOffers.objects.filter(status=True).last()
    YourOrders=YourOrder.objects.all()
    mustKnows = mustKnow.objects.last()
    TitleForPageChoices = TitleForPageChoice.objects.all()
    globalsQuality = globalQuality.objects.all() 
    communityServices=communityService.objects.all()
    downloadApps = downloadApp.objects.last()
    context = {'slides' : slides,'TitleForPageChoices':TitleForPageChoices,'YourOrders':YourOrders ,'mustKnows' : mustKnows,'globalsQuality' : globalsQuality,'communityService':communityServices ,'downloadApps' : downloadApps,'last_offer':last_offer}
    return render(request, "index.html",context)

def community(request):
    slides = slide.objects.all()
    TitleForPageChoices = TitleForPageChoice.objects.all()
    community = Community.objects.all().order_by('-id')[:4][::-1]
    communities = {'slides':slides ,'TitleForPageChoices' : TitleForPageChoices,'community' : community}
    return render(request, 'community.html', communities)

def customers(request):
    slides = slide.objects.all()
    TitleForPageChoices = TitleForPageChoice.objects.all()
    customer = Customer.objects.all().order_by('-id')[:4][::-1]
    customers = {'slides':slides ,'TitleForPageChoices' : TitleForPageChoices,'customer' : customer}
    return render(request, 'customers.html', customers)

def members(request):
    slides = slide.objects.all()
    TitleForPageChoices = TitleForPageChoice.objects.all()
    member = Members.objects.all().order_by('-id')[:4][::-1]
    members = {'slides':slides ,'TitleForPageChoices' : TitleForPageChoices,'member' : member}
    return render(request, "members.html", members)

def ourServices(request):
    slides = slide.objects.all()
    TitleForPageChoices = TitleForPageChoice.objects.all()
    Service = Services.objects.all().order_by('-id')[:4][::-1]
    ourServices = {'slides':slides ,'TitleForPageChoices' : TitleForPageChoices,'Service' : Service}
    return render(request, "ourservices.html",ourServices)

def hasad(request):
    slides = slide.objects.all()
    TitleForPageChoices = TitleForPageChoice.objects.all()
    hasad = Hasad.objects.all().order_by('-id')[:4][::-1]
    hasads = {'slides':slides ,'TitleForPageChoices' : TitleForPageChoices,'hasad' : hasad}
    return render(request, "hasd.html",hasads)

def locationBarnch(request):
    slides = slide.objects.all()
    locationsBranch=locationBranch.objects.all()
    locationBarnches = {'locationsBranch':locationsBranch ,'slides' : slides}
    return render(request, "locationbarnch.html",locationBarnches)

def ourNew(request):
    slides = slide.objects.all()
    offer=offers.objects.all()
    new = news.objects.all()
    newses = {'slides':slides ,'offer':offer ,'new' : new}
    return render(request, "whatnew.html",newses)

def about(request):
    slides = slide.objects.all()
    TitleForPageChoices = TitleForPageChoice.objects.all()
    about = About.objects.all()
    abouts = {'slides':slides ,'TitleForPageChoices' : TitleForPageChoices,'about' : about}
    return render(request, "aboutus.html",abouts)

def errorpage(request):
    return render(request, "404.html")

def logout_view(request):
    logout(request)
    return redirect('index')
