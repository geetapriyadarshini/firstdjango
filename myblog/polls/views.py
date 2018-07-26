from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
#SIMPLE MSG
# def index(request):
    # return HttpResponse("Hello. You're at the polls index.")

    			# OR PRINTING WITHOUT TEMPLET , SEPERATED VALUES


# def index(request):
# 	latest_question_list = Question.objects.order_by('-pub_date')[:3]
# 	output = ', '.join([q.question_text for q in latest_question_list])
# 	return HttpResponse(output)
    					

    					# OR USING TEMPLATE LOADER

# def index(request):
# 	latest_question_list = Question.objects.order_by('-pub_date')[:3]
# 	template = loader.get_template('polls/index.html')  #IMPORT TEMPLATE
# 	context = {
# 	'latest_question_list': latest_question_list,
# 	}
# 	return HttpResponse(template.render(context, request))

					# or using render

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)		#IMPORT RENDER			


def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})
	# return HttpResponse("You are looking at question %s." % question_id)

def results(request, question_id):
	response = "You're looking at results of question %s."
	return HttpResponse(response % question_id) 

		




#     def results(request, question_id):
#     	response = "You're looking at the results of question %s."
#     	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)




#     