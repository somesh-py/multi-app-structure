from django.shortcuts import render

# Create your views here.

def fees(request):
    title1='multi-app'
    title='FEES'
    description='Running from fees app'
    return render(request,'fees.html',{'title':title,'desc':description,'title1':title1})