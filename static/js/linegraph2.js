$(document).ready(function(){
	$.ajax({
		url : "http://192.168.1.166/test/chartjs/php-mysql-chartjs/data2.php",
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

			var chdata3 = {
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
			var chdata4 = {
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
			var options3 = {
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
			var options4 = {
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

			var ctx3 = document.getElementById("myChart3");
			var ctx4 = document.getElementById("myChart4");

			var chart3 = new Chart(ctx3, {
				type: 'line',
				data: chdata3,
				options: options3
			});
			var chart4 = new Chart(ctx4, {
				type: 'line',
				data: chdata4,
				options: options4
			});
		},
		error : function(data) {

		}
	});
});
