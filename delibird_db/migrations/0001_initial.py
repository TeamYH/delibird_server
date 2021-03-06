# Generated by Django 3.2 on 2021-04-17 11:05

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('detail_address', models.CharField(max_length=30)),
                ('store_num', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phonenum', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_num', models.IntegerField()),
                ('pos_x', models.IntegerField()),
                ('pos_y', models.IntegerField()),
                ('angle', models.IntegerField()),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delibird_db.store')),
            ],
        ),
        migrations.AddField(
            model_name='store',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='delibird_db.user'),
        ),
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('serial_num', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('R', 'require_setting'), ('M', 'mapping'), ('I', 'idle'), ('S', 'serving'), ('R', 'returning'), ('C', 'cleaning')], default='R', max_length=1)),
                ('battery', models.IntegerField()),
                ('desc', models.TextField(null=True)),
                ('current_pos_x', models.IntegerField(null=True)),
                ('current_pos_y', models.IntegerField(null=True)),
                ('store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='delibird_db.store')),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('map_key', models.CharField(max_length=1000)),
                ('store', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='delibird_db.store')),
            ],
        ),
    ]
