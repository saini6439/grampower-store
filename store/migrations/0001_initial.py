# Generated by Django 3.1.6 on 2021-02-11 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('about', models.TextField()),
                ('products', models.CharField(max_length=250)),
                ('lang', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('lot', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StoreOpening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sunday_from_hour', models.TimeField()),
                ('monday_from_hour', models.TimeField()),
                ('tuesday_from_hour', models.TimeField()),
                ('wednesday_from_hour', models.TimeField()),
                ('thrusday_from_hour', models.TimeField()),
                ('friday_from_hour', models.TimeField()),
                ('saturday_from_hour', models.TimeField()),
                ('sunday_to_hour', models.TimeField()),
                ('monday_to_hour', models.TimeField()),
                ('tuesday_to_hour', models.TimeField()),
                ('wednesday_to_hour', models.TimeField()),
                ('thrusday_to_hour', models.TimeField()),
                ('friday_to_hour', models.TimeField()),
                ('saturday_to_hour', models.TimeField()),
                ('store', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.store')),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='images/')),
                ('store', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.store')),
            ],
        ),
    ]
