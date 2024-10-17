from romanceHome import views
from django.urls import path

urlpatterns = [
    # path('set-language/', views.set_language, name='set_language'),
    path("", views.index, name="index"),
    path("customers", views.customers, name="customers"),
    path("members", views.members, name="members"),
    path("community", views.community, name="community"),  
    path("about", views.about, name="about"),
    path("ourServices", views.ourServices, name="ourServices"),
    path("hasad", views.hasad, name="hasad"),
    path("locationBarnch", views.locationBarnch, name="locationBarnch"),
    path("ourNew", views.ourNew, name="ourNew"),
    path("404", views.errorpage, name="404"),
  ]
