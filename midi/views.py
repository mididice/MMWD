from django.shortcuts import HttpResponse, render
import numpy as np
import json
import combine

def index(request):
    midi_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
    np.random.shuffle(midi_list)
    json_list = json.dumps(midi_list)
    return render(request, 'midi/index.html', {'json_list': midi_list})

def music_vae(request):
    return HttpResponse("vae")

def make_one(request):
    result_list = request.GET.get("result_list")
    print(result_list)
    outfile = ''.join(infiles)+".wav"
    combine.tidalwave(result_list, outfile)
    return HttpResponse("음악이 완성되었습니다.리스트:{}".format(result_list))