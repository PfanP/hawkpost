# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boxes', '0006_auto_20160429_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(10, 'On Queue'), (20, 'Sent'), (30, 'Failed')], default=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sent_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='box',
            name='max_messages',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='box',
            name='never_expires',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='box',
            name='expires_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='box',
            name='status',
            field=models.IntegerField(choices=[(10, 'Open'), (20, 'Expired'), (30, 'Done'), (40, 'Closed')], default=10),
        ),
        migrations.AddField(
            model_name='message',
            name='box',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='boxes.Box'),
        ),
    ]
