# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.db.models.fields import json
from django.shortcuts import render
from django.http import JsonResponse
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from django.contrib.auth.models import User
from .models import userProfile,Customers,Orders,Products,OrderDetails
# from models import *
from datetime import date,timedelta
import datetime
from django.db.models import Sum
import json



@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    # creating the date object of today's date
    todays_date = date.today()
    totalCustomer = Customers.objects.all().using('analytics')
    request.session['totalCustomer'] = len(totalCustomer)

    totalOrders = Orders.objects.all().using('analytics')
    request.session['totalOrders'] = len(totalOrders)

    # #############################################################################################
    #                         Category Wise Graph Data
    # =============================================================================================
    topImpressions = Products.objects.filter(published =1,is_deleted=0).order_by('-num_of_sale')[0:10].using('analytics')
    # wC_wear = 0
    # mC_wear = 0
    # hDecor = 0
    # premium = 0

    # wC_wear_sales = 0
    # mC_wear_sales = 0
    # hDecor_sales = 0
    # premium_sales = 0

    
    # catTotalOrder = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day)).using('analytics')
    # for i in catTotalOrder:
    #     user = i.user_id
    #     print(user)
    #     OrderInfo = OrderDetails.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day),order_id=i.id).using('analytics')
    #     print('order >> ',OrderInfo)
    #     for j in OrderInfo:
    #         print('product >>> ',j.product_id)
    #         category = Products.objects.filter(id = j.product_id).using('analytics')
    #         print('category >>> ',category[0].category_id,type(category[0].category_id),'<====>',category[0].purchase_price,'<====>',category[0].shipping_cost)
    #         if(category[0].category_id == 1):
    #             wC_wear = wC_wear + 1
    #         elif(category[0].category_id == 2):
    #             mC_wear = mC_wear + 1
    #         elif(category[0].category_id == 3):
    #             hDecor = hDecor + 1
    #         elif(category[0].category_id == 4):
    #             premium = premium + 1

    # catDict = {'sales' : {'Women Chikan Wear':wC_wear_sales,'Men Chikan wear':mC_wear_sales,'Home Decor':hDecor_sales,'Premium':premium_sales},
    #            'SoldQuantity':{'Women Chikan Wear':wC_wear,'Men Chikan wear':mC_wear,'Home Decor':hDecor,'Premium':premium}}
    # print('Category dict ::>> ',catDict)
    # exit()

    # #############################################################################################
    todayTotalOrders = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day)).using('analytics')
    todayTotalOrdersAmount = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day)).using('analytics').aggregate(Sum('grand_total'))
    totalRevenue = Orders.objects.all().using('analytics').aggregate(Sum('grand_total'))
    totalCancelledRevenue = Orders.objects.filter(delivery_status='cancelled').using('analytics').aggregate(Sum('grand_total'))

    todayTotalOrdersRevenue = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day),delivery_status='cancelled').using('analytics').aggregate(Sum('grand_total'))

    # =================================================================================================
    if(todayTotalOrdersRevenue['grand_total__sum'] == None):
        totalTodayRevenue = float(todayTotalOrdersAmount['grand_total__sum'])
    else:
        totalTodayRevenue = float(todayTotalOrdersAmount['grand_total__sum']) - float(todayTotalOrdersRevenue['grand_total__sum'])
    

    # =================================================================================================
    totalPlacedOrders_today = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day),seller_id__isnull=True).using('analytics')
    failedOrders_today = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day),delivery_status='failed').using('analytics')
    ProcessedOrders_today = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day),delivery_status='process').using('analytics')
    shippedOrders_today = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day),delivery_status='shipped').using('analytics')
    cancelledOrders_today = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day),delivery_status='cancelled').using('analytics')

    # =================================================================================================
    totalListings = Products.objects.all().using('analytics')
    liveListings = Products.objects.filter(current_stock__isnull=False).using('analytics')
    outOfStockListings = Products.objects.filter(current_stock__isnull=True).using('analytics')
    unpublishedListings = Products.objects.filter(published__isnull=True).using('analytics')
    # =================================================================================================
    # =================================================================================================
    context['totalCustomer'] = len(totalCustomer)
    context['totalOrders'] = len(totalOrders)
    context['todayTotalOrders'] = len(todayTotalOrders)
    context['todayTotalOrdersAmount'] = round(float(todayTotalOrdersAmount['grand_total__sum']),2)
    context['totalRevenue'] = round(float(totalRevenue['grand_total__sum']) - float(totalCancelledRevenue['grand_total__sum']),2)
    request.session['totalRevenue'] = round(float(totalRevenue['grand_total__sum']) - float(totalCancelledRevenue['grand_total__sum']),2)

    context['totalTodayRevenue'] = round(float(totalTodayRevenue),2)

    context['totalCreatedOrders_today'] = len(todayTotalOrders) - len(totalPlacedOrders_today)
    context['failedOrders_today'] = len(failedOrders_today)
    context['ProcessedOrders_today'] = len(ProcessedOrders_today)
    context['shippedOrders_today'] = len(shippedOrders_today)
    context['cancelledOrders_today'] = len(cancelledOrders_today)

    context['totalListings'] = len(totalListings)
    context['liveListings'] = len(liveListings)
    context['outOfStockListings'] = len(outOfStockListings)
    context['unpublishedListings'] = len(unpublishedListings)


    context['topImpressions'] = topImpressions
    # =================================================================================================

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def profile(request):
    if request.method == 'GET':
        user_fk = User.objects.get(email = request.user.email)
        try:
            profileObj = userProfile.objects.get(userFk=user_fk)
            return render(request,'home/profile.html',{'profileObj':profileObj})
        except:
            return render(request,'home/profile.html',{'profileObj':profileObj})


    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        city = request.POST['city']
        country = request.POST['country']
        postal_code = request.POST['postal_code']
        about_me = request.POST['about_me']

        try:
            user_fk = User.objects.get(email = request.user.email)
            user_fk.first_name = first_name
            user_fk.last_name= last_name
            user_fk.save()

            if(userProfile.objects.filter(userFk=user_fk)):
                profileObj = userProfile.objects.get(userFk=user_fk)
                profileObj.address=address
                profileObj.city=city
                profileObj.country=country
                profileObj.postal_code=postal_code
                profileObj.about_me=about_me
                profileObj.save()
            else:
                profileObj = userProfile(userFk=user_fk,address=address,city=city,country=country,postal_code=postal_code,about_me=about_me)
                profileObj.save()

            return JsonResponse({'response':'success'})
        except:
            return JsonResponse({'response':'fail'})




