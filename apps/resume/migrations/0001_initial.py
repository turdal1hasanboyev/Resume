# Generated by Django 5.0.6 on 2024-06-05 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AWARDS_CERTIFICATIONS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('awards_certifications', models.CharField(blank=True, max_length=225, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EDUCATION',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(blank=True, max_length=225, null=True)),
                ('educational_category', models.CharField(blank=True, max_length=225, null=True)),
                ('educational_direction', models.CharField(blank=True, max_length=225, null=True)),
                ('educational_period', models.CharField(blank=True, max_length=225, null=True)),
                ('gpa', models.CharField(blank=True, max_length=225, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EXPERIENCE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.CharField(blank=True, max_length=225, null=True)),
                ('working_period', models.CharField(blank=True, max_length=225, null=True)),
                ('problem', models.CharField(blank=True, max_length=225, null=True)),
                ('solution', models.CharField(blank=True, max_length=225, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='INTERESTS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interests', models.CharField(blank=True, max_length=225, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SKILLS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_flow', models.CharField(blank=True, max_length=225, null=True)),
            ],
        ),
    ]
