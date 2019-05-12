from django.shortcuts import HttpResponse, render


def index(request):
    return render(request, 'midi/index.html')

def music_vae(request):
    return HttpResponse("vae")

def make_one(request):
    return HttpResponse("음악이 완성되었습니다.")