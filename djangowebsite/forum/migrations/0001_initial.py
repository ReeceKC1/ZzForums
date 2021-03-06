# Generated by Django 2.2.1 on 2019-09-03 02:19

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(max_length=100, primary_key=True, serialize=False)),
                ('poster', models.CharField(max_length=32)),
                ('postid', models.IntegerField()),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(max_length=100, primary_key=True, serialize=False)),
                ('poster', models.CharField(max_length=32)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='post_image')),
                ('content', models.TextField(blank=True, default='')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('rating', models.IntegerField()),
                ('tags', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(max_length=100, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=32)),
                ('contentid', models.IntegerField(default=0)),
                ('contentposter', models.CharField(max_length=32)),
                ('rate', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ForumUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('isadmin', models.BooleanField(default=False)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_image')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
