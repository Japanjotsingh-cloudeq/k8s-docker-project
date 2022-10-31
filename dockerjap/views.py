from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def jk(request):
    return render(request,'jk.html')
# def img(request):
#     return render(request,'jap.jpg')