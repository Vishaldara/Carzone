# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import datetime

# Create your views here.


def say_hello(request):
    return HttpResponse('Hello, World!')


def get_now(request):
    now = datetime.datetime.now()
    return render(request, "HelloWorld/base.html", {"current_date": now})