# ==============================================================================================================================================================
#                                                               DASHBOARD FILTERS
# ==============================================================================================================================================================
@login_required(login_url="/login/")
def total_order_filter(request):
    if request.method == 'GET':
        filter = request.GET['filter']
        responseList = []

        if(filter.strip() == 'Today'):
            todays_date = date.today()
            todayTotalOrders = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day)).using('analytics')
            totalPlacedOrders_today = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day),seller_id__isnull=True).using('analytics')
            failedOrders_today = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day),delivery_status='failed').using('analytics')
            ProcessedOrders_today = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day),delivery_status='process').using('analytics')
            shippedOrders_today = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day),delivery_status='shipped').using('analytics')
            cancelledOrders_today = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day),delivery_status='cancelled').using('analytics')
            
            context = {}
            context['todayTotalOrders'] = len(todayTotalOrders)
            context['totalPlacedOrders_today'] = len(totalPlacedOrders_today)
            context['failedOrders_today'] = len(failedOrders_today)
            context['ProcessedOrders_today'] = len(ProcessedOrders_today)
            context['shippedOrders_today'] = len(shippedOrders_today)
            context['cancelledOrders_today'] = len(cancelledOrders_today)
            responseList.append(context)
        
        
        elif(filter.strip() == 'All Time'):
            todayTotalOrders = Orders.objects.all().using('analytics')
            totalPlacedOrders_today = Orders.objects.filter(seller_id__isnull=True).using('analytics')
            failedOrders_today = Orders.objects.filter(delivery_status='failed').using('analytics')
            ProcessedOrders_today = Orders.objects.filter(delivery_status='process').using('analytics')
            shippedOrders_today = Orders.objects.filter(delivery_status='shipped').using('analytics')
            cancelledOrders_today = Orders.objects.filter(delivery_status='cancelled').using('analytics')
            
            context = {}
            context['todayTotalOrders'] = len(todayTotalOrders)
            context['totalPlacedOrders_today'] = len(totalPlacedOrders_today)
            context['failedOrders_today'] = len(failedOrders_today)
            context['ProcessedOrders_today'] = len(ProcessedOrders_today)
            context['shippedOrders_today'] = len(shippedOrders_today)
            context['cancelledOrders_today'] = len(cancelledOrders_today)
            responseList.append(context)

            
        elif(filter.strip() == 'Last 7 Days'):
            d=date.today()-timedelta(days=7)
            todayTotalOrders = Orders.objects.filter(created_at__gte=d).using('analytics')
            totalPlacedOrders_today = Orders.objects.filter(created_at__gte=d,seller_id__isnull=True).using('analytics')
            failedOrders_today = Orders.objects.filter(created_at__gte=d,delivery_status='failed').using('analytics')
            ProcessedOrders_today = Orders.objects.filter(created_at__gte=d,delivery_status='process' or 'pending').using('analytics')
            shippedOrders_today = Orders.objects.filter(created_at__gte=d,delivery_status='shipped').using('analytics')
            cancelledOrders_today = Orders.objects.filter(created_at__gte=d,delivery_status='cancelled').using('analytics')
            
            context = {}
            context['todayTotalOrders'] = len(todayTotalOrders)
            context['totalPlacedOrders_today'] = len(totalPlacedOrders_today)
            context['failedOrders_today'] = len(failedOrders_today)
            context['ProcessedOrders_today'] = len(ProcessedOrders_today)
            context['shippedOrders_today'] = len(shippedOrders_today)
            context['cancelledOrders_today'] = len(cancelledOrders_today)
            responseList.append(context)


        elif(filter.strip() == 'Current Month'):
            today = datetime.date.today()
            todayTotalOrders = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month).using('analytics')
            totalPlacedOrders_today = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month,seller_id__isnull=True).using('analytics')
            failedOrders_today = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month,delivery_status='failed').using('analytics')
            ProcessedOrders_today = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month,delivery_status='process').using('analytics')
            shippedOrders_today = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month,delivery_status='shipped').using('analytics')
            cancelledOrders_today = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month,delivery_status='cancelled').using('analytics')
            
            context = {}
            context['todayTotalOrders'] = len(todayTotalOrders)
            context['totalPlacedOrders_today'] = len(totalPlacedOrders_today)
            context['failedOrders_today'] = len(failedOrders_today)
            context['ProcessedOrders_today'] = len(ProcessedOrders_today)
            context['shippedOrders_today'] = len(shippedOrders_today)
            context['cancelledOrders_today'] = len(cancelledOrders_today)
            responseList.append(context)

        elif(filter.strip() == 'Last Month'):
            today = datetime.date.today()
            todayTotalOrders = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month-1).using('analytics')
            totalPlacedOrders_today = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month-1,seller_id__isnull=True).using('analytics')
            failedOrders_today = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month-1,delivery_status='failed').using('analytics')
            ProcessedOrders_today = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month-1,delivery_status='process').using('analytics')
            PendingOrders_today = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month-1,delivery_status='pending').using('analytics')

            shippedOrders_today = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month-1,delivery_status='shipped').using('analytics')
            cancelledOrders_today = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month-1,delivery_status='cancelled').using('analytics')
            
            context = {}
            context['todayTotalOrders'] = len(todayTotalOrders)
            context['totalPlacedOrders_today'] = len(totalPlacedOrders_today)
            context['failedOrders_today'] = len(failedOrders_today)
            context['ProcessedOrders_today'] = len(ProcessedOrders_today)+len(PendingOrders_today)
            context['shippedOrders_today'] = len(shippedOrders_today)
            context['cancelledOrders_today'] = len(cancelledOrders_today)
            responseList.append(context)
        else:
            pass


        return JsonResponse(responseList, safe=False)
