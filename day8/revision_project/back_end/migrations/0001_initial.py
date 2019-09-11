# Generated by Django 2.1.7 on 2019-09-11 11:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=100, verbose_name='Category Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=150, verbose_name='Post Title')),
                ('post_img', models.ImageField(blank=True, null=True, upload_to='uploads/post_img', verbose_name='Post Image')),
                ('create_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('content', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('category', models.ManyToManyField(to='back_end.Category', verbose_name='Categories of Post')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_title', models.CharField(max_length=100)),
                ('service_desc', models.TextField(verbose_name='Service Description')),
            ],
        ),
    ]