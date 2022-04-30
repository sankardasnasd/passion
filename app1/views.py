from django.shortcuts import render

def sample(request):
    return render(request, 'sample.html')


def grid(request):
    return render(request, 'grid.html')

    
def bootstrap(request):
    return render(request, 'bootstrap.html')



def boostrapgrid(request):
    return render(request, 'boostrapgrid.html')





def javascript(request):
    return render(request, 'javascript.html')   

def loginpage(request):
    return render(request, 'loginpage.html')  


def javascriptcond(request):
    return render(request, 'javascriptcond.html') 


def jsloops(request):
    return render(request, 'dom.html')    


def jquery(request):
    return render(request, 'jquery.html')    

