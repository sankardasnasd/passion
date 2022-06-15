from django.urls import path
from . import views

app_name="app1"
urlpatterns = [
    path('sample',views.sample,name='sample'),
    path('grid',views.grid,),
    path('bootstrap',views.bootstrap),
    path('boostrapgrid',views.boostrapgrid),
    path('javascript',views.javascript),
    path('loginpage',views.loginpage,name='loginpage'),
    path('javascriptcond',views.javascriptcond),
    path('jsloops',views.jsloops),
    path('jquery',views.jquery),
    path('men',views.men,name="men"),
    path('women',views.women,name="women"),
    path('kids',views.kids,name="kids"),
    path('contact',views.contact,name="contact"),
    path('fooditems',views.fooditems,name="fooditems"),
    path('mobiles',views.mobiles,name="mobiles"),
    path('electronics',views.electronics,name="electronics"),
    path('home-items',views.homeitems,name="home-items")
    
]
