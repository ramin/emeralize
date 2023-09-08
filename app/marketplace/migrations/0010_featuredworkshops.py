# Generated by Django 4.0.1 on 2023-05-21 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('criticalpath', '0016_alter_workshop_excerpt_alter_workshop_title'),
        ('marketplace', '0009_purchase_workshop'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedWorkshops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence_number', models.PositiveIntegerField()),
                ('workshop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='criticalpath.workshop')),
            ],
        ),
    ]
