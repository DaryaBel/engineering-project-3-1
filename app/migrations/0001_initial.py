# Generated by Django 3.1.4 on 2021-01-03 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('location', models.TextField(verbose_name='Место проведения')),
                ('description', models.TextField(verbose_name='Описание')),
                ('date', models.DateField(verbose_name='Дата проведения')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
        migrations.CreateModel(
            name='Faculties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название факультета')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Факультет',
                'verbose_name_plural': 'Факультеты',
            },
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeName', models.CharField(max_length=50, verbose_name='Номер группы')),
                ('course', models.PositiveIntegerField(verbose_name='Курс')),
                ('formEducation', models.CharField(help_text='(очная/заочная/очно-заочная)', max_length=100, verbose_name='Форма обучения')),
                ('studyDegree', models.CharField(help_text='например, бакалавриат', max_length=160, verbose_name='Ступень высшего образования')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('dateStart', models.DateField(verbose_name='Дата начала работы над проектом')),
                ('dateEnd', models.DateField(verbose_name='Дата окончания работ над проектом')),
                ('links', models.JSONField(verbose_name='Список ссылок')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=160, verbose_name='ФИО')),
                ('birtdate', models.DateField(verbose_name='Дата рождения')),
                ('phone', models.CharField(max_length=50, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('budgetary', models.BooleanField(default=False, verbose_name='Бюджетное обучение')),
                ('groupId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.groups')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
        ),
        migrations.CreateModel(
            name='Universities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=150, verbose_name='Полное название')),
                ('shortname', models.CharField(max_length=100, verbose_name='Краткое название или аббревиатура')),
                ('location', models.TextField(verbose_name='Адрес')),
                ('description', models.TextField(verbose_name='Описание')),
                ('phone', models.CharField(max_length=50, verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Университет',
                'verbose_name_plural': 'Университеты',
            },
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('projectId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.projects')),
            ],
            options={
                'verbose_name': 'Команда',
                'verbose_name_plural': 'Команды',
            },
        ),
        migrations.CreateModel(
            name='StudentsInTeams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.students')),
                ('teamId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.teams')),
            ],
            options={
                'verbose_name': 'Студент в командах',
                'verbose_name_plural': 'Студенты в командах',
            },
        ),
        migrations.CreateModel(
            name='StudentsInEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(help_text='например, участник или победитель', max_length=50, verbose_name='Роль студента в мероприятии')),
                ('eventId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.events')),
                ('studentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.students')),
            ],
            options={
                'verbose_name': 'Студенты в мероприятиях',
                'verbose_name_plural': 'Студенты в мероприятиях',
            },
        ),
        migrations.CreateModel(
            name='Specializations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeName', models.CharField(max_length=50, verbose_name='Код специальности')),
                ('name', models.CharField(max_length=150, verbose_name='Название специальности')),
                ('facultyId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.faculties')),
            ],
            options={
                'verbose_name': 'Специальность',
                'verbose_name_plural': 'Специальности',
            },
        ),
        migrations.AddField(
            model_name='groups',
            name='specializationId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.specializations'),
        ),
        migrations.AddField(
            model_name='faculties',
            name='universityId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.universities'),
        ),
    ]