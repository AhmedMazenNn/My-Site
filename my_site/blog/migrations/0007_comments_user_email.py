# Generated by Django 5.0.1 on 2024-03-08 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='user_email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
