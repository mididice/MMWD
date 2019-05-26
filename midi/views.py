from django.shortcuts import HttpResponse, render
from django.conf import settings
import os
import numpy as np
from midi import combine
from django.core.files.storage import FileSystemStorage


def index(request):
    midi_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
    np.random.shuffle(midi_list)
    # json_list = json.dumps(midi_list)
    return render(request, 'midi/index.html', {'json_list': midi_list})


def music_vae(request):
    return HttpResponse("vae")


def make_one(request, slug):
    print(slug)
    base_dir = settings.BASE_DIR
    basic_dir = os.path.join(base_dir, 'wavebasic')
    result_dir = os.path.join(base_dir, 'waveresult')
    filename = ''.join(slug)+".wav"
    outfile = os.path.join(result_dir, filename)
    #같은 패턴 있을 경우에 파일 생성 하지 않는 로직 추가
    #total second도 같이 보내기
    result_list = slug.split('-')
    combine.tidalwave(basic_dir, result_list, outfile)

    return render(request, 'midi/result.html', context={'music_list': result_list, 'music': filename})

#다운로드 추가
