# Generated by Django 3.0.5 on 2020-04-23 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20200421_0303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_post',
            name='posted_by_id',
        ),
        migrations.AlterField(
            model_name='job_post',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='job_post',
            name='maximum_pay',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='job_post',
            name='minimum_pay',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='job_post_activity',
            name='job_post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.job_post'),
        ),
        migrations.AlterField(
            model_name='job_post_activity',
            name='user_account_id',
            field=models.IntegerField(),
        ),
    ]
