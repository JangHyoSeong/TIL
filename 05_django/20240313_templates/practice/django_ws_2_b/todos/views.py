from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'work' : request.GET.get('work'),
    }
    return render(request, 'todos/index.html', context)

def create_todo(request):
    return render(request, 'todos/create_todo.html')