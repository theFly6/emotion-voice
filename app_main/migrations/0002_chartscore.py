# Generated by Django 3.2.16 on 2024-02-24 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChartScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=128, verbose_name='词语')),
                ('before_score', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='账户余额')),
                ('during_score', models.IntegerField(verbose_name='疫情中')),
                ('after_score', models.IntegerField(verbose_name='疫情后')),
            ],
        ),
    ]
