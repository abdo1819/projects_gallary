# Generated by Django 2.2.2 on 2019-07-25 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer_core', '0004_auto_20190725_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instractor',
            name='project',
        ),
        migrations.RemoveField(
            model_name='student',
            name='project',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='instractors',
            field=models.ManyToManyField(to='viewer_core.Instractor'),
        ),
        migrations.AddField(
            model_name='project',
            name='students',
            field=models.ManyToManyField(to='viewer_core.Student'),
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(to='viewer_core.Tag'),
        ),
        migrations.AlterField(
            model_name='instractor',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='img/instractor/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='viewer_core.Project'),
        ),
        migrations.AlterField(
            model_name='student',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='img/student/'),
        ),
    ]
