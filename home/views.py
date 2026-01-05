
from django.shortcuts import render,HttpResponse
from django.http import HttpResponse

# Create your views here.
def index(request):
     # context = {
     #      "variable":"This is sent"   
     # }
     return render(request,'index.html')      
   #return HttpResponse("This is homepage")
def Inventory(request):
     return render(request,'Inventory.html')
     #return HttpResponse("This is Inventory page ")
def Sales(request):
     return render(request,'Sales.html')
     #return HttpResponse("This is Sales page") 
def DemandForecasting(request):
     return render(request,'DemandForecasting.html')
     #return HttpResponse("This is DemandForecasting page ")
# def Reports(request):
#      return HttpResponse("This is Reports page")
def PurchasePlan(request):
     return render(request,'PurchasePlan.html')
     #return HttpResponse("This is PurchasePlan page")
def SmartAlerts(request):
     return render(request,'SmartAlerts.html')
     #return HttpResponse("This is SmartAlerts page")
def PurchasePlan(request):
     return render(request,'PurchasePlan.html')
     #return HttpResponse("This is PurchasePlan page")
def DownloadReports(request):
     return render(request,'DownloadReports.html')
     #return HttpResponse("This is DownloadReports page")
def Admin(request):
     return render(request,'Admin.html')
     #return HttpResponse("This is Admin page")