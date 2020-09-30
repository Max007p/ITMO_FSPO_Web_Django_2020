# Generated by Django 3.1.1 on 2020-09-22 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('au_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Disc',
            fields=[
                ('disc_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('disc_name', models.CharField(max_length=70)),
                ('production_date', models.DateField()),
                ('firm', models.CharField(max_length=70)),
                ('url', models.URLField()),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Диск',
                'verbose_name_plural': 'Диски',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('genre_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('genre_name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('sale_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('date_sale', models.DateField()),
                ('amount', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('disc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gameshop.disc')),
            ],
            options={
                'verbose_name': 'Продажа',
                'verbose_name_plural': 'Продажи',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('game_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('game_name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gameshop.author')),
            ],
            options={
                'verbose_name': 'Игра',
                'verbose_name_plural': 'Игры',
            },
        ),
        migrations.AddField(
            model_name='disc',
            name='games',
            field=models.ManyToManyField(to='Gameshop.Game', verbose_name='Игры'),
        ),
        migrations.AddField(
            model_name='disc',
            name='genres',
            field=models.ManyToManyField(to='Gameshop.Genre', verbose_name='Жанры'),
        ),
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('buy_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('date_buy', models.DateField()),
                ('amount', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('description', models.TextField()),
                ('disc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gameshop.disc')),
            ],
            options={
                'verbose_name': 'Покупка',
                'verbose_name_plural': 'Покупки',
            },
        ),
    ]