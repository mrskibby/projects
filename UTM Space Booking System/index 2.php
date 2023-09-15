<?php
   session_start();

   if(isset($_SESSION['type']) && $_SESSION['type']==='user'){
        header('location: /utm/user/index.php');
   }
   else if(isset($_SESSION['type']) && $_SESSION['type']==='admin'){
        header('location: /utm/admin/index.php');
   }
   else if(isset($_SESSION['type']) && $_SESSION['type']==='hall_admin'){
        header('location: /utm/hall-admin/index.php');
   }
   else{
       //header('location: /utm/index.php');
   }
?>
<!DOCTYPE html>
<html lang="en">
<head>

  <title>UTM Space Booking</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

<!-- <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"> -->
  <link rel="stylesheet" href="css/bootstrap.min.css">
  <link rel="stylesheet" href="css/bootstrap1.min.css">
  <link rel="stylesheet" href="css/bootstrap-datepicker.min.css">
  <link type="text/css" href="css/bootstrap-timepicker.min.css" />
  <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet" type="text/css">
  <link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet" type="text/css">
  <link rel="stylesheet" href="assets/css/Footer-with-social-icons.css">
  <!-- <link rel="stylesheet" href="css/style.css"> -->
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="js/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <!-- <script src="js/bootstrap.min.js"></script> -->
  <script src="js/bootstrap-datepicker.min.js"></script>
  <script type="text/javascript" src="js/bootstrap-timepicker.min.js"></script>
  <script defer src="js/all.js" ></script>
  <style>
  body {
      font: 400 15px Lato, sans-serif;
      line-height: 1.8;
      color: #444;
  }
  h2 {
      font-size: 24px;
      text-transform: uppercase;
      color: #303030;
      font-weight: 600;
      margin-bottom: 30px;
  }
  h4 {
      font-size: 19px;
      line-height: 1.375em;
      color: #303030;
      font-weight: 400;
      margin-bottom: 30px;
  }
  .jumbotron {
      background-color: #171929;
      color: #fff;
      padding: 100px 25px;
      font-family: Montserrat, sans-serif;
  }
  .container-fluid {
      padding: 60px 50px;
  }
  .bg-grey {
      background-color: #f6f6f6;
  }
  .logo-small {
      color: #171929;
      font-size: 50px;
  }
  .logo {
      color: #171929;
      font-size: 200px;
  }
  .thumbnail {
      padding: 0 0 15px 0;
      border: none;
      border-radius: 0;
  }
  .thumbnail img {
      width: 100%;
      height: 100%;
      margin-bottom: 10px;
  }
  .carousel-control.right, .carousel-control.left {
      background-image: none;
      color: #171929;
  }
  .carousel-indicators li {
      border-color: #171929;
  }
  .carousel-indicators li.active {
      background-color: #171929;
  }
  .item h4 {
      font-size: 19px;
      line-height: 1.375em;
      font-weight: 400;
      font-style: italic;
      margin: 70px 0;
  }
  .item span {
      font-style: normal;
  }
  .panel {
      border: 1px solid #171929;
      border-radius:0 !important;
      transition: box-shadow 0.5s;
  }
  .panel:hover {
      box-shadow: 5px 0px 40px rgba(0,0,0, .2);
  }
  .panel-footer .btn:hover {
      border: 1px solid #171929;
      background-color: #fff !important;
      color: #171929;
  }
  .panel-heading {
      color: #fff !important;
      background-color: #171929 !important;
      padding: 25px;
      border-bottom: 1px solid transparent;
      border-top-left-radius: 0px;
      border-top-right-radius: 0px;
      border-bottom-left-radius: 0px;
      border-bottom-right-radius: 0px;
  }
  .panel-footer {
      background-color: white !important;
  }
  .panel-footer h3 {
      font-size: 32px;
  }
  .panel-footer h4 {
      color: #aaa;
      font-size: 14px;
  }
  .panel-footer .btn {
      margin: 15px 0;
      background-color: #171929;
      color: #fff;
  }
  .navbar {
      margin-bottom: 0;
      background-color: #171929;
      z-index: 9999;
      border: 0;
      font-size: 12px !important;
      line-height: 1.42857143 !important;
      letter-spacing: 4px;
      border-radius: 0;
      font-family: Montserrat, sans-serif;
  }
  .navbar li a, .navbar .navbar-brand {
      color: #fff !important;
  }
  .navbar-nav li a:hover, .navbar-nav li.active a {
      color: #171929 !important;
      background-color: #fff !important;
  }
  .navbar-default .navbar-toggle {
      border-color: transparent;
      color: #fff !important;
  }
  footer .glyphicon {
      font-size: 20px;
      margin-bottom: 20px;
      color: #171929;
  }
  .slideanim {visibility:hidden;}
  .slide {
      animation-name: slide;
      -webkit-animation-name: slide;
      animation-duration: 1s;
      -webkit-animation-duration: 1s;
      visibility: visible;
  }

  .notice {
      padding: 15px;
      background-color: #cfefd0;
      border-left: 6px solid #7f7f84;
      margin-bottom: 10px;
      -webkit-box-shadow: 0 5px 8px -6px rgba(0,0,0,.2);
         -moz-box-shadow: 0 5px 8px -6px rgba(0,0,0,.2);
              box-shadow: 0 5px 8px -6px rgba(0,0,0,.2);
  }
  .notice-sm {
      padding: 10px;
      font-size: 80%;
  }
  .notice-lg {
      padding: 35px;
      font-size: large;
      color: #444;
  }
  .notice-success {
      border-color: #80D651;
  }
  .notice-success>strong {
      color: #444;
  }
  .notice-info {
      border-color: #45ABCD;
  }
  .notice-info>strong {
      color: #444;
  }
  .notice-warning {
      border-color: #FEAF20;
  }
  .notice-warning>strong {
      color: #444;
  }
  .notice-danger {
      border-color: #d73814;
      background-color: #fed6d6;
      color: #444;
  }
  .notice-danger>strong {
      color: #444;
  }

  @keyframes slide {
    0% {
      opacity: 0;
      transform: translateY(70%);
    }
    100% {
      opacity: 1;
      transform: translateY(0%);
    }
  }
  @-webkit-keyframes slide {
    0% {
      opacity: 0;
      -webkit-transform: translateY(70%);
    }
    100% {
      opacity: 1;
      -webkit-transform: translateY(0%);
    }
  }
  @media screen and (max-width: 768px) {
    .col-sm-4 {
      text-align: center;
      margin: 25px 0;
    }
    .btn-lg {
        width: 100%;
        margin-bottom: 35px;
    }
  }
  @media screen and (max-width: 480px) {
    .logo {
        font-size: 150px;
    }
  }


  </style>