# ==============================================================================================================================================================
@login_required(login_url="/login/")
def revenue(request):
    if request.method == 'GET':
        responseList = []
        context_1 = {}
        context_1['month_1'] = 0
        context_1['month_2'] = 0
        context_1['month_3'] = 0
        context_1['month_4'] = 0
        context_1['month_5'] = 0
        context_1['month_6'] = 0
        context_1['month_7'] = 0
        context_1['month_8'] = 0
        context_1['month_9'] = 0
        context_1['month_10'] = 0
        context_1['month_11'] = 0
        context_1['month_12'] = 0

        invoices = Orders.objects.all().using('analytics')
        months = invoices.datetimes("created_at", kind="month")
        count = 1

        for month in months:
            month_invs = invoices.filter(created_at__month=month.month)
            month_total = month_invs.aggregate(total=Sum("grand_total")).get("total")
            print(f"Month: {month}, Total: {month_total}")
            context_1['month_'+str(month.month)] = int(month_total)
            count = count + 1

        for i in range(len(context_1)):
            responseList.append(context_1['month_'+str(i+1)])

        return JsonResponse(responseList, safe=False)


# ==============================================================================================================================================================
@login_required(login_url="/login/")
def master_filter_1(request):
    if request.method == 'GET':
        filter = request.GET['filter']
        responseList = []

        print('filter >> ',filter)

        if(filter.strip() == 'Today'):
            todays_date = date.today()
            totalCustomer = Customers.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day)).using('analytics')
            totalPlacedOrders = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day)).using('analytics')
            todayTotalOrdersAmount = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day)).using('analytics').aggregate(Sum('grand_total'))
            todayTotalOrdersRevenue = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day),delivery_status='cancelled').using('analytics').aggregate(Sum('grand_total'))

            # =================================================================================================
            if(todayTotalOrdersRevenue['grand_total__sum'] == None):
                totalTodayRevenue = float(todayTotalOrdersAmount['grand_total__sum'])
            else:
                totalTodayRevenue = float(todayTotalOrdersAmount['grand_total__sum']) - float(todayTotalOrdersRevenue['grand_total__sum'])
    
            
            context = {}
            context['totalCustomer'] = len(totalCustomer)
            context['totalOrders'] = len(totalPlacedOrders)
            context['totalRevenue'] = totalTodayRevenue
            print('context >> ',context)
            responseList.append(context)

        elif(filter.strip() == 'All Time'):
            context = {}
            context['totalCustomer'] = request.session['totalCustomer']
            context['totalOrders'] = request.session['totalOrders']
            context['totalRevenue'] = request.session['totalRevenue']
            responseList.append(context)
            
        elif(filter.strip() == 'Last 7 Days'):
            d=date.today()-timedelta(days=7)
            totalCustomer = Customers.objects.filter(created_at__gte=d).using('analytics')
            totalPlacedOrders = Orders.objects.filter(created_at__gte=datetime.date(d.year, d.month, d.day)).using('analytics')
            todayTotalOrdersAmount = Orders.objects.filter(created_at__gte=datetime.date(d.year, d.month, d.day)).using('analytics').aggregate(Sum('grand_total'))
            todayTotalOrdersRevenue = Orders.objects.filter(created_at__gte=datetime.date(d.year, d.month, d.day),delivery_status='cancelled').using('analytics').aggregate(Sum('grand_total'))

            # =================================================================================================
            if(todayTotalOrdersRevenue['grand_total__sum'] == None):
                totalTodayRevenue = float(todayTotalOrdersAmount['grand_total__sum'])
            else:
                totalTodayRevenue = float(todayTotalOrdersAmount['grand_total__sum']) - float(todayTotalOrdersRevenue['grand_total__sum'])
    
            
            context = {}
            context['totalCustomer'] = len(totalCustomer)
            context['totalOrders'] = len(totalPlacedOrders)
            context['totalRevenue'] = totalTodayRevenue
            responseList.append(context)


        elif(filter.strip() == 'Current Month'):
            today = datetime.date.today()
            totalCustomer = Customers.objects.filter(created_at__year=today.year,created_at__month=today.month).using('analytics')
            todayTotalOrders = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month).using('analytics')
            todayTotalOrdersAmount = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month).using('analytics').aggregate(Sum('grand_total'))
            todayTotalOrdersRevenue = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month,delivery_status='cancelled').using('analytics').aggregate(Sum('grand_total'))

            # =================================================================================================
            if(todayTotalOrdersRevenue['grand_total__sum'] == None):
                totalTodayRevenue = float(todayTotalOrdersAmount['grand_total__sum'])
            else:
                totalTodayRevenue = float(todayTotalOrdersAmount['grand_total__sum']) - float(todayTotalOrdersRevenue['grand_total__sum'])
            
            context = {}
            context['totalCustomer'] = len(totalCustomer)
            context['totalOrders'] = len(todayTotalOrders)
            context['totalRevenue'] = totalTodayRevenue
            responseList.append(context)

        elif(filter.strip() == 'Last Month'):
            today = datetime.date.today()
            totalCustomer = Customers.objects.filter(created_at__year=today.year,created_at__month=today.month-1).using('analytics')
            todayTotalOrders = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month-1).using('analytics')
            todayTotalOrdersAmount = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month-1,).using('analytics').aggregate(Sum('grand_total'))
            todayTotalOrdersRevenue = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month-1,delivery_status='cancelled').using('analytics').aggregate(Sum('grand_total'))

            # =================================================================================================
            if(todayTotalOrdersRevenue['grand_total__sum'] == None):
                totalTodayRevenue = float(todayTotalOrdersAmount['grand_total__sum'])
            else:
                totalTodayRevenue = float(todayTotalOrdersAmount['grand_total__sum']) - float(todayTotalOrdersRevenue['grand_total__sum'])
            
            context = {}
            context['totalCustomer'] = len(totalCustomer)
            context['totalOrders'] = len(todayTotalOrders)
            context['totalRevenue'] = totalTodayRevenue
            responseList.append(context)
        else:
            pass


        return JsonResponse(responseList, safe=False)
