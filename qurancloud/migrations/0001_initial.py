# Generated by Django 4.0.8 on 2023-11-06 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ayah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('number', models.PositiveIntegerField()),
                ('text', models.TextField()),
                ('number_in_surah', models.PositiveIntegerField()),
                ('juz', models.PositiveIntegerField()),
                ('manzil', models.PositiveIntegerField()),
                ('page', models.PositiveIntegerField()),
                ('ruku', models.PositiveIntegerField()),
                ('hizb_quarter', models.PositiveIntegerField()),
                ('sajda', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('identifier', models.CharField(max_length=1000)),
                ('language', models.CharField(max_length=50)),
                ('name', models.TextField()),
                ('englishName', models.CharField(max_length=500)),
                ('format', models.CharField(max_length=128)),
                ('type', models.CharField(max_length=150)),
                ('direction', models.CharField(max_length=80)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Surah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('number', models.PositiveIntegerField()),
                ('name', models.TextField()),
                ('english_name', models.CharField(max_length=255)),
                ('english_name_translation', models.CharField(max_length=255)),
                ('revelation_type', models.CharField(max_length=255)),
                ('ayahs', models.ManyToManyField(to='qurancloud.ayah')),
                ('edition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qurancloud.edition')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Juz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('number', models.PositiveIntegerField()),
                ('ayahs', models.ManyToManyField(related_name='juzs', to='qurancloud.ayah')),
                ('edition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qurancloud.edition')),
                ('surahs', models.ManyToManyField(related_name='juzzsurahs', to='qurancloud.surah')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='ayah',
            name='edition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qurancloud.edition'),
        ),
    ]
