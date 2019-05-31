# Generated by Django 2.1.7 on 2019-05-31 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_topbanner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='banner',
            name='category',
            field=models.CharField(choices=[('Clothing', 'Clothing'), ('Electronics', 'Electronics'), ('Accessories', 'Accessories')], max_length=20),
        ),
        migrations.AlterField(
            model_name='banner',
            name='sub_category',
            field=models.CharField(blank=True, choices=[('Mobiles', 'Mobiles'), ('Mobile_Accessories', 'Mobile Accessories'), ('Laptops', 'Laptops'), ('Desktop_PC', 'Desktop PC'), ('Tablets', 'Tablets'), ('Television', 'Television'), ('Air_Conditioner', 'Air Conditioner'), ('Refrigerator', 'Refrigerator'), ('Washing_Machine', 'Washing Machine'), ('Kitchen_Appliances', 'Kitchen Appliances'), ('T_Shirt', 'T-Shirt'), ('Jeans', 'Jeans'), ('Inner_Wear', 'Inner Wear'), ('Western_Wear', 'Western Wear'), ('Ethnic_Wear', 'Ethnic Wear'), ('Kurti', 'Kurti'), ('Footwear', 'Footwear'), ('Sunglasses', 'Sunglasses'), ('Backpack', 'Backpack'), ('Handbag', 'Handbag'), ('Belt', 'Belt')], max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Clothing', 'Clothing'), ('Electronics', 'Electronics'), ('Accessories', 'Accessories')], max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_category',
            field=models.CharField(choices=[('Mobiles', 'Mobiles'), ('Mobile_Accessories', 'Mobile Accessories'), ('Laptops', 'Laptops'), ('Desktop_PC', 'Desktop PC'), ('Tablets', 'Tablets'), ('Television', 'Television'), ('Air_Conditioner', 'Air Conditioner'), ('Refrigerator', 'Refrigerator'), ('Washing_Machine', 'Washing Machine'), ('Kitchen_Appliances', 'Kitchen Appliances'), ('T_Shirt', 'T-Shirt'), ('Jeans', 'Jeans'), ('Inner_Wear', 'Inner Wear'), ('Western_Wear', 'Western Wear'), ('Ethnic_Wear', 'Ethnic Wear'), ('Kurti', 'Kurti'), ('Footwear', 'Footwear'), ('Sunglasses', 'Sunglasses'), ('Backpack', 'Backpack'), ('Handbag', 'Handbag'), ('Belt', 'Belt')], max_length=20),
        ),
        migrations.AlterField(
            model_name='topbanner',
            name='category',
            field=models.CharField(choices=[('Clothing', 'Clothing'), ('Electronics', 'Electronics'), ('Accessories', 'Accessories')], max_length=20),
        ),
        migrations.AlterField(
            model_name='topbanner',
            name='sub_category',
            field=models.CharField(blank=True, choices=[('Mobiles', 'Mobiles'), ('Mobile_Accessories', 'Mobile Accessories'), ('Laptops', 'Laptops'), ('Desktop_PC', 'Desktop PC'), ('Tablets', 'Tablets'), ('Television', 'Television'), ('Air_Conditioner', 'Air Conditioner'), ('Refrigerator', 'Refrigerator'), ('Washing_Machine', 'Washing Machine'), ('Kitchen_Appliances', 'Kitchen Appliances'), ('T_Shirt', 'T-Shirt'), ('Jeans', 'Jeans'), ('Inner_Wear', 'Inner Wear'), ('Western_Wear', 'Western Wear'), ('Ethnic_Wear', 'Ethnic Wear'), ('Kurti', 'Kurti'), ('Footwear', 'Footwear'), ('Sunglasses', 'Sunglasses'), ('Backpack', 'Backpack'), ('Handbag', 'Handbag'), ('Belt', 'Belt')], max_length=20),
        ),
    ]