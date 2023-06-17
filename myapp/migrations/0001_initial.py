# Generated by Django 4.2.2 on 2023-06-16 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agents',
            fields=[
                ('agentID', models.AutoField(primary_key=True, serialize=False)),
                ('queue', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('issueID', models.AutoField(primary_key=True, serialize=False)),
                ('userID', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
                ('problem', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('INQUEUE', 'In Queue'), ('ASSIGNED', 'Assigned'), ('DISPATCHED', 'Dispatched')], default='INQUEUE', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Mechanic',
            fields=[
                ('mechanicID', models.AutoField(primary_key=True, serialize=False)),
                ('availability', models.BooleanField(default=True)),
            ],
        ),
    ]
