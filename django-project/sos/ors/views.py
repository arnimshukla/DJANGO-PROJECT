from django.http import HttpResponse
from django.shortcuts import render, redirect
from pyexpat.errors import messages

from .Service.UserService import UserService


def third(request):
    return HttpResponse("Hello django this is my second app")


def welcome(request):
    return render(request, 'welcome.html')


def user_signup(request):
    return render(request, 'registration.html')


def user_signup(request):
    if request.method == "POST":
        params = {}
        params['firstName'] = request.POST.get('firstName')
        params['lastName'] = request.POST.get('lastName')
        params['loginId'] = request.POST.get('loginId')
        params['password'] = request.POST.get('password')
        params['dob'] = request.POST.get('dob')
        params['address'] = request.POST.get('address')
        service = UserService()
        service.add(params)
    return render(request, 'registration.html')


def user_signin(request):
    message = ''
    if request.method == "POST":
        if request.POST.get('operation') == "signIn":
            loginId = request.POST.get('loginId')
            password = request.POST.get('password')

            service = UserService()
            user_data = service.auth(loginId, password)
            if len(user_data) != 0:

                request.session['firstName'] = user_data[0].get('firstName')
                return redirect('/ors/welcome/')
            else:
                message = 'ID and Password are invaliud'

        if request.POST.get('operation') == "signUp":
            return redirect('/ors/signup/')

    return render(request, 'login.html', {'message': message})


def test_list(request):
    list = [
        {"id": 1, "firstname": "abc", "lastname": "dsa", "email": "asd@gmail.com", "password": "1234"},
        {"id": 1, "firstname": "abc", "lastname": "dsa", "email": "asd@gmail.com", "password": "1234"},
        {"id": 1, "firstname": "abc", "lastname": "dsa", "email": "asd@gmail.com", "password": "1234"}

    ]
    return render(request, "testlist.html", {"list": list})


def user_logout(request):
    request.session['firstName'] = None
    return redirect('/ors/signin')


def user_list(request):
    params = {}
    params['pageNo'] = 1
    params['pageSize'] = 5
    if request.method == "POST":
        if request.POST['operation'] == "next":
            params['pageNo'] = int(request.POST['pageNo'])
            params['pageNo'] += 1
        if request.POST['operation'] == "previous":
            params['pageNo'] = int(request.POST['pageNo'])
            params['pageNo'] -= 1
        if request.POST['operation'] == "search":
            params['firstName'] = request.POST['firstName']

    service = UserService()
    list = service.search(params)
    index = (params['pageNo'] - 1) * 5
    return render(request, "userlist.html", {"list": list, "index": index, 'pageNo': params['pageNo']})


def delete_user(request, id=0):
    service = UserService()
    service.delete(id)
    return redirect("/ors/list/")


def user_save(request, id=0):
    form = {}
    service = UserService()

    if id > 0:
        user_data = service.get(id)
        user_data[0]['dob'] = user_data[0]['dob'].strftime('%Y-%m-%d')
        form = user_data[0]

    if request.method == "POST":
        params = {}
        params['firstName'] = request.POST.get('firstName')
        params['lastName'] = request.POST.get('lastName')
        params['loginId'] = request.POST.get('loginId')
        params['password'] = request.POST.get('password')
        params['dob'] = request.POST.get('dob')
        params['address'] = request.POST.get('address')

        if request.POST['operation']=="save":
            service.add(params)
        if request.POST['operation']=="update":
            params['id']=id
            service.update(params)
    return render(request,'user.html',{'form':form})

def marksheet_list(request):
    params = {}
    params['pageNo'] = 1
    params['pageSize'] = 5
    if request.method == "POST":
        if request.POST['operation'] == "next":
            params['pageNo'] = int(request.POST['pageNo'])
            params['pageNo'] += 1
        if request.POST['operation'] == "previous":
            params['pageNo'] = int(request.POST['pageNo'])
            params['pageNo'] -= 1
        if request.POST['operation'] == "search":
            params['firstName'] = request.POST['firstName']

    service = UserService()
    list = service.searchMarks(params)
    index = (params['pageNo'] - 1) * 5
    return render(request, "marksheet.html", {"list": list, "index": index, 'pageNo': params['pageNo']})


def marksheet_save(request, id=0):
    form = {}
    service = UserService()

    if id>0:
        user_data = service.getmarkes(id)
        form = user_data[0]


    if request.method == "POST":


        print("POST RECEIVED")
        print(request.POST)
        params = {}
        params['firstName'] = request.POST.get('firstName')
        params['Class'] = request.POST.get('Class')
        params['studentId'] = request.POST.get('studentId')
        params['physics'] = request.POST.get('physics')
        params['chemistry'] = request.POST.get('chemistry')
        params['maths'] = request.POST.get('maths')

        if request.POST['operation']=="save":
            service.addmarksheet(params)
        if request.POST['operation']=="update":
            params['id']=id
            service.updatemarksheet(params)
    return render(request,'addmarksheet.html',{'form':form})