<!DOCTYPE html>
<html>
<head>
<title>UTM SPACE BOOKING</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
  <link href="css/style.css"rel="stylesheet"/>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <link href="https://fonts.googleapis.com/css?family=Abril+Fatface" rel="stylesheet">
</head>
<body style="margin-top:50px;">
	<?php
      include('Menu Bar.php')
  ?><br><br><br>
	<div class="container-fluid"style="margin-top:2%;">
		<div class="continer">
			<div class="row">
				<div class="col-sm-2"></div>
				<div class="col-sm-7">
					<div id="myCarousel" class="carousel slide" data-ride="carousel">
  <!-- Indicators -->
  <ol class="carousel-indicators">
    <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
    <li data-target="#myCarousel" data-slide-to="1"></li>
    <li data-target="#myCarousel" data-slide-to="2"></li>
    <li data-target="#myCarousel" data-slide-to="3"></li>
    <li data-target="#myCarousel" data-slide-to="4"></li>
    <li data-target="#myCarousel" data-slide-to="5"></li>
  </ol>

  <!-- Wrapper for slides -->
  <div class="carousel-inner">
    <div class="item active">
      <img src="image/Dewan Banquet Hall/img1.jpg"class="thumbnail" alt="img1">
    </div>

    <div class="item">
      <img src="image/Dewan Banquet Hall/img2.jpg"class="thumbnail" alt="im2">
    </div>

    <div class="item">
       <img src="image/Dewan Banquet Hall/img3.jpg"class="thumbnail" alt="im3">
    </div>

    <div class="item">
       <img src="image/Dewan Banquet Hall/img4.jpg"class="thumbnail" alt="img4">
    </div>

    <div class="item">
       <img src="image/Dewan Banquet Hall/img5.jpg"class="thumbnail" alt="img5">
    </div>

    <div class="item">
       <img src="image/Dewan Banquet Hall/img6.jpg"class="thumbnail" alt="img7">
    </div>
  </div>

  <!-- Left and right controls -->
  <a class="left carousel-control" href="#myCarousel" data-slide="prev">
    <span class="glyphicon glyphicon-chevron-left"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="right carousel-control" href="#myCarousel" data-slide="next">
    <span class="glyphicon glyphicon-chevron-right"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
<?php
include('connection.php');
$room_id=$_GET['hall_id'];
$sql=mysqli_query($con,"select * from halls where hall_id='$room_id' ");
$res=mysqli_fetch_assoc($sql);
?>

		<h2 class="Ac_Hall_Text"><?php echo $res['type']; ?></h2>
    <h3 class="Ac_Hall_Text"><?php echo $res['price']; ?></h3>
		<p class="text-justify">
      <?php echo $res['details']; ?>
</p>
    <div class="row">
      <h2>Facilities</h2>
      <img src="image/icon/wifi.png"class="img-responsive">
      <a href="Login.php" class="btn btn-danger">Book Now</a><br><br>
      </div>
	</div>
				<div class="col-sm-3">
					<div class="panel panel-primary">
					<div class="panel-heading">
						<h4 align="center">Space Type</h4>
					</div><br>
					<div class="panel-body-right text-center">
    <!--Fatch Mysql Database Select Query Room Details -->
						<?php
            include('connection.php');
            $sql1=mysqli_query($con,"select * from halls");
           while($result1= mysqli_fetch_assoc($sql1))
           {

            ?>
            <a href="hall_details.php?hall_id=<?php echo $result1['hall_id']; ?>"><?php echo $result1['type']; ?></a><hr>
            <?php } ?>
    <!--Fatch Mysql Database Select Query Room Details -->

					</div>
				</div>
				</div>
			</div>
		</div>
	</div>
  <?php
      include('footer.php')
  ?>
</body>
</html>
