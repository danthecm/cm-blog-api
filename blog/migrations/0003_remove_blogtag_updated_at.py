# Generated by Django 4.0.5 on 2022-07-01 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_title_alter_blogtag_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogtag',
            name='updated_at',
        ),
    ]
