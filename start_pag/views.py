from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect

from job.models import  Job, Apply
from django.core.paginator import Paginator
# Create your views here.

# Create your views here.


def Home(request):

    job_lists = Job.objects.all()
    
    i = 0
    for n in job_lists:
        
        i += 1
    print(i)
    paginator = Paginator(job_lists, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs': page_obj, 'job_avl':i}


    return render(request, 'kkk/index.html', context)