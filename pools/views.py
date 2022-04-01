from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.utils import timezone

from pools.models import Question, Choice


class IndexView(View):
    def get(self, request):
        questions_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

        return render(request, 'pools/index.html', context={"questions_list": questions_list})


class DetailView(View):
    def get(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)

        return render(request, 'pools/detail.html', context={"question": question})


class ResultsView(View):
    def get(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)

        return render(request, 'pools/results.html', context={"question": question})


class VoteView(View):
    def post(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)

        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'pools/detail.html', context={'question': question,
                                                                 'error_message': 'You did not select a choice!'})

        else:
            # Race Condition
            selected_choice.votes += 1
            selected_choice.save()

        return HttpResponseRedirect(reverse('pools:results', args=(question_id,)))
