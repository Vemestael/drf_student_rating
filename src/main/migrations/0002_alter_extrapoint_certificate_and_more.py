# Generated by Django 4.0.6 on 2022-08-02 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrapoint',
            name='certificate',
            field=models.FileField(blank=True, upload_to='certificate'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='extra_score',
            field=models.IntegerField(blank=True, help_text='Student points for additional activity'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='scholarship',
            field=models.IntegerField(blank=True),
        ),
    ]