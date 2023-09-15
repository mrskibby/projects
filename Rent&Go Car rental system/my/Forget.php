<?php
include('dbconnect.php');
error_reporting(1);
extract($_REQUEST);
if(isset($submit))
{
  $sql=mysqli_query($mysqli,"select * from user where Email='$email' ");
    if(mysqli_num_rows($sql))
    {
     $res=mysqli_fetch_assoc($sql);
    $error= "<h3 style='color:white; text-align:center;'>Your Password is :".$res['password']."</h3>";
    }
    else
    {
    $error= "<h3 style='color:white;text-align:center;'>Invalid  details</h3>";
    }
}
?>




<!DOCTYPE html>
<html lang="en">
<head>
  <title>Reset Password</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
  <link href="css/style.css"rel="stylesheet"/>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<style>

#myVideo {
  position: fixed;
  right: 0;
  bottom: 0;
  min-width: 100%;
  min-height: 100%;
}

/* Add some content at the bottom of the video/page */
.content {
  position: fixed;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  color: #f1f1f1;
  width: 100%;
  padding: 20px;
}

/* Style the button used to pause/play the video */
#myBtn {
  width: 200px;
  font-size: 18px;
  padding: 10px;
  border: none;
  background: #000;
  color: #fff;
  cursor: pointer;
}

#myBtn:hover {
  background: #ddd;
  color: black;
}

</style>


</head>
<body style="margin-top:50px;">

<video autoplay muted loop id="myVideo">
  <source src="assets/img/carvideo.mp4" type="video/mp4">
</video>



<div class="container-fluid"id="primary"> <!-- Primary Id-->
  <div class="container">
    <div class="row">
      <div class="col-sm-3"></div>
        <div class="col-sm-6">
          <h1 style="margin-top:50px;padding-top:50px; color:white; text-align:center;">Forgot Account?</h1><hr>
          <?php echo  @$error; ?>
          <p class="text-center" style="color:white; font-weight:bold;">Please Enter your Email Address to Find Your Account Password.</p><br><br>
          <form method="post">
        <div class="form-group">
          <input type="Email" name="email" class="form-control" id="#"placeholder="Email Address"required>
        </div><hr>
          <input type="submit" value="submit" name="submit" class="btn btn-primary btn-group-justified"required>
        </form><br><br><br><br>
        </div>
    </div>
  </div>
</div>