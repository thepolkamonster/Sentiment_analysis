from django.shortcuts import render, redirect
from . import final

def home_view(request):
    template = 'common/home.html'
    context = {}
    return render(request,template,context)
# Create your views here.
def sentiment(request):
    res = ""
    if request.method == 'POST':
        if request.POST.get('pred_button'):
            name = request.POST['text data']
            res = final.pre(str(name))
            # print(res)
        else:
            redirect('homepage')
            res = ""
    else:
        print("Error Occurred")

    return render(request, "first.html", {'result': res})