# ==============================================================================================================================================================
@login_required(login_url="/login/")
def master_filter_2(request):
    if request.method == 'GET':
        filter = request.GET['filter']
        responseList = []

        print('filter >> ',filter)

        if(filter.strip() == 'Today'):
            todays_date = date.today()
            totalPlacedOrders = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day)).using('analytics')
            todayTotalOrdersAmount = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day)).using('analytics').aggregate(Sum('grand_total'))
            todayTotalOrdersRevenue = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day),delivery_status='cancelled').using('analytics').aggregate(Sum('grand_total'))

            # =================================================================================================
            if(todayTotalOrdersRevenue['grand_total__sum'] == None):
                totalTodayRevenue = float(todayTotalOrdersAmount['grand_total__sum'])
            else:
                totalTodayRevenue = float(todayTotalOrdersAmount['grand_total__sum']) - float(todayTotalOrdersRevenue['grand_total__sum'])
    
            
            context = {}
            context['totalOrders'] = len(totalPlacedOrders)
            context['totalRevenue'] = totalTodayRevenue
            print('context >> ',context)
            responseList.append(context)

        elif(filter.strip() == 'All Time'):
            context = {}
            context['totalOrders'] = request.session['totalOrders']
            context['totalRevenue'] = request.session['totalRevenue']
            responseList.append(context)
            
        elif(filter.strip() == 'Last 7 Days'):
            d=date.today()-timedelta(days=7)
            totalPlacedOrders = Orders.objects.filter(created_at__gte=datetime.date(d.year, d.month, d.day)).using('analytics')
            todayTotalOrdersAmount = Orders.objects.filter(created_at__gte=datetime.date(d.year, d.month, d.day)).using('analytics').aggregate(Sum('grand_total'))
            todayTotalOrdersRevenue = Orders.objects.filter(created_at__gte=datetime.date(d.year, d.month, d.day),delivery_status='cancelled').using('analytics').aggregate(Sum('grand_total'))

            # =================================================================================================
            if(todayTotalOrdersRevenue['grand_total__sum'] == None):
                totalTodayRevenue = float(todayTotalOrdersAmount['grand_total__sum'])
            else:
                totalTodayRevenue = float(todayTotalOrdersAmount['grand_total__sum']) - float(todayTotalOrdersRevenue['grand_total__sum'])
    
            
            context = {}
            context['totalOrders'] = len(totalPlacedOrders)
            context['totalRevenue'] = totalTodayRevenue
            responseList.append(context)


        elif(filter.strip() == 'Current Month'):
            today = datetime.date.today()
            todayTotalOrders = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month).using('analytics')
            todayTotalOrdersAmount = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month).using('analytics').aggregate(Sum('grand_total'))
            todayTotalOrdersRevenue = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month,delivery_status='cancelled').using('analytics').aggregate(Sum('grand_total'))

            # =================================================================================================
            if(todayTotalOrdersRevenue['grand_total__sum'] == None):
                totalTodayRevenue = float(todayTotalOrdersAmount['grand_total__sum'])
            else:
                totalTodayRevenue = float(todayTotalOrdersAmount['grand_total__sum']) - float(todayTotalOrdersRevenue['grand_total__sum'])
            
            context = {}
            context['totalOrders'] = len(todayTotalOrders)
            context['totalRevenue'] = totalTodayRevenue
            responseList.append(context)

        elif(filter.strip() == 'Last Month'):
            today = datetime.date.today()
            todayTotalOrders = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month-1).using('analytics')
            todayTotalOrdersAmount = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month-1,).using('analytics').aggregate(Sum('grand_total'))
            todayTotalOrdersRevenue = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month-1,delivery_status='cancelled').using('analytics').aggregate(Sum('grand_total'))

            # =================================================================================================
            if(todayTotalOrdersRevenue['grand_total__sum'] == None):
                totalTodayRevenue = float(todayTotalOrdersAmount['grand_total__sum'])
            else:
                totalTodayRevenue = float(todayTotalOrdersAmount['grand_total__sum']) - float(todayTotalOrdersRevenue['grand_total__sum'])
            
            context = {}
            context['totalOrders'] = len(todayTotalOrders)
            context['totalRevenue'] = totalTodayRevenue
            responseList.append(context)
        else:
            pass


        return JsonResponse(responseList, safe=False)
