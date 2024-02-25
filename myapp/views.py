from django.shortcuts import render
from .forms import ImageForm
from .models import Image ,Comment

# Create your views here.
def home(request):
    if request.method=='POST':
        form =ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
   
    form =ImageForm()
    img =Image.objects.all()
    com=Comment.objects.all()
    return render(request,'myapp/index.html',{'form':form,'img':img,'com':com})
