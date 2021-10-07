// =========================================================================================================
//                                        FILTER FOR TOTAL ORDERS
// =========================================================================================================
function filter_total_orders(){
    var selectedParam = $('#totalOrderFilter').val().trim();
    console.log(selectedParam);
    $('#totalOrderFilterdiv').css('opacity',0.5);
    $('#totalOrderFilter').css('cursor','not-allowed');
    $('#totalOrderFilter').css('pointer-events','none');
    $('.total_order_filter').text('-');

    // ---------    AJAX CALL   -------------
    $.ajax({
        type: 'GET',
        url: "/dashboard-filter/total-order",
        data: {'filter': selectedParam},
        success: function (response) {
            console.log(response);
            if(response.length != 0){
                $('#total_order_total').text(response[0]['todayTotalOrders']);
                $('#total_order_created').text(response[0]['totalPlacedOrders_today']);
                $('#total_order_failed').text(response[0]['failedOrders_today']);
                $('#total_order_procesed').text(response[0]['ProcessedOrders_today']);
                $('#total_order_open').text(response[0]['shippedOrders_today']);
                $('#total_order_cancelled').text(response[0]['cancelledOrders_today']);
                $('#totalOrderFilterdiv').css('opacity',1);
                $('#totalOrderFilter').css('cursor','');
                $('#totalOrderFilter').css('pointer-events','');

            }else{
                alert('Under Development!');
                $('#totalOrderFilterdiv').css('opacity',1);
                $('#totalOrderFilter').css('cursor','');
                $('#totalOrderFilter').css('pointer-events','');
                return false;
            }
            
        }
    });
    // --------------------------------------
}
// =========================================================================================================
//                                        REVENUE GRAPH
// =========================================================================================================
$( document ).ready(function() {    
// -------------------AJAX CALL---------------------------
var revenueArray = [];
var catSoldQuantityArray = [];
$.ajax({
    type: 'GET',
    url: "/dashboard-filter/revenue",
    success: function (response) {
        console.log(response);

        // Variables
    var $chart = $('#chart-sales-dark');
    // Methods
    function init($chart) {
  
      var salesChart = new Chart($chart, {
        type: 'line',
        options: {
          scales: {
            yAxes: [{
              gridLines: {
                lineWidth: 1,
                color: Charts.colors.gray[900],
                zeroLineColor: Charts.colors.gray[900]
              },
              ticks: {
                callback: function(value) {
                  if (!(value % 10)) {
                    return '₹ ' + value;
                  }
                }
              }
            }]
          },
          tooltips: {
            callbacks: {
              label: function(item, data) {
                var label = data.datasets[item.datasetIndex].label || '';
                var yLabel = item.yLabel;
                var content = '';
  
                if (data.datasets.length > 1) {
                  content += '<span class="popover-body-label mr-auto">' + label + '</span>';
                }
  
                content += '₹ ' + yLabel;
                return content;
              }
            }
          }
        },
        data: {
          labels: ['Jan','Feb','Mar','Apr','May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
          datasets: [{
            label: 'Performance',
            // data: [10,20,15,40, 20, 10, 30, 15, 40, 0, 0, 100]
            data : response
          }]
        }
      });
  
      // Save to jQuery object
  
      $chart.data('chart', salesChart);
  
    };
  
  
    // Events
  
    if ($chart.length) {
      init($chart);
    }
    }
}).then(function(){
  // console.log('hello world');
  $.ajax({
    type: 'GET',
    url: "/dashboard-filter/categrory",
    success: function (response) {
        console.log(response);
        $('#cat-spinner').css('display','none');
        $('#cat-filter').css('display','');
        
        var $chart = $('#chart-bars');
        // Init chart
        function initChart($chart) {

        // 	// Create chart
        	var ordersChart = new Chart($chart, {
        		type: 'bar',
        		data: {
        			labels: ['Women Chikan Wear', 'Men Chikan Wear', 'Home Decor', 'Premium'],
        			datasets: [{
        				label: 'No. of units',
        				// data: [200, 100, 300, 220]
                data : response['soldOut']
        			},
        			{
        				label: 'Amount',
        				// data: [40, 20, 60, 44],
                data : response['sales'],
        				backgroundColor: [
        					'rgba(75, 192, 192, 0.2)',
        					'rgba(75, 192, 192, 0.2)',
        					'rgba(75, 192, 192, 0.2)',
        					'rgba(75, 192, 192, 0.2)'
        				],
        				borderColor: [
        					'rgba(75, 192, 192, 0.2)',
        					'rgba(75, 192, 192, 0.2)',
        					'rgba(75, 192, 192, 0.2)',
        					'rgba(75, 192, 192, 0.2)'
        				],
        				borderWidth: 1,
        				maxBarThickness: 18,
        			}]
        		}
        	});

        // 	// Save to jQuery object
        	$chart.data('chart', ordersChart);
        }

        // Init chart
        if ($chart.length) {
        	initChart($chart);
        }
    }
})

})


})

// ========================================================================================================================================
function geRevenuetGraphData(){
    $('#revenueGraphDiv').css('opacity',0.5);
    $('#revenueGraphDiv').css('pointer-events','none');
    var year = $('#revenueYear').val().trim();

    if(year == '2021'){
        // -------------------AJAX CALL---------------------------
    var revenueArray = [];
    $.ajax({
        type: 'GET',
        url: "/dashboard-filter/revenue",
        success: function (response) {
            console.log(response);

            // Variables
        var $chart = $('#chart-sales-dark');
        // Methods
        function init($chart) {
    
        var salesChart = new Chart($chart, {
            type: 'line',
            options: {
            scales: {
                yAxes: [{
                gridLines: {
                    lineWidth: 1,
                    color: Charts.colors.gray[900],
                    zeroLineColor: Charts.colors.gray[900]
                },
                ticks: {
                    callback: function(value) {
                    if (!(value % 10)) {
                        return '₹ ' + value;
                    }
                    }
                }
                }]
            },
            tooltips: {
                callbacks: {
                label: function(item, data) {
                    var label = data.datasets[item.datasetIndex].label || '';
                    var yLabel = item.yLabel;
                    var content = '';
    
                    if (data.datasets.length > 1) {
                    content += '<span class="popover-body-label mr-auto">' + label + '</span>';
                    }
    
                    content += '₹ ' + yLabel;
                    return content;
                }
                }
            }
            },
            data: {
            labels: ['Jan','Feb','Mar','Apr','May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            datasets: [{
                label: 'Performance',
                // data: [10,20,15,40, 20, 10, 30, 15, 40, 0, 0, 100]
                data : response
            }]
            }
        });
    
        // Save to jQuery object
    
        $chart.data('chart', salesChart);
    
        };
    
    
        // Events
    
        if ($chart.length) {
        init($chart);
        }
    
    
            
        }
    });
    $('#revenueGraphDiv').css('opacity',1);
    $('#revenueGraphDiv').css('pointer-events','');
    }
    else{
        setTimeout(() => {alert('No record available for selected year!');}, 1000);
        $('#revenueYear').val('2021');
        $('#revenueGraphDiv').css('opacity',1);
        $('#revenueGraphDiv').css('pointer-events','');
        return false;
    }
}