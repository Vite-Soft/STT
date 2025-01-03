# Generated by Django 5.0.2 on 2024-03-02 18:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_file_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=3, unique=True, verbose_name='Til')),
            ],
            options={
                'verbose_name_plural': 'Tillar',
                'ordering': ['language'],
            },
        ),
        migrations.AlterModelOptions(
            name='file',
            options={'ordering': ['file'], 'verbose_name_plural': 'Fayllar'},
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='', verbose_name='Fayl'),
        ),
        migrations.AddField(
            model_name='file',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.language'),
        ),
    ]
