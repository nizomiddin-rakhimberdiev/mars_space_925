# Generated by Django 5.1.2 on 2024-10-28 12:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('space', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student'),
        ),
        migrations.AddField(
            model_name='bloglike',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='space.blog'),
        ),
        migrations.AddField(
            model_name='bloglike',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student'),
        ),
        migrations.AddField(
            model_name='commentary',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='space.blog'),
        ),
        migrations.AddField(
            model_name='commentary',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student'),
        ),
        migrations.AddField(
            model_name='shop_history',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student'),
        ),
        migrations.AddField(
            model_name='shop_history',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='space.product'),
        ),
    ]
