from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Proposal, Task


def home(request):
    return render(request, 'pages/home.html')


def add_proposal(request):
    if request.method == 'GET':
        return render(request, 'pages/add_proposal.html')
    elif request.method == 'POST':
        title = request.POST['title']
        project_description = request.POST['project_description']
        map_id = request.POST['map_id']
        gantt_title = request.POST['gantt_title']
        gantt_date_start = request.POST['gantt_date_start']
        gantt_date_end = request.POST['gantt_date_end']
        proposals = Proposal.objects.create(
            title=title, project_description=project_description, map_id=map_id, gantt_title=gantt_title, gantt_date_start=gantt_date_start, gantt_date_end=gantt_date_end)
        return redirect('add_proposal')


def add_task(request, id):
    if request.method == 'GET':
        add_taskID = Proposal.objects.get(id=id)
        print("This is the task id ", add_taskID)
        return(request, 'pages/add_proposal.html', {"add_taskID":add_taskID})
    elif request.method == 'POST':
        gantt_title = request.POST['gantt_title']
        print("Hello")
        # Task.objects.create(taskItem=gantt_title,task_id=add_taskID).save()
        return redirect('add_proposal')


def delete_task(request, id):
    Task.objects.get(pk=id).delete()
    return HttpResponseRedirect(reverse('add_proposal'))


def proposals(request):
    proposals = Proposal.objects.all()
    context = {
        'proposals': proposals
    }
    return render(request, 'pages/proposals.html', context)


def tasks(request):
    tasks = Task.objects.all()
    context = {
        'tasks': proposals
    }
    return render(request, 'pages/add_proposals.html', context)


def proposal_view(request, id):
    post = Proposal.objects.get(id=id)
    return render(request, 'pages/proposal_view.html', {"post": post})

def see_details(request, id):
    details = Proposal.objects.get(id=id)
    return render(request, 'pages/details.html', {"details": details})

# create details url that has add task/dates