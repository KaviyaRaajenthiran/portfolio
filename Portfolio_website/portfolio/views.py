from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request,'portfolio/home.html')

def about(request):
  return render(request,'portfolio/about.html')

def projects(request):
  projects_show = [
    {'title':'Portfolio',
     'path':'portfolio/images/portfolio image.png'
     },
     {'title':'Food App',
     'path':'portfolio/images/portfolio image.png'
     }
  ] 
  return render(request,'portfolio/projects.html',{'projects_show':projects_show})