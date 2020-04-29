from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "用户名",'autofocus': ''}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': "密码"}))


class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'用户名'}), )
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': "密码",'autofocus': ''}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "确认密码",'autofocus': ''}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': "邮箱地址",'autofocus': ''}))
    card = forms.CharField(label="校园卡号", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': "校园卡号",'autofocus': ''}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    name = forms.CharField(label="姓名", max_length=20,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': "真实姓名",'autofocus': ''}))
    onlyid = forms.CharField(label="身份证号码", max_length=20,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "身份证号",'autofocus': ''}))

class CardForm(forms.Form):
    consume_time = forms.DateField(widget=forms.DateInput(attrs={'type':'date' , 'name': 'time'}))
    rest_money = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'剩余金额' , 'name' : 'rest_money'}), )
    consume_money = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'消费金额', 'name' : 'consume_money'}), )