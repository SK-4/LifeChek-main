from django.shortcuts import render,redirect
from .models import Question
from accounts.models import User
from random import sample
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

# def quiz(request):
#     questions = Question.objects.order_by('?')[:5]

#     if request.method == 'POST':
#         for question in questions:
#             selected_option = request.POST.get(f'question_{question.id}')
#             if selected_option:
#                 question.selected_option = selected_option
#                 question.save()

#         return redirect('results')

#     return render(request, 'quiz.html', {'questions': questions})

def quiz(request):
    questions = Question.objects.all()[:5]

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
            score += 0.6
        elif question.selected_option == "MORE THAN HALF THE DAYS":
            score+=0.2
        else:
            score+=0
            
    # Update user score
    request.user.mental_score = (score / count) * 100.0
    request.user.save()
    context = "You are doing great"
    return render(request, 'results.html',{'context':context})
    # return render(request, 'results.html', {'score': score, 'count': count})

def display_all_patients(request):
    patients = User.objects.filter(role="patient").values('first_name', 'last_name', 'email','date_joined','role','mental_score')
    # print(patients)
    context = {
        'title': 'All Patients',
        'patients': patients
    }
    return render(request, 'accounts/doctor/all-patient.html', context)
