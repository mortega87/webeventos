from django.shortcuts import render_to_response
# from .models import Post
from django.template.context import RequestContext
# from django.contrib.auth.models import User
# from django.core.urlresolvers import reverse
# from django.http.response import HttpResponseRedirect
# from django.contrib.auth.decorators import login_required
# from django.contrib import auth


def index(request):
    # posts = Post.objects.filter(published_date__isnull=False).order_by('published_date')
    # activa_index = True
    titulo= 'WebEventos'
    return render_to_response('bloques/index.html',{'titulo':titulo}, context_instance=RequestContext(request))

def login(request):

    return render_to_response('popup.html', context_instance=RequestContext(request))

def about(request):
    titulo= 'About - WebEventos'
    return render_to_response('bloques/about.html', {'titulo':titulo}, context_instance=RequestContext(request))