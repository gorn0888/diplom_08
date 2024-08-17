# Generated by Django 5.0.7 on 2024-08-13 08:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='категория')),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=40, null=True, verbose_name='подразделение')),
                ('address', models.CharField(blank=True, max_length=240, null=True, verbose_name='адрес')),
                ('title_into_chaos', models.CharField(blank=True, max_length=160, null=True, verbose_name='название в запрос')),
                ('outgoing', models.CharField(blank=True, max_length=16, null=True, verbose_name='исходящий')),
                ('coming_from', models.DateField(blank=True, default='2024-01-01', null=True, verbose_name='исходящий от')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_card', models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='images/', verbose_name='фотокарточка')),
                ('personal_number', models.CharField(blank=True, max_length=9, null=True, verbose_name='личный номер')),
                ('last_name', models.CharField(max_length=16, verbose_name='фамилия')),
                ('first_name', models.CharField(max_length=24, verbose_name='имя')),
                ('patronymic', models.CharField(blank=True, max_length=24, verbose_name='отчество')),
                ('date_of_birth', models.DateField(default='1983-08-08', verbose_name='дата рождения')),
                ('sex', models.CharField(choices=[('мужской', 'мужской'), ('женский', 'женский')], default='мужской', max_length=8, verbose_name='пол')),
                ('category', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, related_name='person_category', to='app.category')),
                ('division', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, related_name='person_division', to='app.division')),
            ],
        ),
    ]
