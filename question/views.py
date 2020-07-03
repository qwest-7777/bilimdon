from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomLoginForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import CustomUser, Question, Choice, Answered, Statistic
import random

User_get = get_user_model()


def home(request):
    if request.user:
        lang = request.LANGUAGE_CODE
        
        user = request.user
        username = request.user.username
        failed = Answered.objects.filter(answered_user=username, failed_answer=True)
        if failed:
            return render(request, 'pages/home.html', {'failed_answer': True})
        else:
            answered = list(Answered.objects.values_list('question', flat=True).filter(answered_user=username))
            if len(answered) < 11:
                questions_id_list = list(Question.objects.values_list('id', flat=True).filter(question_language=lang))
                a = set(questions_id_list)^set(answered)
                random_question_id = random.choice(list(a))
                questions = Question.objects.get(id=random_question_id)
                return render(request, 'pages/home.html', {'user': user, 'question':questions})
            else:
                question = False
                return render(request, 'pages/home.html', {'question': question})
    else:
        questions_id_list = Question.objects.values_list('id', flat=True).all()
        random_question_id = (random.sample(list(questions_id_list), 1))
        questions = Question.objects.filter(id__in=random_question_id)
        return render(request, 'pages/home.html', {'question': questions})


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            phone_number = form.cleaned_data.get('phone_number')
            password = form.cleaned_data.get('password1')
            user = CustomUser.objects.create_user( username=username, phone_number=phone_number, is_active=True, password=password)
            user.save()
            user = authenticate(username=username, password=password)            
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'registration/login.html', {'form': form,'error': 1})
    else:
        form = CustomLoginForm()
    return render(request, 'registration/login.html', {'form': form})

def vote(request, question_id, choice_id):
    if request.user:
        question = get_object_or_404(Question, pk=question_id)
        choice = get_object_or_404(Choice, pk=choice_id)
        user = request.user
        
        if choice.result:
            user.statistic.scores +=30
            user.statistic.right_answer +=1
            user.statistic.save()
            answered = Answered.objects.create(question=question, answered_user=request.user.username, failed_answer=False)

            return redirect('home')
        elif choice.result == False:
            user.statistic.false_answer +=1
            user.statistic.save()
            answered = Answered.objects.create(question=question, answered_user=request.user.username, failed_answer=True)

        return redirect('home')

    else:
        return redirect('login')


def user_page(request):
    user = request.user
    score = Statistic.objects.get(user=user)
    cash = user.statistic.scores * 2000
    context = {
        'user':user,
        'score':score,
        'cash':cash
    }
    return render(request, 'pages/user_page.html', context)


def contacts(request):
    return render(request, 'pages/contact.html')