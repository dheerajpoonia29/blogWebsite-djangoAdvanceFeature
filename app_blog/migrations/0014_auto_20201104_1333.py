# Generated by Django 3.1.2 on 2020-11-04 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0013_auto_20201104_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='rating_id',
        ),
        migrations.AddField(
            model_name='blog',
            name='rating_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_blog.rating'),
        ),
    ]