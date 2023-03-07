from django.shortcuts import render

# Create your views here.

def course(request):
    title1='multi-app'
    title='COURSE'
    description='Running from course app'
    return render(request,'course.html',{'title':title,'desc':description,'title1':title1})