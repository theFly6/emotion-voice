"""
自定义的分页组件
用法：
def pretty_lst(request):
    from app01.utils.pagination import Pagination
    pagination = Pagination(request, queryset, page_size=15)
    page_html = pagination.html()
    content = {
        'data_lst': pagination.page_queryset,
        'search_word': search_word,
        'page_li_str': mark_safe(page_html)
    }
    return render(request, 'pretty_list.html', content)

模板.html文件
<ul class="pagination">
    {{ page_li_str }}
</ul>
"""


class Pagination:
    def __init__(self, request, queryset, page_size=10):
        """
        :param request: 请求的对象
        :param queryset: 符号条件的数据
        :param page_size: 每页的页数
        """
        self.request = request
        self.queryset = queryset
        self.page = int(request.GET.get('page', '0'))
        self.start_page = self.page * page_size
        self.page_queryset = queryset[self.start_page: self.start_page + page_size]

    def html(self):
        page_li_str = ''

        for i in range(max(self.page - 5, 0), self.page + 5 + 1):
            if i == self.page:
                page_li_str += f'<li class="active"><a href="?page={i}">{i + 1}</a></li>'
            else:
                page_li_str += f'<li><a href="?page={i}">{i + 1}</a></li>'
        return page_li_str
