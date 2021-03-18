# Generated by Django 3.1.6 on 2021-03-14 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creating', models.DateTimeField(auto_now_add=True)),
                ('users', models.ManyToManyField(related_name='my_chats', to=settings.AUTH_USER_MODEL, verbose_name='chat_users')),
            ],
            options={
                'verbose_name': 'Chat',
                'verbose_name_plural': 'Chats',
                'ordering': ['-date_creating'],
            },
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='message')),
                ('date_creating', models.DateTimeField(auto_now_add=True)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_messages', to='Chats.chats', verbose_name='chat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='my_messages', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Chat message',
                'verbose_name_plural': 'Chat messages',
                'ordering': ['date_creating'],
            },
        ),
        migrations.CreateModel(
            name='Chats_admins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creating', models.DateTimeField(auto_now_add=True)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats_admins', to='Chats.chats', verbose_name='chat_admins')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='you_chats_admin', to=settings.AUTH_USER_MODEL, verbose_name='you_admin')),
            ],
            options={
                'verbose_name': 'Chats admin',
                'verbose_name_plural': 'Chats admins',
                'ordering': ['-date_creating'],
                'unique_together': {('chat', 'user')},
            },
        ),
    ]
