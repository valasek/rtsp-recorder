# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from rtsp_recorder.recorder.tasks import start_ffmpeg, stop_ffmpeg


# from django.core.urlresolvers import reverse
# from django.views.generic import DetailView, ListView, RedirectView, UpdateView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from .models import User


def recording(request):
    if request.GET.get('mybtn') == 'Start':
        print("*** Calling start_ffmpeg")
        start_ffmpeg.delay()
        return HttpResponse(status=204)
    elif request.GET.get('mybtn') == 'Stop':
        print("*** Calling stop_ffmpeg")
        stop_ffmpeg.delay()
        return HttpResponse(status=204)
    else:
        print("*** Recording view main page")
        return render(request, 'recorder/record.html')
