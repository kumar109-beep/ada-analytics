# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userProfile(models.Model):
    userFk = models.ForeignKey(User, verbose_name=("User Fk"), on_delete=models.CASCADE)
    address = models.TextField(blank=True,null=True)
    city = models.CharField(max_length=50,blank=True,null=True)
    country = models.CharField(max_length=50,default='India')
    postal_code = models.CharField(max_length=10,blank=True,null=True)
    about_me = models.TextField(blank=True,null=True)


class secretKey(models.Model):
    secret_key = models.CharField(max_length=200)
    timeStamp = models.DateTimeField(auto_now_add=True)



class Customers(models.Model):
    user_id = models.IntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customers'
        unique_together = (('id', 'user_id'),)



class Orders(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    guest_id = models.IntegerField(blank=True, null=True)
    is_deleted = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    seller_id = models.IntegerField(blank=True, null=True)
    shipping_address = models.TextField(blank=True, null=True)
    uniware_request = models.TextField(blank=True, null=True)
    uniware_response = models.TextField(blank=True, null=True)
    delivery_status = models.CharField(max_length=20, blank=True, null=True)
    payment_type = models.CharField(max_length=20, blank=True, null=True)
    purchase_order_number = models.CharField(max_length=200, blank=True, null=True)
    payment_status = models.CharField(max_length=20, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    payment_details = models.TextField(blank=True, null=True)
    grand_total = models.FloatField(blank=True, null=True)
    shipping_charge = models.CharField(max_length=200, blank=True, null=True)
    coupon_code = models.CharField(max_length=200, blank=True, null=True)
    coupon_discount = models.FloatField()
    code = models.TextField(blank=True, null=True)
    date = models.IntegerField()
    viewed = models.IntegerField()
    gift_wrap = models.IntegerField()
    delivery_viewed = models.IntegerField()
    payment_status_viewed = models.IntegerField(blank=True, null=True)
    commission_calculated = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'orders'



class OrderLog(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    guest_id = models.IntegerField(blank=True, null=True)
    seller_id = models.IntegerField(blank=True, null=True)
    shipping_address = models.TextField(blank=True, null=True)
    delivery_status = models.CharField(max_length=20, blank=True, null=True)
    payment_type = models.CharField(max_length=20, blank=True, null=True)
    purchase_order_number = models.CharField(max_length=200, blank=True, null=True)
    payment_status = models.CharField(max_length=20, blank=True, null=True)
    payment_details = models.TextField(blank=True, null=True)
    grand_total = models.FloatField(blank=True, null=True)
    shipping_charge = models.CharField(max_length=200, blank=True, null=True)
    coupon_code = models.CharField(max_length=200, blank=True, null=True)
    coupon_discount = models.FloatField()
    code = models.TextField(blank=True, null=True)
    date = models.IntegerField()
    viewed = models.IntegerField()
    gift_wrap = models.IntegerField()
    remark = models.TextField(blank=True, null=True)
    delivery_viewed = models.IntegerField()
    payment_status_viewed = models.IntegerField(blank=True, null=True)
    commission_calculated = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'order_log'




class OrderStatus(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    short = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    order_by = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'order_status'




class Products(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=200, blank=True, null=True)
    added_by = models.CharField(max_length=6)
    user_id = models.IntegerField()
    category_id = models.IntegerField()
    subcategoryid = models.CharField(db_column='subCategoryId', max_length=200, blank=True, null=True)  # Field name made lowercase.
    brand_id = models.IntegerField(blank=True, null=True)
    photos = models.CharField(max_length=2000, blank=True, null=True)
    thumbnail_img = models.CharField(max_length=100, blank=True, null=True)
    imagetype = models.CharField(db_column='imageType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    video_provider = models.CharField(max_length=20, blank=True, null=True)
    video_link = models.CharField(max_length=100, blank=True, null=True)
    tags = models.CharField(max_length=1000, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    unit_price = models.FloatField()
    added_hsn_price = models.FloatField()
    purchase_price = models.FloatField(blank=True, null=True)
    variant_product = models.IntegerField()
    attributes = models.CharField(max_length=1000)
    choice_options = models.TextField(blank=True, null=True)
    colors = models.TextField(blank=True, null=True)
    variations = models.TextField(blank=True, null=True)
    todays_deal = models.IntegerField()
    published = models.IntegerField()
    stock_visibility_state = models.CharField(max_length=10, blank=True, null=True)
    cash_on_delivery = models.IntegerField()
    featured = models.IntegerField()
    seller_featured = models.IntegerField()
    current_stock = models.IntegerField()
    unit = models.CharField(max_length=20, blank=True, null=True)
    min_qty = models.IntegerField()
    low_stock_quantity = models.IntegerField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    discount_type = models.CharField(max_length=10, blank=True, null=True)
    tax = models.FloatField(blank=True, null=True)
    tax_type = models.CharField(max_length=10, blank=True, null=True)
    shipping_type = models.CharField(max_length=20, db_collation='latin1_swedish_ci', blank=True, null=True)
    shipping_cost = models.TextField(blank=True, null=True)
    is_quantity_multiplied = models.IntegerField()
    est_shipping_days = models.IntegerField(blank=True, null=True)
    num_of_sale = models.IntegerField()
    meta_title = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_img = models.CharField(max_length=255, blank=True, null=True)
    pdf = models.CharField(max_length=255, blank=True, null=True)
    slug = models.TextField()
    refundable = models.IntegerField()
    earn_point = models.FloatField()
    rating = models.FloatField()
    barcode = models.CharField(max_length=255, blank=True, null=True)
    hsncode = models.CharField(db_column='HSNCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    digital = models.IntegerField()
    is_deleted = models.IntegerField()
    file_name = models.CharField(max_length=255, blank=True, null=True)
    file_path = models.CharField(max_length=255, blank=True, null=True)
    isshikoh = models.CharField(max_length=200, blank=True, null=True)
    shikohpriority = models.CharField(db_column='ShikohPriority', max_length=200, blank=True, null=True)  # Field name made lowercase.
    trendingpriority = models.IntegerField(db_column='TrendingPriority', blank=True, null=True)  # Field name made lowercase.
    istrending = models.CharField(max_length=200, blank=True, null=True)
    isfestivewear = models.CharField(db_column='isFestiveWear', max_length=100, blank=True, null=True)  # Field name made lowercase.
    festivepriority = models.IntegerField(db_column='FestivePriority', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'products'




class OrderDetails(models.Model):
    order_id = models.IntegerField()
    seller_id = models.IntegerField(blank=True, null=True)
    product_id = models.IntegerField()
    variation = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    tax = models.FloatField()
    shipping_cost = models.FloatField()
    quantity = models.IntegerField(blank=True, null=True)
    payment_status = models.CharField(max_length=10)
    delivery_status = models.CharField(max_length=20, blank=True, null=True)
    shipping_type = models.CharField(max_length=255, blank=True, null=True)
    pickup_point_id = models.IntegerField(blank=True, null=True)
    product_referral_code = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'order_details'