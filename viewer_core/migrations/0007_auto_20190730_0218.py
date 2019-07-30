# Generated by Django 2.2.2 on 2019-07-30 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer_core', '0006_auto_20190725_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='branch',
        ),
        migrations.AlterField(
            model_name='project',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='viewer_core.Project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='students',
            field=models.ManyToManyField(to='viewer_core.Student'),
        ),
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(to='viewer_core.Tag'),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viewer_core.Branch')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='group',
            field=models.ManyToManyField(to='viewer_core.Group'),
        ),
    ]
