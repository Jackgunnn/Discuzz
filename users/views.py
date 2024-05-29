from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout, login as auth_login, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from questions.models import Question, Answer
from .forms import UserProfileForm, PasswordChangeCustomForm
from django.core.paginator import Paginator

def home1(request):
    questions = Question.objects.all().order_by("-asked_at")
    paginator = Paginator(questions,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'homepage_with_pagination.html', {'page_obj':page_obj, 'questions':questions})

def home(request):
    questions = Question.objects.order_by("-asked_at")
    return render(request, 'homepage.html', {'questions': questions})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Redirect to home page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def logout(request):
    auth_logout(request)
    return redirect('home')


@login_required
def user_profile(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    question_count = Question.objects.filter(asked_by=user_id).count()
    answer_count = Answer.objects.filter(answered_by=user_id).count()
    return render(request, 'user_profile.html', {"user": user,"question_count": question_count, "answer_count": answer_count})


def edit_profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=request.user)
        password_form = PasswordChangeCustomForm(request.user, request.POST)

        if profile_form.is_valid():
            profile_form.save()
            return redirect('user_profile')
        elif password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            return redirect('user_profile')
    else:
        profile_form = UserProfileForm(instance=request.user)
        password_form = PasswordChangeCustomForm(request.user)
    return render(request, 'edit_profile.html', {"profile_form": profile_form, "password_form": password_form})


@login_required
def user_questions(request):
    user_id = request.user.id
    questions = Question.objects.filter(asked_by=user_id).order_by("-asked_at")
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        question = get_object_or_404(Question, id=question_id)
        question.delete()
    return render(request, 'user_questions.html', {"questions": questions})


@login_required
def user_answers(request):
    user_id = request.user.id
    answers = Answer.objects.filter(answered_by=user_id).order_by("answered_at")
    if request.method == 'POST':
        answer_id = request.POST.get('answer_id')
        answer = get_object_or_404(Answer, id=answer_id)
        answer.delete()
    return render(request, 'user_answers.html', {"answers": answers})


def other_user_profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    question_count = Question.objects.filter(asked_by=user_id).count()
    answer_count = Answer.objects.filter(answered_by=user_id).count()
    return render(request, 'other_user_profile.html',
                  {"user": user, "question_count": question_count, "answer_count": answer_count})


def other_user_questions(request,user_id):
    questions = Question.objects.filter(asked_by=user_id).order_by("-asked_at")
    return render(request, "other_user_questions.html", {"questions":questions})
def other_user_answers(request, user_id):
    answers = Answer.objects.filter(answered_by=user_id).order_by("-answered_at")
    return render(request, "other_user_answers.html", {"answers": answers})

