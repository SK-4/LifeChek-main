from django.shortcuts import render,redirect,get_object_or_404
from .models import Question
from accounts.models import User
from random import sample
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import RelativeForm
import csv
import random
from django.db.models import Avg

def index(request):
    return render(request, 'index.html')

@login_required
def quiz(request):
    questions = Question.objects.order_by('?')[:10]

    if request.method == 'POST':
        for question in questions:
            selected_option = request.POST.get(f'question_{question.id}')
            if selected_option:
                question.selected_option = selected_option
                question.save()
            else:
                question.selected_option = None
                question.save()

        return redirect('results')

    # If the request method is not POST, clear the selected options
    for question in questions:
        question.selected_option = None
        question.save()

    return render(request, 'quiz.html', {'questions': questions})
# def quiz(request):
#     # Retrieve the current question index from the session, or initialize it to 0 if it does not exist
#     current_question_index = request.session.get('current_question_index', 0)

#     # Retrieve the current question from the database
#     question = Question.objects.order_by('?')[:5][current_question_index]

#     if request.method == 'POST':
#         selected_option = request.POST.get('selected_option')
#         if selected_option:
#             # Save the selected option for the current question
#             question.selected_option = selected_option
#             question.save()

#             # Increment the current question index and store it in the session
#             # current_question_index += 1
#             # request.session['current_question_index'] = current_question_index

#             # If all questions have been answered, redirect to the results page
#             if current_question_index >= 5:
#                 return redirect('results')

#             # Retrieve the next question from the database
#             question = Question.objects.order_by('?')

#     return render(request, 'quiz.html', {'question': question})

@login_required
def results(request):
    questions = Question.objects.all()[:5]
    count = len(questions)
    score = 0
    for question in questions:
        if question.selected_option == question.correct_option:
            score += 1
        elif question.selected_option == "Several Days":
            score += 0.4
        elif question.selected_option == "MORE THAN HALF THE DAYS":
            score+=0.2
        else:
            score+=0

    # Update user score
    request.user.mental_score = (score / count) * 100.0
    request.user.save()
    context = "You are doing great"
    return render(request, 'results.html',{'context':context})

def patient_details(request, first_name):
    patient = get_object_or_404(User, first_name=first_name)
    return render(request, 'accounts/doctor/patient_details.html', {'patient': patient})

def display_all_patients(request):
    patients = User.objects.filter(role="patient").values('first_name', 'last_name', 'email','date_joined','mental_score')
    # print(patients)
    context = {
        'title': 'All Patients',
        'patients': patients
    }
    return render(request, 'accounts/doctor/all-patient.html', context)

def music(request):
    return render(request,'music.html')

class RelativeView(LoginRequiredMixin, View):
    form_class = RelativeForm
    template_name = 'user_info.html'
    # success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = User.objects.get(email=request.user.email)
            user.relative_name = form.cleaned_data['relative_name']
            user.relative_email = form.cleaned_data['relative_email']
            user.relative_phone_number = form.cleaned_data['relative_phone_number']
            user.save()
            messages.success(request, 'Relative information saved successfully!')
            return redirect(success_url)
        # return render(request, self.template_name, {'form': form})
    

def success_url(request):
    return render(request,'success.html')


def streamlit_view(request):
    return render(request, 'streamlit.html')

def chatroom(request):
    return render(request,'chatroom.html')

def get_random_tweet():

    with open('random_tweets.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        tweets = [row['tweet'] for row in reader]

    return random.choice(tweets)

def random_tweet_view(request):
    # tweets = []
    # for i in range(5):
    #     tweet = get_random_tweet()
    #     tweets.append(tweet)
    tweet = get_random_tweet()
    print(tweet)
    return render(request, 'tweet.html', {'tweet': tweet})
