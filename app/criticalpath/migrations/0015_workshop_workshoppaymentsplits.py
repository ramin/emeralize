# Generated by Django 4.0.1 on 2023-05-21 22:28

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('marketplace', '0008_rename_currency_text_currency_text'),
        ('criticalpath', '0014_ebook_currency_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Not Published'), (1, 'Published'), (2, 'Archived')], default=0)),
                ('title', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3, 'Ebook title must be greater than 3 characters')])),
                ('excerpt', models.CharField(blank=True, max_length=500, null=True, validators=[django.core.validators.MinLengthValidator(3, 'Ebook excerpt must be greater than 3 characters')])),
                ('content', django_quill.fields.QuillField(blank=True, null=True)),
                ('cover_image', models.ImageField(blank=True, default='seo-card-image.png', null=True, upload_to='workshops/cover_images/')),
                ('price', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100000)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('currency_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='marketplace.currency')),
            ],
        ),
        migrations.CreateModel(
            name='WorkshopPaymentSplits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('workshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='criticalpath.workshop')),
            ],
        ),
    ]
