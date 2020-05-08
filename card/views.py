import os

import pandas as pd
from django.shortcuts import render, redirect
from card.page import Pagination
from . import models, forms

# Create your views here.

#txt的文件路径;
data_path = os.path.join(os.path.dirname(__file__), 'test')
def index(request):
    # with open(data_path, 'r', encoding='utf-8') as f:
    #     content = f.readline()
    username = request.session.get("username")
    listdata = models.User.objects.filter(username=username)
    data = models.Cardmoney.objects.first()

    return render(request, 'cardApp/index.html', locals())
def cardtest(request):
    username = request.session.get("username")
    listinfo = models.User.objects.filter(username=username)
    cardlist = models.Cardmoney.objects.filter(username=username)
    print(username)
    if request.method == 'POST' and request.POST:
        card_form = forms.CardForm(request.POST)
        message = "请检查填写的内容！"
        if card_form.is_valid():
            consume = card_form.cleaned_data.get('consume_money')
            rest = card_form.cleaned_data.get('rest_money')
            card_table = models.Cardmoney()  # 实例化一个对象
            print("************************")
            print(rest, consume)
            card_table.consume_money = consume
            card_table.rest_money = rest
            for item in listinfo:
                card_table.card = item.card
                card_table.username = username
                card_table.cardnum_id = item.id
            card_table.save()
            return redirect('/index/')
    else:
        card_form = forms.CardForm()

    # 获取当前页
    current_page = request.GET.get('p')
    # 创建对象传入值 199总数
    page_obj = Pagination(199, current_page)
    # 切片传入值
    USER_LIST = models.Cardmoney.objects.filter(username=username)
    data_list = USER_LIST[page_obj.start():page_obj.end()]
    return render(request, 'cardApp/cardtest.html', locals())
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
                request.session['username'] = username
                return redirect('/index/')
            else:
                message = '密码不正确！'
                return render(request, 'cardApp/login.html', locals())
        else:
            return render(request, 'cardApp/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'cardApp/login.html', locals())


def register(request):
    with open(data_path, 'r', encoding='utf-8') as f:
        content = f.readline()
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
                new_user.card = content
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

