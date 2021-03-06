# Generated by Django 2.2.5 on 2019-09-22 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroOp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orcamento', models.IntegerField()),
                ('cliente', models.CharField(max_length=300)),
                ('servico', models.TextField()),
                ('quant', models.DecimalField(decimal_places=0, max_digits=7)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=7)),
                ('entrada', models.DateField()),
                ('vendedor', models.CharField(max_length=100)),
                ('op', models.IntegerField()),
                ('prev_entrega', models.DateTimeField()),
            ],
        ),
    ]
