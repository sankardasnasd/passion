from django.urls import path
from . import views

urlpatterns = [
    path('sample',views.sample,name='sample'),
    path('grid',views.grid,),
    path('bootstrap',views.bootstrap),
    path('boostrapgrid',views.boostrapgrid),
    path('javascript',views.javascript),
    path('loginpage',views.loginpage),
    path('javascriptcond',views.javascriptcond),
    path('jsloops',views.jsloops),
    path('jquery',views.jquery)
    
]
