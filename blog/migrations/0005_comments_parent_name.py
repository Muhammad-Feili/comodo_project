# Generated by Django 2.2.5 on 2019-10-03 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comments_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='parent_name',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
