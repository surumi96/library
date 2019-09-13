from django.shortcuts import render, redirect

# Create your views
def front(request):
    if request.method == 'POST' and 'teacher' in request.POST:
        return redirect('login')
    return render(request, 'front.html', {})
def login(request):
    return render(request, 'login.html', {})
def student(request):
    return render(request, 'student.html', {})