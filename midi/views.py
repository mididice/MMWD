from django.shortcuts import HttpResponse, render
from django.conf import settings
import os
import os.path
import numpy as np
from midi import combine


def index(request):
    midi_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
    np.random.shuffle(midi_list)
    return render(request, 'midi/index.html', {'json_list': midi_list})


def music_vae(request):
    return HttpResponse("vae")


def make_one(request, slug):
    base_dir = settings.BASE_DIR
    basic_dir = os.path.join(base_dir, 'wavebasic')
    result_dir = os.path.join(base_dir, 'waveresult')
    filename = ''.join(slug)+".wav"
    outfile = os.path.join(result_dir, filename)
    result_list = slug.split('-')
    if not os.path.isfile(outfile):
        combine.tidalwave(basic_dir, result_list, outfile)
    return render(request, 'midi/result.html',
                  context={'music_list': result_list, 'music': filename})

#다운로드 추가
