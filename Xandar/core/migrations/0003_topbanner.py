# Generated by Django 2.1.7 on 2019-05-31 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190530_0449'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('Electronics', 'Electronics'), ('Clothing', 'Clothing'), ('Lifestyle', 'Lifestyle')], max_length=20)),
                ('sub_category', models.CharField(blank=True, choices=[('T-Shirts', 'T-Shirts'), ('Glasses', 'Glasses'), ('Shoes', 'Shoes'), ('Phone', 'Phone')], max_length=20)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('image', models.FileField(upload_to='banner_images/')),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