</head>
<body id="myPage" data-spy="scroll" data-target=".navbar" data-offset="60">

  <header className="app-header text-center" style="background: #fff;">
    <!-- <img src="img/banner.jpg" class="img-fluid" alt="Banner" style="width: 100%;height: 250px;" /> -->
    <nav class="navbar navbar-expand-lg">
      <a class="navbar-brand" href="index.php">UTM Space Booking</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item"><a class="nav-link" href="#about">ABOUT</a></li>
          <li class="nav-item"><a class="nav-link" href="#pricing">PRICING</a></li>
          <li class="nav-item"><a class="nav-link" href="#contact">CONTACT</a></li>
          <li class="nav-item"><a class="nav-link" href="gallery.html">GALLERY</a></li>
          <li class="nav-item"><a class="nav-link" href="login.php">LOG IN</a></li>
          <li class="nav-item"><a class="nav-link" href="registration.php">REGISTRATION</a></li>
      </div>
    </nav>
    <!-- <h3 className="app-title" style="margin-top: 1em; font-weight: bold;">Welcome to UTM Space Booking</h3> -->
  </header>

<div class="jumbotron">
  <h1 class="text-center">UTM Space Booking</h1>
  <div class="container pt-2">
    <div class="row">
      <div class="col-lg-12">
        <div class="text-center">
        <p>Check availbality here</p>
      </div>
      </div>
    </div>
    <div class="row ml-4 mt-2">
      <div class="col-lg-12">
  <form method="post" action="">
    <div class="form-group row">
    
      <label for="inputEmail3" class="col-sm-2 col-form-label">Select hall</label>
      <div class="col-sm-10">
        <select class="form-control" name="hall_name">
          <option>-- Select your option --</option>
          <?php
            include("connect.php");
            $query = "SELECT * FROM `halls`";
            $result = $conn->query($query);
            while($row = mysqli_fetch_assoc($result)){
              echo '<option value="'.$row['id'].'">'.$row['hall_name'].'</option>';
            }
          ?>
        </select>
      </div>
    </div>
    <div class="form-group row">
      <label for="sandbox-container1" class="col-sm-2 col-form-label">Date</label>
      <div class="col-sm-10"><div class="span5 col-md-5" id="sandbox-container"><input type="text" class="form-control" name="booking_date"></div>
      </div>
    </div>
    <fieldset class="form-group">
      <div class="row">
        <legend class="col-form-label col-sm-2 pt-0">Book For </legend>
        <div class="col-sm-10">
          <div class="form-check">
            <input class="form-check-input" type="radio" name="book_type" id="gridRadios1" value="full_day" checked>
            <label class="form-check-label" for="gridRadios1">
              Full Day (8:00 AM to 10:00 PM)
            </label>
          </div>
          <div class="form-check">
            <input class="form-check-input" type="radio" name="book_type" id="gridRadios2" value="half_day">
            <label class="form-check-label" for="gridRadios2">
              Half Day from
            </label>
            <!-- <fieldset class="form-group" >
              <div class="row" id="time_select">
                <legend class="col-form-label col-sm-2 pt-0"> From </legend> -->
                <div class="col-sm-10">
                  <div class="form-check">
                    <input class="form-check-input" type="radio" name="time1" id="gridRadios2_1" value="8_to_3">
                    <label class="form-check-label" for="gridRadios2_1">
                      8:00 AM to 2:30 PM
                    </label>
                  </div>
                  <div class="form-check">
                    <input class="form-check-input" type="radio" name="time1" id="gridRadios2_2" value="3_to_10">
                    <label class="form-check-label" for="gridRadios2_2">
                      3:30 PM to 10:00 PM
                    </label>
                  </div>

                </div>
              <!-- </div>
            </fieldset> -->
          </div>


        </div>
      </div>
    </fieldset>
    <div class="form-group row text-center">
      <div class="col-sm-10">
        <button type="submit" class="btn default">Cancel</button>

        <button type="submit" class="btn btn-primary" name="check_booking">Check</button>
      </div>
    </div>

  </form>
  <?php
    include('connect.php');

    if(isset($_POST['check_booking']))
    {
      $hall = $_POST['hall_name'];
      $booking_date = $_POST['booking_date'];
      // echo $booking_date;
      $book_type = $_POST['book_type'];
      // echo $book_type;
      $booking_time = '';
      if($book_type === 'full_day')
      {
        $booking_time = '8_to_10';
        // echo $booking_time;
      }
      else {
        $booking_time = $_POST['time1'];
        // echo $booking_time;
      }
      $query1 = "SELECT `hall_name` FROM `halls` WHERE id = '$hall'";
      $result1 = $conn->query($query1);
      $row1 = mysqli_fetch_assoc($result1);
      // echo 'hello';
      $query = "SELECT * FROM `booking_details` WHERE `hall_id` = '$hall' and `booked_on_date` like '$booking_date' and `booking_time` = '$booking_time'";
      $result = $conn->query($query);
      // echo $result['num_rows'];
      //var_dump($result);
      $d_res = $result;
      $row = mysqli_fetch_assoc($result);
      if($row != null){

          echo '<div class="notice notice-danger">
                    '.$row1['hall_name'].' is not Available for booking. Try another time.
                </div>';

      }
      else {
        if($book_type === 'full_day')
        {
          echo '<div class="notice notice-lg">
                    '.$row1['hall_name'].' is Available from <strong>8:00 AM to 10:00 PM</strong> on '.$booking_date.'.
                    <p>For booking you need to <a href="login.php"> LOG IN </a> now</p>
                </div>';
        }

        elseif($booking_time == '8_to_3' && $book_type === 'half_day'){
          // echo $booking_time;
          echo '<div class="notice notice-lg">
                    '.$row1['hall_name'].' is Available from <strong>8:00 AM to 2:30 PM</strong> on '.$booking_date.'.
                    <p>For booking you need to <a href="login.php"> LOG IN </a> now</p>
                </div>';
        }
        elseif($booking_time == '3_to_10'){
          echo '<div class="notice notice-lg">
                    '.$row1['hall_name'].' is Available from <strong>3:30 PM to 10:00 PM</strong> on '.$booking_date.'.
                    <p>For booking you need to <a href="login.php"> LOG IN </a> now</p>
                </div>';
        }
        // echo $booking_time;
      }


    }

  ?>

