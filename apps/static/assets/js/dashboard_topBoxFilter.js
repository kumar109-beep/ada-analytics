// =========================================================================================================
//                                        FILTER FOR TOTAL ORDERS
// =========================================================================================================
function masterFilter1(){
    // return false;
    var selectedParam = $('#masterFilter_1').val().trim();
    console.log(selectedParam);
    $('#masterDiv1').css('opacity',0.5);
    $('#masterDiv1').css('cursor','not-allowed');
    $('#masterDiv1').css('pointer-events','none');
    $('.masterDiv1').text('-');

    // ---------    AJAX CALL   -------------
    $.ajax({
        type: 'GET',
        url: "/dashboard-filter/master-filter-1",
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

            }else{
                alert('Under Development!');
                $('#masterDiv1').css('opacity',1);
                $('#masterDiv1').css('cursor','');
                $('#masterDiv1').css('pointer-events','');
                return false;
            }
            
        }
    });
    // --------------------------------------
}
// =========================================================================================================
function masterFilter2(){
    // return false;
    var selectedParam = $('#master_filter_2').val().trim();
    console.log(selectedParam);
    $('#masterDiv2').css('opacity',0.5);
    $('#masterDiv2').css('cursor','not-allowed');
    $('#masterDiv2').css('pointer-events','none');
    $('.masterDiv2').text('-');

    // ---------    AJAX CALL   -------------
    $.ajax({
        type: 'GET',
        url: "/dashboard-filter/master-filter-2",
        data: {'filter': selectedParam},
        success: function (response) {
            console.log(response);
            if(response.length != 0){
                $('#totalTodays_orders-2').text(response[0]['totalOrders']);
                $('#totalTodays_revenue-2').text(response[0]['totalRevenue']);
                $('#totalTodays_orders-2-para').text('Total Orders '+ selectedParam);
                $('#totalTodays_revenue-2-para').text('Total Revenue '+ selectedParam);
                $('#masterDiv2').css('opacity',1);
                $('#masterDiv2').css('cursor','');
                $('#masterDiv2').css('pointer-events','');

            }else{
                alert('Under Development!');
                $('#masterDiv2').css('opacity',1);
                $('#masterDiv2').css('cursor','');
                $('#masterDiv2').css('pointer-events','');
                return false;
            }
            
        }
    });
    // --------------------------------------
}
// =========================================================================================================