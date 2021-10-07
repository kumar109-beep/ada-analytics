# Generated by Django 3.2.6 on 2021-10-07 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'customers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField()),
                ('seller_id', models.IntegerField(blank=True, null=True)),
                ('product_id', models.IntegerField()),
                ('variation', models.TextField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('tax', models.FloatField()),
                ('shipping_cost', models.FloatField()),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('payment_status', models.CharField(max_length=10)),
                ('delivery_status', models.CharField(blank=True, max_length=20, null=True)),
                ('shipping_type', models.CharField(blank=True, max_length=255, null=True)),
                ('pickup_point_id', models.IntegerField(blank=True, null=True)),
                ('product_referral_code', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'order_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('guest_id', models.IntegerField(blank=True, null=True)),
                ('seller_id', models.IntegerField(blank=True, null=True)),
                ('shipping_address', models.TextField(blank=True, null=True)),
                ('delivery_status', models.CharField(blank=True, max_length=20, null=True)),
                ('payment_type', models.CharField(blank=True, max_length=20, null=True)),
                ('purchase_order_number', models.CharField(blank=True, max_length=200, null=True)),
                ('payment_status', models.CharField(blank=True, max_length=20, null=True)),
                ('payment_details', models.TextField(blank=True, null=True)),
                ('grand_total', models.FloatField(blank=True, null=True)),
                ('shipping_charge', models.CharField(blank=True, max_length=200, null=True)),
                ('coupon_code', models.CharField(blank=True, max_length=200, null=True)),
                ('coupon_discount', models.FloatField()),
                ('code', models.TextField(blank=True, null=True)),
                ('date', models.IntegerField()),
                ('viewed', models.IntegerField()),
                ('gift_wrap', models.IntegerField()),
                ('remark', models.TextField(blank=True, null=True)),
                ('delivery_viewed', models.IntegerField()),
                ('payment_status_viewed', models.IntegerField(blank=True, null=True)),
                ('commission_calculated', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'order_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('guest_id', models.IntegerField(blank=True, null=True)),
                ('is_deleted', models.IntegerField()),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('seller_id', models.IntegerField(blank=True, null=True)),
                ('shipping_address', models.TextField(blank=True, null=True)),
                ('uniware_request', models.TextField(blank=True, null=True)),
                ('uniware_response', models.TextField(blank=True, null=True)),
                ('delivery_status', models.CharField(blank=True, max_length=20, null=True)),
                ('payment_type', models.CharField(blank=True, max_length=20, null=True)),
                ('purchase_order_number', models.CharField(blank=True, max_length=200, null=True)),
                ('payment_status', models.CharField(blank=True, max_length=20, null=True)),
                ('remark', models.TextField(blank=True, null=True)),
                ('payment_details', models.TextField(blank=True, null=True)),
                ('grand_total', models.FloatField(blank=True, null=True)),
                ('shipping_charge', models.CharField(blank=True, max_length=200, null=True)),
                ('coupon_code', models.CharField(blank=True, max_length=200, null=True)),
                ('coupon_discount', models.FloatField()),
                ('code', models.TextField(blank=True, null=True)),
                ('date', models.IntegerField()),
                ('viewed', models.IntegerField()),
                ('gift_wrap', models.IntegerField()),
                ('delivery_viewed', models.IntegerField()),
                ('payment_status_viewed', models.IntegerField(blank=True, null=True)),
                ('commission_calculated', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('short', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('order_by', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'order_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('sku', models.CharField(blank=True, max_length=200, null=True)),
                ('added_by', models.CharField(max_length=6)),
                ('user_id', models.IntegerField()),
                ('category_id', models.IntegerField()),
                ('subcategoryid', models.CharField(blank=True, db_column='subCategoryId', max_length=200, null=True)),
                ('brand_id', models.IntegerField(blank=True, null=True)),
                ('photos', models.CharField(blank=True, max_length=2000, null=True)),
                ('thumbnail_img', models.CharField(blank=True, max_length=100, null=True)),
                ('imagetype', models.CharField(blank=True, db_column='imageType', max_length=100, null=True)),
                ('video_provider', models.CharField(blank=True, max_length=20, null=True)),
                ('video_link', models.CharField(blank=True, max_length=100, null=True)),
                ('tags', models.CharField(blank=True, max_length=1000, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('short_description', models.TextField(blank=True, null=True)),
                ('unit_price', models.FloatField()),
                ('added_hsn_price', models.FloatField()),
                ('purchase_price', models.FloatField(blank=True, null=True)),
                ('variant_product', models.IntegerField()),
                ('attributes', models.CharField(max_length=1000)),
                ('choice_options', models.TextField(blank=True, null=True)),
                ('colors', models.TextField(blank=True, null=True)),
                ('variations', models.TextField(blank=True, null=True)),
                ('todays_deal', models.IntegerField()),
                ('published', models.IntegerField()),
                ('stock_visibility_state', models.CharField(blank=True, max_length=10, null=True)),
                ('cash_on_delivery', models.IntegerField()),
                ('featured', models.IntegerField()),
                ('seller_featured', models.IntegerField()),
                ('current_stock', models.IntegerField()),
                ('unit', models.CharField(blank=True, max_length=20, null=True)),
                ('min_qty', models.IntegerField()),
                ('low_stock_quantity', models.IntegerField(blank=True, null=True)),
                ('discount', models.FloatField(blank=True, null=True)),
                ('discount_type', models.CharField(blank=True, max_length=10, null=True)),
                ('tax', models.FloatField(blank=True, null=True)),
                ('tax_type', models.CharField(blank=True, max_length=10, null=True)),
                ('shipping_type', models.CharField(blank=True, db_collation='latin1_swedish_ci', max_length=20, null=True)),
                ('shipping_cost', models.TextField(blank=True, null=True)),
                ('is_quantity_multiplied', models.IntegerField()),
                ('est_shipping_days', models.IntegerField(blank=True, null=True)),
                ('num_of_sale', models.IntegerField()),
                ('meta_title', models.TextField(blank=True, null=True)),
                ('meta_description', models.TextField(blank=True, null=True)),
                ('meta_img', models.CharField(blank=True, max_length=255, null=True)),
                ('pdf', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.TextField()),
                ('refundable', models.IntegerField()),
                ('earn_point', models.FloatField()),
                ('rating', models.FloatField()),
                ('barcode', models.CharField(blank=True, max_length=255, null=True)),
                ('hsncode', models.CharField(blank=True, db_column='HSNCode', max_length=255, null=True)),
                ('digital', models.IntegerField()),
                ('is_deleted', models.IntegerField()),
                ('file_name', models.CharField(blank=True, max_length=255, null=True)),
                ('file_path', models.CharField(blank=True, max_length=255, null=True)),
                ('isshikoh', models.CharField(blank=True, max_length=200, null=True)),
                ('shikohpriority', models.CharField(blank=True, db_column='ShikohPriority', max_length=200, null=True)),
                ('trendingpriority', models.IntegerField(blank=True, db_column='TrendingPriority', null=True)),
                ('istrending', models.CharField(blank=True, max_length=200, null=True)),
                ('isfestivewear', models.CharField(blank=True, db_column='isFestiveWear', max_length=100, null=True)),
                ('festivepriority', models.IntegerField(blank=True, db_column='FestivePriority', null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'products',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='secretKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secret_key', models.CharField(max_length=200)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]