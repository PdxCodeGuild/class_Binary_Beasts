from django.shortcuts import render,redirect
from .models import Todo, Author

def todo_list(request):
    todos = Todo.objects.all()  # get all of the todos from the database and store them in todos

    todo = Todo.objects.get(id = 1)
    print('AUTHOR SET FOREIGNKEY', todo.author_set.all())
    
    authors = Author.objects.get(id = 1)
    print('ORDER SET FOREIGNKEY', authors.task_set.all())
    # create the context dictionary to send the todos to the template
    context = {
        'todos': todos
    }

    return render(request, 'todos/todo_list.html', context) # context is sent to 'todos/list.html'