</div>
</div>
</div>
</div>


<!-- Container (About Section) -->
<div id="about" class="container-fluid">
  <div class="row">
    <div class="col-sm-8">
      <h2>About Us</h2><br>
      <h4>UTM spacebooking website is a self-service website where users can book hall easily on online.
</h4><br>
      <p>user can query time and halls are available to book anytime and anywhere</p>
      <br><button class="btn btn-default btn-lg">Get in Touch</button>
    </div>
    <div class="col-sm-4">
      <span class="glyphicon glyphicon-signal logo"></span>
    </div>
  </div>
</div>

<div class="container-fluid bg-grey">
  <div class="row">
    <div class="col-sm-4">
      <span class="glyphicon glyphicon-globe logo slideanim"></span>
    </div>
    <div class="col-sm-8">
      <h2>Our Values</h2><br>
      <h4><strong>MISSION:</strong> Our mission is to ease the way of hall booking for users in UTM . </h4><br>
      <p><strong>VISION:</strong> Our vission is aiming at digitalizing the booking system from manual system. </p>
    </div>
  </div>
</div>



<!-- Container (Pricing Section) -->
<div id="pricing" class="container-fluid">
  <div class="text-center">
    <h2>Pricing</h2>
    <h4>Choose a payment plan that works for you</h4>
  </div>
  <div class="row slideanim">
    <div class="col-sm-4 col-xs-12">
      <div class="panel panel-default text-center">
        <div class="panel-heading">
          <h1>Half Day</h1>
        </div>
        <div class="panel-body">
          <p><strong>8:00</strong> AM</p>
          <p> to</p>
          <p><strong>2:30</strong> PM</p>

        </div>
        <div class="panel-footer">
          <h3>250.00</h3>
          <h4>MRT</h4>
        </div>
      </div>
    </div>
    <div class="col-sm-4 col-xs-12">
      <div class="panel panel-default text-center">
        <div class="panel-heading">
          <h1>Full Day</h1>
        </div>
        <div class="panel-body">
          <p><strong>8:00</strong> AM</p>
          <p> to</p>
          <p><strong>10:00</strong> PM</p>

        </div>
        <div class="panel-footer">
          <h3>500.00</h3>
          <h4>MRT</h4>
        </div>
      </div>
    </div>
    <div class="col-sm-4 col-xs-12">
      <div class="panel panel-default text-center">
        <div class="panel-heading">
          <h1>Half Day</h1>
        </div>
        <div class="panel-body">
          <p><strong>3:30</strong> PM</p>
          <p> to</p>
          <p><strong>10:00</strong> PM</p>

        </div>
        <div class="panel-footer">
          <h3>250.00</h3>
          <h4>MRT</h4>
          <!-- <button class="btn btn-lg">Sign Up</button> -->
        </div>
      </div>
    </div>
  </div>
