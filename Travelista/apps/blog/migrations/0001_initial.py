# Generated by Django 4.2.9 on 2024-02-02 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='blog_media/default.jpg', upload_to='blog_media/', verbose_name='Image')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(allow_unicode=True, max_length=255, unique_for_date='published_date', verbose_name='Slug')),
                ('content', models.TextField(verbose_name='Content')),
                ('counted_views', models.IntegerField(default=0, verbose_name='Counted Views')),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Published', 'Published')], default='Draft', max_length=15, verbose_name='Status')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='Publish Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(to='blog.category')),
                ('tag', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tag')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ('-published_date',),
            },
            managers=[
                ('posts', django.db.models.manager.Manager()),
            ],
        ),
    ]
