<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=yes">
        <title>Dashboard</title>      <!-- import plugin script -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <style>
			.chart-container {
				width: auto;
				height: auto;
			}
		</style>
    </head>
    <body>
    <?php
        header('Access-Control-Allow-Origin: *');
        header('Access-Control-Allow-Headers: Cache-Control, Pragma, Origin, Authorization, Content-Type, X-Requested-With');
        header('Access-Control-Allow-Methods: GET, PUT, POST');
    ?>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <script type="text/javascript" src="static/Chart.min.js"></script>
    <script type="text/javascript" src="static/linegraph.js"></script>
    <div class="navbar navbar-inverse">
            <div class="container-fluid">
                            <div class="navbar-header">
                                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#mynavbar">
                                    <span class="icon-bar"></span>
                                    <span class="icon-bar"></span>
                                    <span class="icon-bar"></span>
                                </button>
                                <a class="navbar-brand" href="/"><span class="glyphicon glyphicon-home"></span> Home</a>
                            </div>
                            <div class="collapse navbar-collapse" id="mynavbar">
                                <ul class="nav navbar-nav navbar-right">
                                    <li><a href="/logout"><span class="glyphicon glyphicon-log-out"></span> Logout</a></li>
                                </ul>
                            </div>
            </div>
        </div>

             {% with messages = get_flashed_messages() %}
               {% if messages %}
                  {% for message in messages %}
                    {{ message }}
                  {% endfor %}
               {% endif %}
            {% endwith %}

        <div class="container">
          <h2>Dashboard</h2>
          <ul class="nav nav-tabs">
            <li class="active"><a data-toggle="tab" href="#home">Home</a></li>
            <li><a data-toggle="tab" href="#perfcharts">Perf Test Charts</a></li>
            <li><a data-toggle="tab" href="#menu2">Menu 2</a></li>
            <li><a data-toggle="tab" href="#menu3">Menu 3</a></li>
          </ul>

          <div class="tab-content">
            <div id="home" class="tab-pane fade in active">
              <h3>HOME</h3>
              <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
            </div>
            <div id="perfcharts" class="tab-pane fade">
              <h3>Perf Test Charts</h3>
              <div class="chart-container">
                <canvas id="myChart1"></canvas>
                <canvas id="myChart2"></canvas>
              </div>
            </div>
            <div id="menu2" class="tab-pane fade">
              <h3>Menu 2</h3>
              <p>Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam.</p>
            </div>
            <div id="menu3" class="tab-pane fade">
              <h3>Menu 3</h3>
              <p>Eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.</p>
            </div>
          </div>
        </div>



    </body>
</html>






