from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

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


def experience(request):
  experience = [
    
      {
      'company':'Smavy Private Limited',
      'position':'Freelance English Tutor',
      'period':'Present'
    },
    {
      'company':'Draup',
      'position':'Research Executive',
      'period':'Mar 2022 - May 2024'
    },
    {
      'company':'Amazon (contract)',
      'position':'Customer Service Associate',
      'period':'Aug 2021 - Nov 2021'
    },
      {'company':'TNQ Technologies',
      'position':'Copy Editor',
      'period':'Oct 2020 - Aug 2021'
    },  
  ]
  return render(request,'experience.html',{'experience':experience})


def certificate(request):
  return render(request,'portfolio/certificate.html')

def contact(request):
  return render(request,'portfolio/contact.html')

def resume(request):
  resume_path = "file/KaviyaRaajenthiran_resume.pdf"
  resume_path=staticfiles_storage.path(resume_path)
  if staticfiles_storage.exists(resume_path):
    with open(resume_path,"rb") as resume_file:
      response = HttpResponse(resume_file.read(),content_type = "application/pdf")
      response["Content-Disposition"]='attachment';filename='KaviyaRaajenthiran_resume.pdf'
      return response
  else:
    return HttpResponse('resume not found',status=404)