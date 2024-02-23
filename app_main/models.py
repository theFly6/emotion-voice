from django.db import models


# Create your models here.
class Admin(models.Model):
    """ 管理员 """
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)

    def __str__(self):
        return self.username


if not Admin.objects.filter(username='admin').exists():
    Admin.objects.create(username='admin',
                         password='ecdc80b866bef369eb57302124b2ff07')
