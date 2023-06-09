# Generated by Django 4.1.7 on 2023-03-20 11:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_alter_post_options_alter_post_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogs.post')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
