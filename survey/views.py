from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Candidate

def index(request):
    candidates = Candidate.objects.all()
    context = {
        'candidates': candidates,
    }
    return render(request, 'survey/survey.html', context)

def vote(request,vote_id):
    candidate = Candidate.objects.get(pk=vote_id)

    if (candidate.vote == 0 ):
        candidate.vote = 1
    else:
        candidate.vote += 1

    return HttpResponseRedirect("/survey/results")

def result(request):
    candidates = Candidate.objects.all()
    context = {
        'candidates': candidates
    }

    return render(request, 'survey/result.html', context)
