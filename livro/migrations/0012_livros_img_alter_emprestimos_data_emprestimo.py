# Generated by Django 4.1.1 on 2022-10-27 03:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0011_alter_emprestimos_data_emprestimo'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='capa_livro'),
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 27, 0, 58, 14, 748732)),
        ),
    ]