</div>

<!-- Container (Contact Section) -->
<div id="contact" class="container-fluid bg-grey">
  <h2 class="text-center">CONTACT</h2>
  <div class="row">
    <div class="col-sm-5">
      <p>Contact us and we'll get back to you within 24 hours.</p>
      <p><span class="glyphicon glyphicon-map-marker"></span> Universiti Teknologi Malaysia,Johor, 81310 </p>
      <p><span class="glyphicon glyphicon-phone"></span> +601121665883 , +601137332108 </p>
      <p><span class="glyphicon glyphicon-envelope"></span> shuvohoque@ymail.com </p>
    </div>
    <div class="col-sm-7 slideanim">
      <div class="row">
        <div class="col-sm-6 form-group">
          <input class="form-control" id="name" name="name" placeholder="Name" type="text" required>
        </div>
        <div class="col-sm-6 form-group">
          <input class="form-control" id="email" name="email" placeholder="Email" type="email" required>
        </div>
      </div>
      <textarea class="form-control" id="comments" name="comments" placeholder="Comment" rows="5"></textarea><br>
      <div class="row">
        <div class="col-sm-12 form-group">
          <button class="btn btn-default pull-right" type="submit">Send</button>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- Add Google Maps -->
<div id="googleMap" style="height:400px;width:100%;"></div>
<script>
function myMap() {
  //1.558600 , 103.640656
var myCenter = new google.maps.LatLng(1.558600, 103.640656);
var mapProp = {center:myCenter, zoom:12, scrollwheel:false, draggable:false, mapTypeId:google.maps.MapTypeId.ROADMAP};
var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);
var marker = new google.maps.Marker({position:myCenter});
marker.setMap(map);
}
</script>
<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyB2t6jCuYGGMwh0HxKH7uYwVKJokSElUAQ&callback=myMap"></script>