# ==============================================================================================================================================================
@login_required(login_url="/login/")
def master_filter(request):
    if request.method == 'GET':
        filter = request.GET['filter']
        responseList = []

        print('filter >> ',filter)

        if(filter.strip() == 'Today'):
            todays_date = date.today()
            todayTotalOrders = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day)).using('analytics')
            totalPlacedOrders_today = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day),seller_id__isnull=True).using('analytics')
            failedOrders_today = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day),delivery_status='failed').using('analytics')
            ProcessedOrders_today = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day),delivery_status='process').using('analytics')
            shippedOrders_today = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day),delivery_status='shipped').using('analytics')
            cancelledOrders_today = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day),delivery_status='cancelled').using('analytics')
            # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            totalCustomer = Customers.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day)).using('analytics')
            totalPlacedOrders = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day)).using('analytics')
            todayTotalOrdersAmount = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day)).using('analytics').aggregate(Sum('grand_total'))
            todayTotalOrdersRevenue = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day),delivery_status='cancelled').using('analytics').aggregate(Sum('grand_total'))

            if(todayTotalOrdersRevenue['grand_total__sum'] == None):
                totalTodayRevenue = float(todayTotalOrdersAmount['grand_total__sum'])
            else:
                totalTodayRevenue = float(todayTotalOrdersAmount['grand_total__sum']) - float(todayTotalOrdersRevenue['grand_total__sum'])
            # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


            # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            context = {}
            context['todayTotalOrders'] = len(todayTotalOrders)
            context['totalPlacedOrders_today'] = len(totalPlacedOrders_today)
            context['failedOrders_today'] = len(failedOrders_today)
            context['ProcessedOrders_today'] = len(ProcessedOrders_today)
            context['shippedOrders_today'] = len(shippedOrders_today)
            context['cancelledOrders_today'] = len(cancelledOrders_today)
            # ==============================================================================
            context['totalCustomer'] = len(totalCustomer)
            context['totalOrders'] = len(totalPlacedOrders)
            context['totalRevenue'] = round(totalTodayRevenue,2)
            # ==============================================================================


            # ==============================================================================
            responseList.append(context)



        elif(filter.strip() == 'All Time'):
            todayTotalOrders = Orders.objects.all().using('analytics')
            totalPlacedOrders_today = Orders.objects.filter(seller_id__isnull=True).using('analytics')
            failedOrders_today = Orders.objects.filter(delivery_status='failed').using('analytics')
            ProcessedOrders_today = Orders.objects.filter(delivery_status='process').using('analytics')
            shippedOrders_today = Orders.objects.filter(delivery_status='shipped').using('analytics')
            cancelledOrders_today = Orders.objects.filter(delivery_status='cancelled').using('analytics')

            totalCustomer = Customers.objects.all().using('analytics')
            totalPlacedOrders = Orders.objects.all().using('analytics')
            todayTotalOrdersAmount = Orders.objects.all().using('analytics').aggregate(Sum('grand_total'))
            todayTotalOrdersRevenue = Orders.objects.filter(delivery_status='cancelled').using('analytics').aggregate(Sum('grand_total'))

            if(todayTotalOrdersRevenue['grand_total__sum'] == None):
                totalTodayRevenue = float(todayTotalOrdersAmount['grand_total__sum'])
            else:
                totalTodayRevenue = float(todayTotalOrdersAmount['grand_total__sum']) - float(todayTotalOrdersRevenue['grand_total__sum'])
            
            context = {}
            context['todayTotalOrders'] = len(todayTotalOrders)
            context['totalPlacedOrders_today'] = len(totalPlacedOrders_today)
            context['failedOrders_today'] = len(failedOrders_today)
            context['ProcessedOrders_today'] = len(ProcessedOrders_today)
            context['shippedOrders_today'] = len(shippedOrders_today)
            context['cancelledOrders_today'] = len(cancelledOrders_today)

            context['totalCustomer'] = len(totalCustomer)
            context['totalOrders'] = len(totalPlacedOrders)
            context['totalRevenue'] = round(totalTodayRevenue,2)
            responseList.append(context)

            
        elif(filter.strip() == 'Last 7 Days'):
            d=date.today()-timedelta(days=7)
            todayTotalOrders = Orders.objects.filter(created_at__gte=d).using('analytics')
            totalPlacedOrders_today = Orders.objects.filter(created_at__gte=d,seller_id__isnull=True).using('analytics')
            failedOrders_today = Orders.objects.filter(created_at__gte=d,delivery_status='failed').using('analytics')
            ProcessedOrders_today = Orders.objects.filter(created_at__gte=d,delivery_status='process' or 'pending').using('analytics')
            shippedOrders_today = Orders.objects.filter(created_at__gte=d,delivery_status='shipped').using('analytics')
            cancelledOrders_today = Orders.objects.filter(created_at__gte=d,delivery_status='cancelled').using('analytics')
            # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            totalCustomer = Customers.objects.filter(created_at__gte=d).using('analytics')
            totalPlacedOrders = Orders.objects.filter(created_at__gte=datetime.date(d.year, d.month, d.day)).using('analytics')
            todayTotalOrdersAmount = Orders.objects.filter(created_at__gte=datetime.date(d.year, d.month, d.day)).using('analytics').aggregate(Sum('grand_total'))
            todayTotalOrdersRevenue = Orders.objects.filter(created_at__gte=datetime.date(d.year, d.month, d.day),delivery_status='cancelled').using('analytics').aggregate(Sum('grand_total'))

            # =================================================================================================
            if(todayTotalOrdersRevenue['grand_total__sum'] == None):
                totalTodayRevenue = float(todayTotalOrdersAmount['grand_total__sum'])
            else:
                totalTodayRevenue = float(todayTotalOrdersAmount['grand_total__sum']) - float(todayTotalOrdersRevenue['grand_total__sum'])
            # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            
            # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            context = {}
            context['todayTotalOrders'] = len(todayTotalOrders)
            context['totalPlacedOrders_today'] = len(totalPlacedOrders_today)
            context['failedOrders_today'] = len(failedOrders_today)
            context['ProcessedOrders_today'] = len(ProcessedOrders_today)
            context['shippedOrders_today'] = len(shippedOrders_today)
            context['cancelledOrders_today'] = len(cancelledOrders_today)
            # ==============================================================================
            context['totalCustomer'] = len(totalCustomer)
            context['totalOrders'] = len(totalPlacedOrders)
            context['totalRevenue'] = round(totalTodayRevenue,2)
            # ==============================================================================


            # ==============================================================================
            responseList.append(context)


        elif(filter.strip() == 'Current Month'):
            today = datetime.date.today()
            todayTotalOrders = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month).using('analytics')
            totalPlacedOrders_today = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month,seller_id__isnull=True).using('analytics')
            failedOrders_today = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month,delivery_status='failed').using('analytics')
            ProcessedOrders_today = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month,delivery_status='process').using('analytics')
            shippedOrders_today = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month,delivery_status='shipped').using('analytics')
            cancelledOrders_today = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month,delivery_status='cancelled').using('analytics')
            # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            totalCustomer = Customers.objects.filter(created_at__year=today.year,created_at__month=today.month).using('analytics')
            todayTotalOrders = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month).using('analytics')
            todayTotalOrdersAmount = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month).using('analytics').aggregate(Sum('grand_total'))
            todayTotalOrdersRevenue = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month,delivery_status='cancelled').using('analytics').aggregate(Sum('grand_total'))

            # =================================================================================================
            if(todayTotalOrdersRevenue['grand_total__sum'] == None):
                totalTodayRevenue = float(todayTotalOrdersAmount['grand_total__sum'])
            else:
                totalTodayRevenue = float(todayTotalOrdersAmount['grand_total__sum']) - float(todayTotalOrdersRevenue['grand_total__sum'])
            # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            context = {}
            context['todayTotalOrders'] = len(todayTotalOrders)
            context['totalPlacedOrders_today'] = len(totalPlacedOrders_today)
            context['failedOrders_today'] = len(failedOrders_today)
            context['ProcessedOrders_today'] = len(ProcessedOrders_today)
            context['shippedOrders_today'] = len(shippedOrders_today)
            context['cancelledOrders_today'] = len(cancelledOrders_today)
            # ==============================================================================
            context['totalCustomer'] = len(totalCustomer)
            context['totalOrders'] = len(todayTotalOrders)
            context['totalRevenue'] = round(totalTodayRevenue,2)
            # ==============================================================================


            # ==============================================================================
            responseList.append(context)

        elif(filter.strip() == 'Last Month'):
            today = datetime.date.today()
            todayTotalOrders = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month-1).using('analytics')
            totalPlacedOrders_today = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month-1,seller_id__isnull=True).using('analytics')
            failedOrders_today = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month-1,delivery_status='failed').using('analytics')
            ProcessedOrders_today = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month-1,delivery_status='process').using('analytics')
            PendingOrders_today = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month-1,delivery_status='pending').using('analytics')

            shippedOrders_today = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month-1,delivery_status='shipped').using('analytics')
            cancelledOrders_today = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month-1,delivery_status='cancelled').using('analytics')
            # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            totalCustomer = Customers.objects.filter(created_at__year=today.year,created_at__month=today.month-1).using('analytics')
            todayTotalOrders = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month-1).using('analytics')
            todayTotalOrdersAmount = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month-1,).using('analytics').aggregate(Sum('grand_total'))
            todayTotalOrdersRevenue = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month-1,delivery_status='cancelled').using('analytics').aggregate(Sum('grand_total'))

            # =================================================================================================
            if(todayTotalOrdersRevenue['grand_total__sum'] == None):
                totalTodayRevenue = float(todayTotalOrdersAmount['grand_total__sum'])
            else:
                totalTodayRevenue = float(todayTotalOrdersAmount['grand_total__sum']) - float(todayTotalOrdersRevenue['grand_total__sum'])
            # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            context = {}
            context['todayTotalOrders'] = len(todayTotalOrders)
            context['totalPlacedOrders_today'] = len(totalPlacedOrders_today)
            context['failedOrders_today'] = len(failedOrders_today)
            context['ProcessedOrders_today'] = len(ProcessedOrders_today)+len(PendingOrders_today)
            context['shippedOrders_today'] = len(shippedOrders_today)
            context['cancelledOrders_today'] = len(cancelledOrders_today)
            # ==============================================================================
            context['totalCustomer'] = len(totalCustomer)
            context['totalOrders'] = len(todayTotalOrders)
            context['totalRevenue'] = round(totalTodayRevenue,2)
            # ==============================================================================


            # ==============================================================================
            responseList.append(context)
        else:
            pass


        return JsonResponse(responseList, safe=False)
