# Generated by Django 3.1.4 on 2020-12-07 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0019_doctor_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='cnews',
            name='i_active',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cnews',
            name='i_death',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cnews',
            name='i_recoverd',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cnews',
            name='india',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cnews',
            name='w_active',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cnews',
            name='w_death',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cnews',
            name='w_recoverd',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cnews',
            name='world',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
