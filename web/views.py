from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Team, HeaderSliderContent
from django.views.generic import ListView, TemplateView


class HomeView(TemplateView):
    template_name = "index.html"
