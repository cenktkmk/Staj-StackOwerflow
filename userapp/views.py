from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from .models import *
from .form import *


from django.contrib import messages

from django.shortcuts import get_object_or_404

def increase_tag_view(tag_id):
    tag = get_object_or_404(Tags, pk=tag_id)
    tag.view += 1
    tag.save()

def index(request):

    return render(request, 'index.html')


def profile(request, user_uuid):
    user = get_object_or_404(CustomUser, user_uuid=user_uuid)
    followers_count = user.followers.count()
    following_count = user.following.count()
    badges = user.badge.all()


    context = {
        'badges': badges,
        'user': user,
        'followers_count': followers_count,
        'following_count': following_count,
    }

    return render(request, 'profile.html', context)

def questions(request):
    context = {}
    sorular = Post.objects.all().order_by("-createdAt")
    context["sorular"] = sorular

   
    
    return render(request, 'questions.html', context)


def questionDetails(request, questionId):
    context = {}

    form2 = CommentForm
    context["form2"] = form2
    form3 = AnswerForm
    context["form3"] = form3    


    soru = Post.objects.filter(id=questionId).first()
    yorumlar = Comments.objects.filter(post = soru)
    context["yorumlar"] = yorumlar

    yorumlar2 = Comments2.objects.filter(answer__post = soru)
    context["yorumlar2"] = yorumlar2
    if request.method == "POST":
        form = YourModelForm(request.POST)
        if form.is_valid():
            postform = form.save(commit=False)
            postform.user = request.user
            postform.post = soru
            postform.save()
            return redirect ("questionDetails", questionId)

    else:
        
        context["sorular"] = soru
        cevaplar = Answer.objects.filter(post=soru)
        context["cevaplar"] = cevaplar
        context["form"] = YourModelForm
        return render(request, 'questionsDetail.html',context)


def commentCreate(request, questionId):
    context = {}
    soru = Post.objects.filter(id=questionId).first()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            postform = form.save(commit=False)
            postform.user = request.user
            postform.post = soru
            postform.save()
            return redirect ("questionDetails" , questionId)

def commentCreate2(request, answerId , questionId):
    context = {}
    
    

    if request.method == "POST":
        yorumlar2 = Answer.objects.filter(id = answerId).first()
        form = AnswerForm(request.POST)
        if form.is_valid():
            postform = form.save(commit=False)
            postform.user = request.user
            postform.answer = yorumlar2
            postform.save()
            return redirect ("questionDetails" , questionId)



def tags(request):

    return render(request, 'tags.html')


def users(request):

    return render(request, 'users.html')



def createpost(request):
    context = {}
    if request.method == "POST":
        form = CreatePost(request.POST)
        if form.is_valid():
            postform = form.save(commit=False)
            postform.user = request.user
            postform.save()
            form.save_m2m()

            # Oluşturulan postun içerdiği taglerin view sayısını artırın
            for tag in postform.tagleri.all():
                increase_tag_view(tag.id)

            return redirect("questions")
    else:
        context["form"] = CreatePost

        return render(request, "createPost.html", context)    
    
def addLike(request, userId, postId):

  
    user = CustomUser.objects.filter(user_uuid=userId).first()
    post = Post.objects.filter(id=postId).first()
    
    dislikeModel = PostDislike.objects.filter(user=user) & PostDislike.objects.filter(post=post)

    is_liked = PostLikes.objects.filter(user=user) & PostLikes.objects.filter(post=post)

    if is_liked:
        

        return redirect("questionDetails" , postId)
    
    if user and post:
        if dislikeModel:
            dislikeModel.delete()
        PostLikes.objects.create(
            user = user,
            post = post
           

        )
        postlike = post.like + 1
        
        post.like = postlike
        post.save(update_fields=['like'])



        return redirect("questionDetails" , postId)     
def dislike(request, userId, postId):

  
    user = CustomUser.objects.filter(user_uuid=userId).first()
    post = Post.objects.filter(id=postId).first()

    likeModel = PostLikes.objects.filter(user=user) & PostLikes.objects.filter(post=post)

    is_disliked = PostDislike.objects.filter(user=user) & PostDislike.objects.filter(post=post)

    if is_disliked:
        

        return redirect("questionDetails" , postId)
    
    if user and post:
        if likeModel:
            likeModel.delete()
        PostDislike.objects.create(
            user = user,
            post = post
           

        )
        postlike = post.like - 1
        
        post.like = postlike
        post.save(update_fields=['like'])



        return redirect("questionDetails" , postId)         
    
def answerlike(request, userId, answerId):

  
    user = CustomUser.objects.filter(user_uuid=userId).first()
    post = Answer.objects.filter(id=answerId).first()
    is_liked = AnswerLikes.objects.filter(user=user) & AnswerLikes.objects.filter(answer=post)
    dislikeModel = AnswerDislike.objects.filter(user=user) & AnswerDislike.objects.filter(answer=post)

    if is_liked:
        

        return redirect("questionDetails" , post.post.id)
    
    if user and post:
        if dislikeModel:
            dislikeModel.delete()
            
        AnswerLikes.objects.create(
            user = user,
            answer = post
           

        )
        postlike = post.like + 1
        
        post.like = postlike
        post.save(update_fields=['like'])



        return redirect("questionDetails" , post.post.id)     
def answerdislike(request, userId, answerId):

  
    user = CustomUser.objects.filter(user_uuid=userId).first()
    post = Answer.objects.filter(id=answerId).first()
    is_disliked = AnswerDislike.objects.filter(user=user) & AnswerDislike.objects.filter(answer=post)
    likeModel = AnswerLikes.objects.filter(user=user) & AnswerLikes.objects.filter(answer=post)

    if is_disliked:
        

        return redirect("questionDetails" , post.post.id)
    
    if user and post:
        if likeModel:
            likeModel.delete()        
        AnswerDislike.objects.create(
            user = user,
            answer = post
           

        )
        postlike = post.like - 1
        
        post.like = postlike
        post.save(update_fields=['like'])



        return redirect("questionDetails" , post.post.id)             