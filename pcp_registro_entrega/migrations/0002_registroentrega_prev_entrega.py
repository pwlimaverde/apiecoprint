# Generated by Django 2.2.5 on 2019-09-23 02:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pcp_registro_entrega', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registroentrega',
            name='prev_entrega',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
