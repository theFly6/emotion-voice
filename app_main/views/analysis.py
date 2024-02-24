from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from app_main.utils.transutil import trans_word_fromA2B


def show(request):
    return render(request, 'analysis.html')


def get_trans_result(request):
    lang_map = {
        '中文（简体）': 'zh',
        '英语': 'en'
    }
    from_lang = lang_map[request.GET.get('from_lang')]
    to_lang = lang_map[request.GET.get('to_lang')]
    word = request.GET.get('word')
    trans_result = trans_word_fromA2B(from_lang, to_lang, word)
    data_dict = {
        'status': True,
        'trans_result': trans_result
    }
    return JsonResponse(data_dict, json_dumps_params={'ensure_ascii': False})

