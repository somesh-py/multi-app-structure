from django.shortcuts import render

# Create your views here.

def app(request):
    title1='multi-app'    
    title='APP'
    place='Running from inner project'
    return render(request,'app/app.html',{'title':title,'place':place,'title1':title1})