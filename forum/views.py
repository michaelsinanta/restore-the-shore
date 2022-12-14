from forum.models import Post, Comment
from .forms import PostForm, CommentForm

from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import datetime

# Create your views here.
@login_required(login_url="/welcome/login/")
@csrf_exempt
def show_forum(request):
    posts_data = Post.objects.all()
    context = {
        'posts_data' : posts_data
    }
    return render(request, "forum.html", context)

@login_required(login_url="/welcome/login/")
@csrf_exempt
def show_forum_json(request):
    posts_data = Post.objects.all()
    return HttpResponse(serializers.serialize("json", posts_data), content_type="application/json")

@login_required(login_url="/welcome/login/")
@csrf_exempt
def show_forum_json_by_user(request):
    posts_data= Post.objects.filter(creator=request.user)
    return HttpResponse(serializers.serialize("json", posts_data), content_type="application/json")

@login_required(login_url="/welcome/login/")
@csrf_exempt
def show_comments_json(request, id):
    comments_data = Comment.objects.filter(original_post_id=id)
    return HttpResponse(serializers.serialize("json", comments_data), content_type="application/json")

@login_required(login_url="/welcome/login/")
@csrf_exempt
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.creator = request.user
            form.creator_name = request.user.username
            form.date = datetime.datetime.now()
            form.save()

            return JsonResponse({
                "model": "forum.post",
                "pk": form.pk,
                "fields":
                {
                    "creator": form.creator.pk,
                    "creator_name": form.creator_name,
                    "date": form.date,
                    "content": form.content,
                    "image": form.image
                }
            })
    else:
        return HttpResponseBadRequest('Invalid request')

@login_required(login_url="/welcome/login/")
@csrf_exempt
def add_comment(request, id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.creator = request.user
            form.creator_name = request.user.username
            form.date = datetime.datetime.now()
            form.original_post_id = id
            form.save()

        comments_data = Comment.objects.all()
        context = {
            "comments_data": comments_data
        }    
        return render(request, "forum.html", context)
    else:
        return HttpResponseBadRequest('Invalid request')

# api

@csrf_exempt
def post_post(request):
    if request.method == 'POST':
        return add_post(request)
    
    return HttpResponse(status=404)

@login_required(login_url="/welcome/login/")
@csrf_exempt
def post_comment(request, id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.creator = request.user
            form.creator_name = request.user.username
            form.date = datetime.datetime.now()
            form.original_post_id = id
            form.save()

            return JsonResponse({
                "model": "forum.comment",
                "pk": form.pk,
                "fields":
                {
                    "creator": form.creator.pk,
                    "creator_name": form.creator_name,
                    "date": form.date,
                    "content": form.content,
                    "original_post_id": form.original_post_id,
                }
            })

    return HttpResponse(status=404)
