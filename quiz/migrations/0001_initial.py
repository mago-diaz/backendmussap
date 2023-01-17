# Generated by Django 4.1.2 on 2023-01-17 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnsweredQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_obtained', models.IntegerField()),
                ('comments', models.TextField(blank=True)),
                ('quiz_grade', models.DecimalField(decimal_places=2, max_digits=3)),
                ('time_left', models.IntegerField()),
                ('is_checked', models.BooleanField(default=False)),
                ('create_by_teacher', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('ended_date', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_ended', models.BooleanField(default=False)),
                ('total_score', models.IntegerField()),
                ('min_quiz_grade', models.DecimalField(decimal_places=2, max_digits=3)),
                ('aprobal_quiz_grade', models.DecimalField(decimal_places=2, max_digits=3)),
                ('max_quiz_grade', models.DecimalField(decimal_places=2, max_digits=3)),
                ('scale', models.DecimalField(decimal_places=2, max_digits=3)),
                ('ended_time', models.IntegerField()),
                ('number_of_questions', models.IntegerField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_manager.subject')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_manager.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='WrittingQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('question', models.TextField(max_length=500)),
                ('score', models.IntegerField()),
                ('rubric', models.TextField(blank=True)),
                ('quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TOFQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('question', models.TextField(max_length=500)),
                ('score', models.IntegerField()),
                ('correct_answer', models.BooleanField()),
                ('quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SelectionQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('question', models.TextField(max_length=500)),
                ('correct_answer', models.CharField(max_length=255)),
                ('score', models.IntegerField()),
                ('options', models.JSONField()),
                ('quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PianoQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('question', models.TextField(max_length=500)),
                ('score', models.IntegerField()),
                ('visiblepiano', models.BooleanField(default=True)),
                ('rubric', models.TextField(blank=True)),
                ('quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MusicSheetQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('question', models.TextField(max_length=500)),
                ('score', models.IntegerField()),
                ('rubric', models.TextField(blank=True)),
                ('quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnsweredWrittingQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(blank=True)),
                ('score', models.IntegerField()),
                ('answer', models.TextField(blank=True, max_length=500)),
                ('answered_quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.answeredquiz')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.writtingquestion')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnsweredTOFQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(blank=True)),
                ('score', models.IntegerField()),
                ('answer', models.CharField(blank=True, max_length=255)),
                ('answered_quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.answeredquiz')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.tofquestion')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnsweredSelectionQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(blank=True)),
                ('score', models.IntegerField()),
                ('answer', models.CharField(blank=True, max_length=255)),
                ('answered_quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.answeredquiz')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.selectionquestion')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='answeredquiz',
            name='quiz_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz'),
        ),
        migrations.AddField(
            model_name='answeredquiz',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_manager.student'),
        ),
        migrations.AddField(
            model_name='answeredquiz',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_manager.subject'),
        ),
        migrations.CreateModel(
            name='AnsweredPianoQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(blank=True)),
                ('score', models.IntegerField()),
                ('answer', models.JSONField()),
                ('answered_quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.answeredquiz')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.pianoquestion')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnsweredMusicSheetQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(blank=True)),
                ('score', models.IntegerField()),
                ('answer', models.JSONField()),
                ('answered_quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.answeredquiz')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.musicsheetquestion')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
