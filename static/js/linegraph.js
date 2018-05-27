$(document).ready(function(){
	$.ajax({
		url : "http://192.168.1.166/test/chartjs/php-mysql-chartjs/data1.php",
		type : "GET",
		crossDomain: true,
		success : function(data){
			console.log(data);

				var testid = [];
				var readspeed = [];
				var writespeed = [];

				for(var i in data) {
					testid.push("Test ID " + data[i].test_id);
					readspeed.push(data[i].read_speed);
					writespeed.push(data[i].write_speed);
				}

			var chdata1 = {
				labels: testid,
				datasets: [
					{
						label: "Read Speed (in Mbps)",
						fill: false,
						lineTension: 0,
						backgroundColor: "rgba(59, 89, 152, 0.75)",
						borderColor: "rgba(59, 89, 152, 1)",
						pointHoverBackgroundColor: "rgba(59, 89, 152, 1)",
						pointHoverBorderColor: "rgba(59, 89, 152, 1)",
						data: readspeed
					}
				]
			};
			var chdata2 = {
				labels: testid,
				datasets: [
					{
						label: "Write Speed (in Mbps)",
						fill: false,
						lineTension: 0,
						backgroundColor: "rgba(29, 202, 255, 0.75)",
						borderColor: "rgba(29, 202, 255, 1)",
						pointHoverBackgroundColor: "rgba(29, 202, 255, 1)",
						pointHoverBorderColor: "rgba(29, 202, 255, 1)",
						data: writespeed
					}
				]
			};
			var options1 = {
				title: {
					display: true,
					position: "top",
					responsive: true,
					text: "Test Results - Read Speed",
					fontSize: 18,
					fontColor: "#111"
					},
					legend: {
						display: true,
						position: "bottom"
						}
					};
			var options2 = {
				title: {
					display: true,
					position: "top",
					responsive: true,
					text: "Test Results - Write Speed",
					fontSize: 18,
					fontColor: "#111"
					},
					legend: {
						display: true,
						position: "bottom"
						}
					};

			var ctx1 = document.getElementById("myChart1");
			var ctx2 = document.getElementById("myChart2");

			var chart1 = new Chart(ctx1, {
				type: 'line',
				data: chdata1,
				options: options1
			});
			var chart2 = new Chart(ctx2, {
				type: 'line',
				data: chdata2,
				options: options2
			});
		},
		error : function(data) {

		}
	});
});
