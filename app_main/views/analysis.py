from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from app_main.models import ChartScore
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


def line_data(request):
    print(request.GET)
    from_word = request.GET.get('from_word')
    from_data = ChartScore.objects.filter(word=from_word).first()
    to_word = request.GET.get('to_word')
    to_data = ChartScore.objects.filter(word=to_word).first()
    res = {
        'status': True,
        'data': [from_word, to_word],
        'series': [
            {
                'name': from_word,
                'type': 'line',
                'stack': 'Total',
                'data': [from_data.before_score, from_data.during_score, from_data.after_score]
            },
            {
                'name': to_word,
                'type': 'line',
                'stack': 'Total',
                'data': [to_data.before_score, to_data.during_score, to_data.after_score]
            }
        ]
    }
    return JsonResponse(res, json_dumps_params={'ensure_ascii': False})
