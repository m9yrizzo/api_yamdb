import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=64, unique=True, verbose_name='Слаг категории')),
            ],
            options={
                'verbose_name': 'Category',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Жанр')),
                ('slug', models.SlugField(max_length=64, unique=True, verbose_name='Слаг жанра')),
            ],
            options={
                'verbose_name': 'Genre',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Произведение')),
                ('year', models.IntegerField(db_index=True, verbose_name='Год создания')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание произведения')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='title', to='categories.Category', verbose_name='Категория произведения')),
            ],
            options={
                'verbose_name': 'Title',
                'ordering': ('-year',),
            },
        ),
        migrations.CreateModel(
            name='TitleGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.Genre', verbose_name='Жанр произведения')),
                ('title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.Title', verbose_name='Произведение')),
            ],
        ),
        migrations.AddField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(through='categories.TitleGenre', to='categories.Genre', verbose_name='Жанр произведения'),
        ),
    ]
