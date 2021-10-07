// =========================================================================================================
//                                        FILTER FOR TOTAL ORDERS
// =========================================================================================================
function masterFilter(){
    // return false;
    var selectedParam = $('#masterFilter').val().trim();
    console.log(selectedParam);
    $('#totalOrderFilterdiv').css('opacity',0.5);
    $('#totalOrderFilter').css('cursor','not-allowed');
    $('#totalOrderFilter').css('pointer-events','none');
    $('.total_order_filter').text('-');

    $('#masterDiv1').css('opacity',0.5);
    $('#masterDiv1').css('cursor','not-allowed');
    $('#masterDiv1').css('pointer-events','none');
    $('.masterDiv1').text('-');

    $('#masterDiv2').css('opacity',0.5);
    $('#masterDiv2').css('cursor','not-allowed');
    $('#masterDiv2').css('pointer-events','none');
    $('.masterDiv2').text('-');

    // ---------    AJAX CALL   -------------
    $.ajax({
        type: 'GET',
        url: "/dashboard-filter/master-filter",
        data: {'filter': selectedParam},
        success: function (response) {
            console.log(response);
            if(response.length != 0){
                $('#totalCustomers').text(response[0]['totalCustomer']);
                $('#totalOrders').text(response[0]['totalOrders']);
                $('#total_Reveue').text(response[0]['totalRevenue']);
                $('#masterDiv1').css('opacity',1);
                $('#masterDiv1').css('cursor','');
                $('#masterDiv1').css('pointer-events','');
                $('#masterFilter_1').val(selectedParam);

                $('#total_order_total').text(response[0]['todayTotalOrders']);
                $('#total_order_created').text(response[0]['totalPlacedOrders_today']);
                $('#total_order_failed').text(response[0]['failedOrders_today']);
                $('#total_order_procesed').text(response[0]['ProcessedOrders_today']);
                $('#total_order_open').text(response[0]['shippedOrders_today']);
                $('#total_order_cancelled').text(response[0]['cancelledOrders_today']);
                $('#totalOrderFilterdiv').css('opacity',1);
                $('#totalOrderFilter').css('cursor','');
                $('#totalOrderFilter').css('pointer-events','');
                $('#totalOrderFilter').val(selectedParam);

                $('#totalTodays_orders-2').text(response[0]['totalOrders']);
                $('#totalTodays_revenue-2').text(response[0]['totalRevenue']);
                $('#totalTodays_orders-2-para').text('Total Orders '+ selectedParam);
                $('#totalTodays_revenue-2-para').text('Total Revenue '+ selectedParam);
                $('#masterDiv2').css('opacity',1);
                $('#masterDiv2').css('cursor','');
                $('#masterDiv2').css('pointer-events','');
                $('#master_filter_2').val(selectedParam);

            }else{
                alert('Under Development!');
                $('#totalOrderFilterdiv').css('opacity',1);
                $('#totalOrderFilter').css('cursor','');
                $('#totalOrderFilter').css('pointer-events','');
                $('.total_order_filter').text('-');

                $('#masterDiv1').css('opacity',1);
                $('#masterDiv1').css('cursor','');
                $('#masterDiv1').css('pointer-events','');
                $('.masterDiv1').text('-');

                $('#masterDiv2').css('opacity',1);
                $('#masterDiv2').css('cursor','');
                $('#masterDiv2').css('pointer-events','');
                $('.masterDiv2').text('-');
                return false;
            }
            
        }
    });
    // --------------------------------------
}
// =========================================================================================================