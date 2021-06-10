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
        proposals = Proposal.objects.create(
            title=title, project_description=project_description, map_id=map_id, gantt_title=gantt_title)
        return redirect('add_proposal')


def add_task(request, id):
    if request.method == 'GET':
        tasks = Task.objects.all()
        details = Proposal.objects.get(id=id)
        context = {
            "details": details,
            "tasks": tasks
            }
        return render(request, 'pages/details.html', context)
    elif request.method == 'POST':
        details = Proposal.objects.get(id=id)
        gantt_title = request.POST['gantt_title']
        Task.objects.create(taskItem=gantt_title, task_id=details)
        return render(request, 'pages/details.html', {"details": details})


def delete_task(request, id):
    Task.objects.get(pk=id).delete()
    return render(request, 'pages/details.html', {"details": details})


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