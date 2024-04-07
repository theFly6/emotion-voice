from django.db import models


# Create your models here.
class Admin(models.Model):
    """ 管理员 """
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)

    def __str__(self):
        return self.username


class ChartScore(models.Model):
    """ 图表分值表 """
    word = models.CharField(verbose_name='词语', max_length=128)
    before_score = models.DecimalField(verbose_name='疫情前', max_digits=6, decimal_places=3, default=0)
    during_score = models.DecimalField(verbose_name='疫情中', max_digits=6, decimal_places=3, default=0)
    after_score = models.DecimalField(verbose_name='疫情后', max_digits=6, decimal_places=3, default=0)

try:
    if not Admin.objects.filter(username='admin').exists():
        Admin.objects.create(username='admin',
                            password='ecdc80b866bef369eb57302124b2ff07')

    to_insert = {
        '快递小哥': (4.11, 3.73, 2.78),
        'Delivery guy': (0.192, 0.206, 0.173),
        'deliver man': (0.192, 0.206, 0.173),
        '返乡': (6.08, 7.26, 8.59),
        'return home': (0.282, 0.238, 0.199),
        'homecoming': (0.282, 0.238, 0.199),
        '戴口罩': (-0.56, 1.37, 1.31),
        'wear a mask': (0.151, 0.130, 0.023),
        'mask': (0.151, 0.130, 0.023),
        '网课': (5.38, 3.86, 3.54),
        'online classes': (0.293, 0.211, 0.268),
        'online courses': (0.293, 0.211, 0.268),
        '居家': (7.14, 7.2, 4.97),
        'stay at home': (0.178, 0.037, 0.121),
    }

    for index, (word, score) in enumerate(to_insert.items()):
        if index % 3:
            score = [c * 10 for c in score]
        if not ChartScore.objects.filter(word=word).exists():
            ChartScore.objects.create(
                word=word,
                before_score=score[0],
                during_score=score[1],
                after_score=score[2]
            )
except Exception as e:
    print('@@@@@出现此提示无需惊慌')
    print('@@@@@如果你正在执行python manage.py makemigrations,则忽略此信息')
    print('@@@@@如果你正在执行python manage.py migrate, 请你再次执行此命令')
    print('@@@@@执行完上述指令后最终执行python manage.py runserve 8080')
    print('@@@@@即可成功运行项目(账号Admin,密码123)')
    