# ==============================================================================================================================================================
@login_required(login_url="/login/")
def categrory(request):
    if request.method == 'GET':
        todays_date = date.today()
        responseList = []
        responseList2 = []
        mainList = []

        wC_wear = 0
        mC_wear = 0
        hDecor = 0
        premium = 0

        wC_wear_sales = 0
        mC_wear_sales = 0
        hDecor_sales = 0
        premium_sales = 0

        
        catTotalOrder = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day)).using('analytics')
        for i in catTotalOrder:
            user = i.user_id
            OrderInfo = OrderDetails.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day),order_id=i.id).using('analytics')
            for j in OrderInfo:
                category = Products.objects.filter(id = j.product_id).using('analytics')
                if(category[0].category_id == 1):
                    wC_wear = wC_wear + 1
                    wC_wear_sales = wC_wear_sales + float(j.price)
                elif(category[0].category_id == 2):
                    mC_wear = mC_wear + 1
                    mC_wear_sales = mC_wear_sales + float(j.price)
                elif(category[0].category_id == 3):
                    hDecor = hDecor + 1
                    hDecor_sales = hDecor_sales + float(j.price)
                elif(category[0].category_id == 4):
                    premium = premium + 1
                    premium_sales = premium_sales + float(j.price)
        responseList.append(wC_wear)
        responseList.append(mC_wear)
        responseList.append(hDecor)
        responseList.append(premium)

        responseList2.append(wC_wear_sales)
        responseList2.append(mC_wear_sales)
        responseList2.append(hDecor_sales)
        responseList2.append(premium_sales)

        mainList.extend(responseList)

        dataArray = {
            'soldOut' : responseList,
            'sales' : responseList2
        }
        print('dataArray ::>> ',dataArray)

        return JsonResponse(dataArray, safe=False)


