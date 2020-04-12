from django.shortcuts import render, redirect

from . import models, forms


# Create your views here.
def index(request):
    pass
    return render(request, 'cardApp/index.html')


def login(request):
    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect('/index/')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = models.User.objects.get(username=username)
            except :
                message = '用户不存在！'
                return render(request, 'cardApp/login.html', locals())

            if user.password == password:
                return redirect('/index/')
            else:
                message = '密码不正确！'
                return render(request, 'cardApp/login.html', locals())
        else:
            return render(request, 'cardApp/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'cardApp/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            card = register_form.cleaned_data.get('card')
            name = register_form.cleaned_data.get('name')
            sex = register_form.cleaned_data.get('sex')
            onlyid = register_form.cleaned_data.get('onlyid')

            #sex = register_form.cleaned_data.get('sex')

            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'cardApp/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(username=username)
                if same_name_user:
                    message = '用户名已经存在'
                    return render(request, 'cardApp/register.html', locals())
                same_card_user = models.User.objects.filter(card=card)
                if same_card_user:
                    message = '该校园卡号已经被注册了！'
                    return render(request, 'cardApp/register.html', locals())

                new_user = models.User()
                new_user.username = username
                new_user.password = password1
                new_user.card = card
                new_user.email = email
                new_user.sex = sex
                new_user.name = name
                new_user.onlyid = onlyid
                new_user.save()

                return redirect('/login/')
        else:
            return render(request, 'cardApp/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'cardApp/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/login/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/login/")