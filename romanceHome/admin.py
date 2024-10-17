from django.contrib import admin
from .models import slide, mustKnow, globalQuality, downloadApp,Community, Customer,Members,YourOrder,Hasad,communityService,Services,locationBranch,offers,news,About,TitleForPageChoice,lastOffers

# Register your models here.

class AdminlastOffers(admin.ModelAdmin):
    list_display = ('id', 'status','video_url')

    class Meta:
        model = lastOffers
admin.site.register(lastOffers,AdminlastOffers)

class Adminslide(admin.ModelAdmin):
    list_display = ('id', 'title','description')

    class Meta:
        model = slide
admin.site.register(slide,Adminslide)

class AdminYourOrder(admin.ModelAdmin):
    list_display = ('id','image')

    class Meta:
        model = YourOrder        
admin.site.register(YourOrder,AdminYourOrder)

class AdminmustKnow(admin.ModelAdmin):
    list_display = ('id', 'video_url')

    class Meta:
        model = mustKnow
admin.site.register(mustKnow,AdminmustKnow)

class AdmincommunityService(admin.ModelAdmin):
    list_display = ('id', 'title','description')

    class Meta:
        model = communityService
admin.site.register(communityService,AdmincommunityService)

class AdminGlobalQuality(admin.ModelAdmin):
    list_display = ('id', 'title','description')

    class Meta:
        model = globalQuality
admin.site.register(globalQuality,AdminGlobalQuality)

class AdmindownloadApp(admin.ModelAdmin):
    list_display = ('id', 'title','description')

    class Meta:
        model = downloadApp
admin.site.register(downloadApp,AdmindownloadApp)

class AdminCommunity(admin.ModelAdmin):
    list_display = ('id', 'title','question','answer')

    class Meta:
        model = Community
admin.site.register(Community,AdminCommunity)

class AdminCustomer(admin.ModelAdmin):
    list_display = ('id', 'title','question','answer')

    class Meta:
        model = Customer
admin.site.register(Customer,AdminCustomer)

class AdminMembers(admin.ModelAdmin):
    list_display = ('id', 'title','question','answer')

    class Meta:
        model = Members
admin.site.register(Members,AdminMembers)

class AdminServices(admin.ModelAdmin):
    list_display = ('id', 'title','price')

    class Meta:
        model = Services
admin.site.register(Services,AdminServices)

class AdminHasad(admin.ModelAdmin):
    list_display = ('id', 'title','question','answer')

    class Meta:
        model = Hasad
admin.site.register(Hasad,AdminHasad)

class AdminlocationBranch(admin.ModelAdmin):
    list_display = ('id', 'title','description','branch')

    class Meta:
        model = locationBranch
admin.site.register(locationBranch,AdminlocationBranch)

class Adminoffers(admin.ModelAdmin):
    list_display = ('id', 'title','description','date')

    class Meta:
        model = offers
admin.site.register(offers,Adminoffers)

class Adminnews(admin.ModelAdmin):
    list_display = ('id', 'title','description','date')

    class Meta:
        model = news
admin.site.register(news,Adminnews)

class AdminAbout(admin.ModelAdmin):
    list_display = ('id', 'title','description')

    class Meta:
        model = About
admin.site.register(About,AdminAbout)

class AdminTitleForPageChoice(admin.ModelAdmin):
    list_display = ('id', 'title','description')

    class Meta:
        model = TitleForPageChoice
admin.site.register(TitleForPageChoice,AdminTitleForPageChoice)
