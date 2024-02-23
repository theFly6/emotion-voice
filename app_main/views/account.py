from django import forms
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect

from app_main.models import Admin
from app_main.utils.code import check_code
from app_main.utils.encrypt import md5


class LoginForm(forms.Form):
    username = forms.CharField(
        label='用户名',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,  # 默认值不为空
    )
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}, render_value=True),
        required=True,  # 默认值不为空
    )
    code = forms.CharField(
        label='验证码',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,  # 默认值不为空
    )

    def clean_password(self):
        user = self.cleaned_data.get('username')
        pwd_md5 = md5(self.cleaned_data.get('password'))
        print(pwd_md5)
        print(md5(('123')))
        if not Admin.objects.filter(username=user, password=pwd_md5).exists():
            raise ValidationError('账号或密码错误')
        return pwd_md5


def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    form = LoginForm(data=request.POST)
    input_code = request.POST.get('code', '')
    right_code = request.session.get('image_code')
    if right_code is None or input_code.upper() != right_code.upper():
        form.add_error('code', '验证码错误')

    if form.is_valid():
        username = form.cleaned_data.get('username')
        u_id = Admin.objects.filter(username=username).first().id
        request.session['info'] = {
            'id': u_id,
            'username': username,
        }
        # 登录有限时限30分钟/30分钟自动退出
        request.session.set_expiry(60 * 30)
        return redirect('/admin/list')
    return render(request, 'login.html', {'form': form})


def logout(request):
    request.session.clear()
    return redirect('/account/login')


def image_code(request):
    img, code_str = check_code()
    request.session['image_code'] = code_str
    request.session.set_expiry(60)
    response = HttpResponse(content_type='png')
    img.save(response, 'png')
    print('code:', code_str)
    return response
