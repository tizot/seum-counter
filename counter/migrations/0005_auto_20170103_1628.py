# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 16:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0004_auto_20161225_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='date et heure')),
            ],
            options={
                'verbose_name': 'like',
                'verbose_name_plural': 'likes',
            },
        ),
        migrations.AlterModelOptions(
            name='counter',
            options={'verbose_name': 'compteur'},
        ),
        migrations.AlterModelOptions(
            name='reset',
            options={'verbose_name': 'remise à zéro', 'verbose_name_plural': 'remises à zéro'},
        ),
        migrations.AlterField(
            model_name='counter',
            name='email',
            field=models.EmailField(default='null@localhost', max_length=264, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='counter',
            name='email_notifications',
            field=models.BooleanField(default=False, verbose_name='notifications par email'),
        ),
        migrations.AlterField(
            model_name='counter',
            name='name',
            field=models.CharField(max_length=60, verbose_name='nom'),
        ),
        migrations.AlterField(
            model_name='counter',
            name='trigramme',
            field=models.CharField(max_length=3, verbose_name='trigramme'),
        ),
        migrations.AlterField(
            model_name='counter',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='utilisateur associé'),
        ),
        migrations.AlterField(
            model_name='reset',
            name='counter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='counter', to='counter.Counter', verbose_name='victime'),
        ),
        migrations.AlterField(
            model_name='reset',
            name='reason',
            field=models.TextField(verbose_name='raison'),
        ),
        migrations.AlterField(
            model_name='reset',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date et heure'),
        ),
        migrations.AlterField(
            model_name='reset',
            name='who',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='who', to='counter.Counter', verbose_name='fouteur de seum'),
        ),
        migrations.AddField(
            model_name='like',
            name='liker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='counter.Counter', verbose_name='likeur'),
        ),
        migrations.AddField(
            model_name='like',
            name='reset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='counter.Reset', verbose_name='seum'),
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set([('liker', 'reset')]),
        ),
    ]
