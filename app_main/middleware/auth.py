from django.middleware.common import CommonMiddleware
from django.shortcuts import redirect


class LoginMiddleWare(CommonMiddleware):
    def process_request(self, request):
        except_lst = ['/account/login', '/account/image/code']
        if request.session.get('info') is None and request.path not in except_lst:
            return redirect('/account/login')
        # print('当前用户：', request.session.get('info'), request.session.session_key)
        # print(dict(request.session))

    def process_response(self, request, response):
        return response
