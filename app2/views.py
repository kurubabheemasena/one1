from django.shortcuts import render

# Create your views here.
def an(request):
    d={'name':'bheemasena'}
    return render(request,'first1.html',context=d)