# =========================================================================================================================================================
@login_required(login_url="/login/")
def category_filter(request):
    if request.method == 'GET':
        filter = request.GET['filter']
        todays_date = date.today()
        responseList = []
        responseList2 = []
        mainList = []

        wC_wear = 0
        mC_wear = 0
        hDecor = 0
        premium = 0

        wC_wear_sales = 0
        mC_wear_sales = 0
        hDecor_sales = 0
        premium_sales = 0
        print('filter >> ',filter)

        if(filter.strip() == 'Today'):
            catTotalOrder = Orders.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day)).using('analytics')
            print('catTotalOrder >>> ',len(catTotalOrder))
            count = 0
            for i in catTotalOrder:
                user = i.user_id
                OrderInfo = OrderDetails.objects.filter(created_at__gte=datetime.date(todays_date.year, todays_date.month, todays_date.day),order_id=i.id).using('analytics')
                for j in OrderInfo:
                    category = Products.objects.filter(id = j.product_id).using('analytics')
                    for k in category:
                        if(k.category_id == 1):
                            wC_wear = wC_wear + 1
                            wC_wear_sales = wC_wear_sales + float(j.price)
                        elif(k.category_id == 2):
                            mC_wear = mC_wear + 1
                            mC_wear_sales = mC_wear_sales + float(j.price)
                        elif(k.category_id == 3):
                            hDecor = hDecor + 1
                            hDecor_sales = hDecor_sales + float(j.price)
                        elif(k.category_id == 4):
                            premium = premium + 1
                            premium_sales = premium_sales + float(j.price)
            responseList.append(wC_wear)
            responseList.append(mC_wear)
            responseList.append(hDecor)
            responseList.append(premium)

            responseList2.append(wC_wear_sales)
            responseList2.append(mC_wear_sales)
            responseList2.append(hDecor_sales)
            responseList2.append(premium_sales)

            mainList.extend(responseList)

            dataArray = {
                'soldOut' : responseList,
                'sales' : responseList2
            }
            print('dataArray ::>> ',dataArray)


        elif(filter.strip() == 'All Time'):
            catTotalOrder = Orders.objects.all().using('analytics')
            print('catTotalOrder >>> ',len(catTotalOrder))
            count = 0
            for i in catTotalOrder:
                user = i.user_id
                OrderInfo = OrderDetails.objects.filter(order_id=i.id).using('analytics')
                for j in OrderInfo:
                    category = Products.objects.filter(id = j.product_id).using('analytics')
                    for k in category:
                        if(k.category_id == 1):
                            wC_wear = wC_wear + 1
                            wC_wear_sales = wC_wear_sales + float(j.price)
                        elif(k.category_id == 2):
                            mC_wear = mC_wear + 1
                            mC_wear_sales = mC_wear_sales + float(j.price)
                        elif(k.category_id == 3):
                            hDecor = hDecor + 1
                            hDecor_sales = hDecor_sales + float(j.price)
                        elif(k.category_id == 4):
                            premium = premium + 1
                            premium_sales = premium_sales + float(j.price)
                    print(count)
                    count = count + 1
            responseList.append(wC_wear)
            responseList.append(mC_wear)
            responseList.append(hDecor)
            responseList.append(premium)

            responseList2.append(wC_wear_sales)
            responseList2.append(mC_wear_sales)
            responseList2.append(hDecor_sales)
            responseList2.append(premium_sales)

            mainList.extend(responseList)

            dataArray = {
                'soldOut' : responseList,
                'sales' : responseList2
            }
            print('dataArray ::>> ',dataArray)

            
        elif(filter.strip() == 'Last 7 Days'):
            d=date.today()-timedelta(days=7)
            catTotalOrder = Orders.objects.filter(created_at__gte=datetime.date(d.year, d.month, d.day)).using('analytics')
            print('catTotalOrder >>> ',len(catTotalOrder))
            count = 0
            for i in catTotalOrder:
                user = i.user_id
                
                OrderInfo = OrderDetails.objects.filter(created_at__gte=datetime.date(d.year, d.month, d.day),order_id=i.id).using('analytics')
                for j in OrderInfo:
                    category = Products.objects.filter(id = j.product_id).using('analytics')
                    for k in category:
                        if(k.category_id == 1):
                            wC_wear = wC_wear + 1
                            wC_wear_sales = wC_wear_sales + float(j.price)
                        elif(k.category_id == 2):
                            mC_wear = mC_wear + 1
                            mC_wear_sales = mC_wear_sales + float(j.price)
                        elif(k.category_id == 3):
                            hDecor = hDecor + 1
                            hDecor_sales = hDecor_sales + float(j.price)
                        elif(k.category_id == 4):
                            premium = premium + 1
                            premium_sales = premium_sales + float(j.price)
                print(count)
                count = count + 1

            responseList.append(wC_wear)
            responseList.append(mC_wear)
            responseList.append(hDecor)
            responseList.append(premium)

            responseList2.append(wC_wear_sales)
            responseList2.append(mC_wear_sales)
            responseList2.append(hDecor_sales)
            responseList2.append(premium_sales)

            mainList.extend(responseList)

            dataArray = {
                'soldOut' : responseList,
                'sales' : responseList2
            }
            print('dataArray ::>> ',dataArray)


        elif(filter.strip() == 'Current Month'):
            today = datetime.date.today()
            catTotalOrder = Orders.objects.filter(created_at__year=today.year,created_at__month=today.month).using('analytics')
            print('catTotalOrder >>> ',len(catTotalOrder))
            count = 0
            for i in catTotalOrder:
                user = i.user_id
                OrderInfo = OrderDetails.objects.filter(created_at__year=today.year,created_at__month=today.month,order_id=i.id).using('analytics')
                for j in OrderInfo:
                    category = Products.objects.filter(id = j.product_id).using('analytics')
                    for k in category:
                        if(k.category_id == 1):
                            wC_wear = wC_wear + 1
                            wC_wear_sales = wC_wear_sales + float(j.price)
                        elif(k.category_id == 2):
                            mC_wear = mC_wear + 1
                            mC_wear_sales = mC_wear_sales + float(j.price)
                        elif(k.category_id == 3):
                            hDecor = hDecor + 1
                            hDecor_sales = hDecor_sales + float(j.price)
                        elif(k.category_id == 4):
                            premium = premium + 1
                            premium_sales = premium_sales + float(j.price)
                print(count)
                count = count + 1
            responseList.append(wC_wear)
            responseList.append(mC_wear)
            responseList.append(hDecor)
            responseList.append(premium)

            responseList2.append(wC_wear_sales)
            responseList2.append(mC_wear_sales)
            responseList2.append(hDecor_sales)
            responseList2.append(premium_sales)

            mainList.extend(responseList)

            dataArray = {
                'soldOut' : responseList,
                'sales' : responseList2
            }
            print('dataArray ::>> ',dataArray)

        elif(filter.strip() == 'Last Month'):
            catTotalOrder = Orders.objects.filter(created_at__year=todays_date.year,created_at__month=todays_date.month-1).using('analytics')
            print('catTotalOrder >>> ',len(catTotalOrder))
            count = 0
            for i in catTotalOrder:
                user = i.user_id
                OrderInfo = OrderDetails.objects.filter(created_at__year=todays_date.year,created_at__month=todays_date.month-1,order_id=i.id).using('analytics')
                for j in OrderInfo:
                    category = Products.objects.filter(id = j.product_id).using('analytics')
                    for k in category:
                        if(k.category_id == 1):
                            wC_wear = wC_wear + 1
                            wC_wear_sales = wC_wear_sales + float(j.price)
                        elif(k.category_id == 2):
                            mC_wear = mC_wear + 1
                            mC_wear_sales = mC_wear_sales + float(j.price)
                        elif(k.category_id == 3):
                            hDecor = hDecor + 1
                            hDecor_sales = hDecor_sales + float(j.price)
                        elif(k.category_id == 4):
                            premium = premium + 1
                            premium_sales = premium_sales + float(j.price)
                print(count)
                count = count + 1
            responseList.append(wC_wear)
            responseList.append(mC_wear)
            responseList.append(hDecor)
            responseList.append(premium)

            responseList2.append(wC_wear_sales)
            responseList2.append(mC_wear_sales)
            responseList2.append(hDecor_sales)
            responseList2.append(premium_sales)

            mainList.extend(responseList)

            dataArray = {
                'soldOut' : responseList,
                'sales' : responseList2
            }
            print('dataArray ::>> ',dataArray)

        else:
            dataArray = {}
        
        return JsonResponse(dataArray, safe=False)
