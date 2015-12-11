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
    return render_to_response('index.html', context_instance=RequestContext(request))

def login(request):
    print('por aqui')
    return render_to_response('popup.html', context_instance=RequestContext(request))