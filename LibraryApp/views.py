from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Sum
from .models import User
from .models import Book
from .models import Order
from datetime import date



# Create your views
def form(request):
    if request.method == 'POST':
        username = request.POST.get("uname")
        studclass = request.POST.get("studclass")
        emailid = request.POST.get("email")
        fine = request.POST.get("fine")
        password = request.POST.get("password")
        confirm_password = request.POST.get("psw")
        if password == confirm_password:
            user = User.objects.create_user(username=username,studclass=studclass, email=emailid, fine=fine, password=password)
            user.save()
            return redirect('login')
    return render(request, 'form.html', {})


def front(request):
    return render(request, 'front.html', {})


# def adminlogin(request):
#     if request.method == 'POST':
#         username = request.POST.get("Username")
#         password = request.POST.get("pass")
#         user = authenticate(username=username,password=password)
#         if user is None:
#             print("user not exist")
#         else:
#             login(request, user)
#             if user.is_staff:
#                 return redirect('admin')
#             else:
#                 return redirect('studentadmin')
#
#     return render(request, 'adminlogin.html', {})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("Username")
        password = request.POST.get("pass")
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is None:
            print("user not exist")
        else:
            login(request, user)
            if user.is_staff:
                return redirect('admin')
            else:
                return redirect('studentadmin')
    return render(request, 'login.html', {})


def admin(request):
    if request.method == 'POST' and 'logout' in request.POST:
        return redirect('logout')
    return render(request, 'admin.html', {})


def student(request):
    obj = User.objects.filter(is_staff=False)
    if request.method == 'POST' and 'delete' in request.POST:
        idd = request.POST.get('delete')
        print(idd)
        ob = User.objects.get(id=idd)
        ob.delete()
    return render(request, 'student.html', {'key': obj})


def book(request):
    obj=Book.objects.all()
    if request.method == 'POST' and 'add' in request.POST:
        return redirect('bookform')
    if request.method == 'POST' and 'delete' in request.POST:
        idd =request.POST.get('delete')
        ob = Book.objects.get(id=idd)
        ob.delete()
    return render(request, 'book.html', {'key':obj})


def search(request):
    obj = Book.objects.filter(BookName= request.POST.get("bname"), Number__gt=0)
    return render(request, 'search.html', {'key': obj})


def order(request):
    fine=0
    today=date.today()
    msg=''
    ob=Order.objects.filter(returndate=None)
    if request.method == 'POST':
        if 'issue' in request.POST:
            username = request.POST.get("username")
            BookName = request.POST.get("bookname")
            username=User.objects.get(username=username)
            BookName=Book.objects.get(BookName=BookName)
            t=Order.objects.filter(username=username, returndate=None)
            s=Order.objects.filter(returndate=None, BookName=BookName, username=username)
            if BookName.Number > 0:
                if len(t) < 2 and len(s) == 0:
                    obj=Order()
                    obj.username=username
                    obj.BookName=BookName
                    obj.save()
                    BookName.Number -= 1
                    BookName.save()
            else:
                msg="not available"

        if 'return' in request.POST:
            username = request.POST.get("username")
            BookName = request.POST.get("bookname")
            username = User.objects.get(username=username)
            BookName = Book.objects.get(BookName=BookName)
            obj = Order.objects.filter(username=username, BookName=BookName)

            for i in obj:
                i.returndate = today
                delay=i.returndate-i.issuedate
                if delay.days > 15:
                    fine=fine+0.50
                else:
                    fine=0
                i.fine=fine
                i.save()


            BookName.Number += 1
            BookName.save()
        # obj=Order.objects.filter(username=username, BookName=BookName)
    return render(request, 'order.html',{'key': ob,'key1' :msg})

#

def history(request):
    obj=Order.objects.exclude(returndate=None)

        #today = date.today()
    return render(request, 'history.html',{'key': obj})


def fine(request):
    obj=Order.objects.exclude(returndate =None)
    return render(request, 'fine.html',{'key':obj})


def edit(request,id):
    obj = User.objects.get(id=id)
    if request.method == 'POST':
        username = request.POST.get("username")
        obj.username = username
        studclass = request.POST.get("studclass")
        obj.studclass = studclass
        email =request.POST.get("email")
        obj.email=email
        fine = request.POST.get("fine")
        obj.fine = fine
        obj.save()
        return redirect('student')
    return render(request, 'edit.html', {'key': obj})


def bookform(request):
    if request.method == 'POST':
        BookName = request.POST.get("bookname")
        AuthorName = request.POST.get("authorname")
        Number = request.POST.get("number")
        print(BookName, AuthorName, Number)
        book =Book.objects.create(BookName=BookName,AuthorName=AuthorName,Number=Number)
        book.save()
        return redirect("book")
    return render(request, 'bookform.html', {})


def editbook(request,id):
    obj = Book.objects.get(id=id)
    if request.method == 'POST':
        BookName = request.POST.get("bookname")
        obj.BookName = BookName
        AuthorName=request.POST.get("authorname")
        obj.AuthorName = AuthorName
        Number =request.POST.get("number")
        obj.Number =Number
        obj.save()
        return redirect('book')
    return render(request, 'editbook.html', {})


def log_out(request):
    logout(request)
    return redirect('login')


def studentadmin(request):
    return render(request, 'studentadmin.html', {})


def bookavailable(request):
    obj = Book.objects.all()
    return render(request, 'bookavailable.html', {'key':obj})