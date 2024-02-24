"""EmotionVoice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from app_main.views import account, index, analysis, hots, talking, about

urlpatterns = [
    # 首页
    path('', index.show),
    path('index', index.show),

    # 用户登录、退出
    path('account/login', account.login),
    path('account/logout', account.logout),
    path('account/image/code', account.image_code),

    # 情感分析
    path('analysis', analysis.show),
    path('analysis/gettrans', analysis.get_trans_result),
    path('analysis/line', analysis.line_data),

    # 热点资讯
    path('hots', hots.show),

    # 讨论投稿
    path('talking', talking.show),

    # 关于我们
    path('about', about.show),

]
