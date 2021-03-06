# Generated by Django 3.1 on 2020-08-30 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('description', models.TextField(null=True)),
                ('color', models.CharField(max_length=30, null=True)),
                ('size', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], max_length=20, null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('price', models.FloatField(max_length=10, null=True)),
            ],
        ),
    ]
