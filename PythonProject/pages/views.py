from django.shortcuts import render
import random
# Create your views here.

from django.http import HttpResponse

def home(request):
    random_num = random.randint(1,10)
    context = {
        'random' : random_num
    }
    return render(request,'pages/home.html',context)

def about(request):
    return render(request,'pages/about.html')

def send(request):
    return render(request,'pages/send.html')

def recieve(request):
     if request.method == 'GET': #GET jahle capital hunu parcha
       email = request.GET.get('email')
       sometext = request.GET.get('Sometext')
       return HttpResponse(f"Hii from get .{email=} {sometext=}")

     if request.method == 'POST':
             email = request.POST.get('email')
             sometext = request.POST.get('Sometext') 
             return HttpResponse(f"Hii from post .{email=} {sometext=}")


def takenum(request):
    return render(request,'pages/takenum.html')

def Average(request):
     if request.method=='POST':
         FirstNumber = request.POST.get('FirstNumber')
         SecondNumber =request.POST.get('SecondNumber')
         avg= (int(FirstNumber) + int(SecondNumber))/2
         return HttpResponse(f"Average of two number is.{avg=}")

       

                  
         
                

      
    
