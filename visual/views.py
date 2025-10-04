from django.shortcuts import render

# Create your views here.
def homePage(req):
    
    return render(
        request=req, 
        template_name = 'visual/index.html'
    )