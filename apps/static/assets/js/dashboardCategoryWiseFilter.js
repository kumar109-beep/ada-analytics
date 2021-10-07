function categoryFilter(){
    $('#categoryFilterDiv').css('opacity',0.5);
    $('#categoryFilterDiv').css('pointer-events','none');
    $('#cat-spinner').css('display','');
    $('#cat-filter').css('display','none');
    var selectedParam = $('#cat-filter').val().trim();
    console.log('selected param >>> ',selectedParam);

        // -------------------AJAX CALL---------------------------
    var revenueArray = [];
    $.ajax({
        type: 'GET',
        url: "/dashboard-filter/categrory-filter",
        data : {'filter' : selectedParam},
        success: function (response) {
            console.log(response);

            document.querySelector("#categoryChartCanvasDiv").innerHTML = '<canvas id="chart-bars"></canvas>';
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
        // $chart.update();
        	$chart.data('chart', ordersChart);
        }

        // Init chart
        if ($chart.length) {
        	initChart($chart);
        }
            
        }
    }).then(function(){
        $('#categoryFilterDiv').css('opacity',1);
        $('#categoryFilterDiv').css('pointer-events','');
        $('#cat-spinner').css('display','none');
        $('#cat-filter').css('display','');
    })
}