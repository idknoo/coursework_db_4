# Generated by Django 4.1.4 on 2022-12-22 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('status', models.BooleanField(blank=True, null=True)),
                ('damage_level', models.IntegerField(blank=True, null=True)),
                ('animal', models.ManyToManyField(blank=True, null=True, to='product.animal')),
            ],
        ),
        migrations.CreateModel(
            name='Robot_description',
            fields=[
                ('robot_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='robot.robot')),
                ('size', models.CharField(blank=True, max_length=32, null=True)),
                ('color', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
    ]
