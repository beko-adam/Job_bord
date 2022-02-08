from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect

from .models import  Job, Apply
from django.core.paginator import Paginator
from .forms import Apply_form, jobsss

# Create your views here.

def job_list(request):

    job_lists = Job.objects.all()
    
    i = 0
    for n in job_lists:
        
        i += 1
        
    print(i)
    paginator = Paginator(job_lists, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs': page_obj, 'job_avl':i}

    return render(request, './job/jobs.html', context)





def job_detail(request, slug):


    job_lists = Job.objects.get(slug=slug)

    if request.method == 'POST':

        form_Apply = Apply_form(request.POST, request.FILES)
        if form_Apply.is_valid():
            form = form_Apply.save(commit=False)
            form.job_link = job_lists
            form.save()

        print('done')

    else:

        form_Apply = Apply_form()

        print('done2')

    context = {'job_details': job_lists, 'form_Apply':form_Apply}

    return render(request, './job/job_details.html', context)


 

def get_form(request):

    if request.method == 'POST':

        form = jobsss(request.POST, request.FILES)

        if form.is_valid():

            form.save()
            return redirect('/')

        print('done')

    else:

        form = jobsss()


    context = {

        'form': form ,
    }

    return render(request, './job/test_form.html', context)

    