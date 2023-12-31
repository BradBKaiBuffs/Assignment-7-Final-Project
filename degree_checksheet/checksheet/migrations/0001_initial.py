# Generated by Django 4.2.4 on 2023-11-03 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=20)),
                ('course_title', models.CharField(max_length=60)),
                ('course_desc', models.CharField(default='None', max_length=60)),
                ('credit_hours', models.IntegerField(default=3)),
                ('prerequisite', models.BooleanField(default=False)),
                ('semester', models.CharField(default='TBD', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('major_id', models.AutoField(primary_key=True, serialize=False)),
                ('major_name', models.CharField(max_length=60)),
                ('total_hours', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('requirement_id', models.AutoField(primary_key=True, serialize=False)),
                ('req_type', models.CharField(max_length=60)),
                ('req_desc', models.CharField(max_length=60)),
                ('req_hours', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('wt_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Major_selection',
            fields=[
                ('majorsel_id', models.AutoField(primary_key=True, serialize=False)),
                ('selection_date', models.DateTimeField(auto_now_add=True)),
                ('major_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checksheet.major')),
                ('wt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checksheet.student')),
            ],
        ),
        migrations.CreateModel(
            name='Major_requirement',
            fields=[
                ('majorreq_id', models.AutoField(primary_key=True, serialize=False)),
                ('major_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checksheet.major')),
                ('requirement_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checksheet.requirement')),
            ],
        ),
        migrations.CreateModel(
            name='Enroll',
            fields=[
                ('enroll_id', models.AutoField(primary_key=True, serialize=False)),
                ('enroll_date', models.DateTimeField(auto_now_add=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checksheet.course')),
                ('wt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checksheet.student')),
            ],
        ),
        migrations.CreateModel(
            name='Course_requirement',
            fields=[
                ('coursereq_id', models.AutoField(primary_key=True, serialize=False)),
                ('recommended', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], max_length=3)),
                ('lang_equiv', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], max_length=3)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checksheet.course')),
                ('requirement_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checksheet.requirement')),
            ],
        ),
    ]
