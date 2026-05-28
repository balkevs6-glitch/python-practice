import json
import os

from django.shortcuts import redirect, render

def home(request):
    return render(request, 'quiz/home.html')

def quiz_page(request):
    return render(request, 'quiz/quiz.html')

def easy_level(request):
    return render(request, 'quiz/easy.html')

def medium_level(request):
    return render(request, 'quiz/medium.html')

def hard_level(request):
    return render(request, 'quiz/hard.html')

def leaderboard(request):

    file_path = os.path.join(os.path.dirname(__file__), 'data', 'rank.json')

    try:
        with open(file_path, 'r') as file:
            scores = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        scores = []

    return render(request, 'quiz/leader.html', {'scores': scores})

def student_id(request):
    if request.method == 'POST':
        name = request.POST.get('student_id')
        if name:
            request.session['student_id'] = name
            return redirect('quiz')
    return render(request, 'quiz/student_id.html')