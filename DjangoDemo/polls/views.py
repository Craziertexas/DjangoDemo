from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.views import generic



'''
def index(request):
    question = Question.objects.all()
    return render(request, 'polls/index.html', {"question": question})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {"question": question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {"question": question}) 
'''

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'question'

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")

class DetailView(generic.DetailView):
    template_name = 'polls/detail.html'
    model = Question

class ResultView(generic.DetailView):
    template_name = 'polls/results.html'
    model = Question
    
def vote(request, pk):
    question = get_object_or_404(Question, id=pk)
    try:
        selected_choice = question.choice_set.get(pk = request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {"question": question, "error_message": "No elegiste una respuesta"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))