<!--Footer-->
    <footer id="myFooter">
        <div class="container">
            <div class="row">

                <div class="col-sm-4 myCols">
                    <h5>About us</h5>
                    <ul>
                        <li><a href="#">Company Information</a></li>
                        <li><a href="#">Contact us</a></li>
                        <li><a href="#">Reviews</a></li>
                    </ul>
                </div>
                <div class="col-sm-4 myCols">
                    <h5>Support</h5>
                    <ul>
                        <li><a href="#">FAQ</a></li>
                        <li><a href="#">Help desk</a></li>
                        <li><a href="#">Forums</a></li>
                    </ul>
                </div>
                <div class="col-sm-4 myCols">
                    <h5>Legal</h5>
                    <ul>
                        <li><a href="#">Terms of Service</a></li>
                        <li><a href="#">Terms of Use</a></li>
                        <li><a href="#">Privacy Policy</a></li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="social-networks">
            <a href="#" class="twitter"><i class="fab fa-twitter"></i></a>
            <a href="#" class="facebook"><i class="fab fa-facebook-f"></i></a>
            <a href="#" class="google"><i class="fab fa-google-plus"></i></a>
        </div>
        <div class="footer-copyright">
            <p>© 2016 Copyright UTM </p>
        </div>
    </footer>
    <!--/.Footer-->

<script>
$('#sandbox-container input').datepicker({
  });
$(document).ready(function(){
  // Add smooth scrolling to all links in navbar + footer link
  $(".navbar a, footer a[href='#myPage']").on('click', function(event) {
    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      event.preventDefault();

      // Store hash
      var hash = this.hash;

      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (900) specifies the number of milliseconds it takes to scroll to the specified area
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 900, function(){

        // Add hash (#) to URL when done scrolling (default click behavior)
        window.location.hash = hash;
      });
    } // End if
  });

  $(window).scroll(function() {
    $(".slideanim").each(function(){
      var pos = $(this).offset().top;

      var winTop = $(window).scrollTop();
        if (pos < winTop + 600) {
          $(this).addClass("slide");
        }
    });
  });
})


</script>
</body>
</html>
