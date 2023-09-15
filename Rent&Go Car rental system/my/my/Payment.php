<html>
<?php
$username = $_GET['id'];


?>
<head>
	<title> Payment </title>
</head>
<style>
@import url(https://fonts.googleapis.com/css?family=Roboto:400,900,700,500);

body {
  padding: 60px 0;
  background-color: rgba(178,209,229,0.7);
  margin: 0 auto;
  width: 600px;
}
.body-text {
  padding: 0 20px 30px 20px;
  font-family: "Roboto";
  font-size: 1em;
  color: #333;
  text-align: center;
  line-height: 1.2em;
}
.form-container {
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.card-wrapper {
  background-color: #6FB7E9;
  width: 100%;
  display: flex;

}
.personal-information {
  background-color: #3C8DC5;
  color: #fff;
  padding: 1px 0;
  text-align: center;
}
h1 {
  font-size: 1.3em;
  font-family: "Roboto"
}
input {
  margin: 1px 0;
  padding-left: 3%;
  font-size: 14px;
}
input[type="text"]{
  display: block;
  height: 50px;
  width: 97%;
  border: none;
}
input[type="email"]{
  display: block;
  height: 50px;
  width: 97%;
  border: none;
}
input[type="submit"]{
  display: block;
  height: 60px;
  width: 100%;
  border: none;
  background-color: #3C8DC5;
  color: #fff;
  margin-top: 2px;
  curson: pointer;
  font-size: 0.9em;
  text-transform: uppercase;
  font-weight: bold;
  cursor: pointer;
}
input[type="submit"]:hover{
  background-color: #6FB7E9;
  transition: 0.3s ease;
}
#column-left {
  width: 46.8%;
  float: left;
  margin-bottom: 2px;
}
#column-right {
  width: 46.8%;
  float: right;
}

@media only screen and (max-width: 480px){
  body {
    width: 100%;
    margin: 0 auto;
  }
  .form-container {
    margin: 0 2%;
  }
  input {
    font-size: 1em;
  }
  #input-button {
    width: 100%;
  }
  #input-field {
    width: 96.5%;
  }
  h1 {
    font-size: 1.2em;
  }
  input {
    margin: 2px 0;
  }
  input[type="submit"]{
    height: 50px;
  }
  #column-left {
    width: 96.5%;
    display: block;
    float: none;
  }
  #column-right {
    width: 96.5%;
    display: block;
    float: none;
  }
   #box {
            padding-top:40px;
            width: 400px;
            height: 100px;
            border: 50px solid green;
            margin: 50px;
            text-align:center;
            font-size:32px;
            font-weight:bold;
        }
}
</style>

<?php


//including the database connection file
include('carrental.php');


if(isset($_POST["bookCar"])) {

$location = mysqli_real_escape_string($mysqli, $_POST['location']);
$pick_date = mysqli_real_escape_string($mysqli, $_POST['pick_date']);
$return_date = mysqli_real_escape_string($mysqli, $_POST['return_date']);
$car = mysqli_real_escape_string($mysqli, $_POST['car_type']);


$pickdate = date('Y-m-d', strtotime($_POST['pick_date']));
$returndate = date('Y-m-d', strtotime($_POST['return_date']));
$pick = new DateTime($pickdate);
$return = new DateTime($returndate);
$diff = date_diff($pick, $return);
//$diff->format('%R%a days');


$sql=mysqli_query($mysqli, "INSERT INTO booking(bookID,username,location,pickdate,returndate,car)
VALUES(NULL,'$username','$_POST[location]','$pickdate','$returndate','$car')");

if ($car == 'Axia')
{
	$amount_per_day = 100;
	$price = 100 + $amount_per_day * $diff->days;
	//$price=$price + '100.00';
}
else if ($car== 'Alza')
{
	$amount_per_day = 160;
	$price = 160 +$amount_per_day * $diff->days;
}
else
{
	$amount_per_day = 120;
	$price = 120 +$amount_per_day * $diff->days;
}
//echo "<font color='green'>Car successfully booked.";




}

?>

<body background="assets/payment.jpg">

<div class="container">
<div class="row">
<!-- You can make it whatever width you want. I'm making it full width
on <= small devices and 4/12 page width on >= medium devices -->
<div class="col-xs-12 col-md-4">
<div class="container">
    <div class="total-logo">
        <div class="total">
            <span style="color:red; font-family:verdana;"><font size:4><b>Total: RM</b></font></span>
            <span class="total-n"><font size=6><?php echo $price ?></font> </span>
        </div>


<!-- CREDIT CARD FORM STARTS HERE -->
<div class="panel panel-default credit-card-box">
<div class="panel-heading display-table" >
<div class="row display-tr" >
<h3 class="panel-title display-td" >Payment Details</h3>
<div class="display-td" >
<img class="img-responsive pull-right" src="http://i76.imgup.net/accepted_c22e0.png">
</div>
</div>
</div>
<div class="panel-body">
<form role="form" id="payment-form">
<div class="row">
<div class="col-xs-12">
<div class="form-group">
<label for="cardNumber">CARD NUMBER</label>
<div class="input-group">
<input
type="tel"
class="form-control"
name="cardNumber"
placeholder="Valid Card Number"
autocomplete="cc-number"
required autofocus
/>
<span class="input-group-addon"><i class="fa fa-credit-card"></i></span>
</div>
</div>
</div>
</div>
<div class="row">
<div class="col-xs-7 col-md-7">
<div class="form-group">
<label for="cardExpiry"><span class="hidden-xs">EXPIRATION</span><span class="visible-xs-inline">EXP</span> DATE</label>
<input
type="tel"
class="form-control"
name="cardExpiry"
placeholder="MM / YY"
autocomplete="cc-exp"
required
/>
</div>
</div>
<div class="col-xs-5 col-md-5 pull-right">
<div class="form-group">
<label for="cardCVC">CV CODE</label>
<input
type="tel"
class="form-control"
name="cardCVC"
placeholder="CVC"
autocomplete="cc-csc"
required
/>
</div>
</div>
</div>
<div class="row">
<div class="col-xs-12">
<div class="form-group">
<label for="couponCode">COUPON CODE</label>
<input type="text" class="form-control" name="couponCode" />
</div>
</div>
</div>
<div class="row">
<div class="col-xs-12">

</div>
</div>
<div class="row" style="display:none;">
<div class="col-xs-12">
<p class="payment-errors"></p>
</div>
</div>
</form>
</div>
</div>
<!-- CREDIT CARD FORM ENDS HERE -->
<!-- ONLINE BANKING FORM BEGINS HERE -->
<div class="panel panel-default credit-card-box">
<div class="panel-heading display-table" >
<div class="row display-tr" >
<form>
<h3 class="panel-title display-td" >ONLINE BANKING </h3>
<div class="display-td" >
<img class="img-responsive pull-right" src="https://www.pbebank.com/images/FPX/fpx_business.aspx">

<!--<div>
<div>
<input type="radio" name="onlineBanking1" value="cimb" checked >
<img class="img-responsive pull-right" src="https://assets.bharian.com.my/images/articles/cimbank_1557489867.jpg" height="200" width="200"><br>
</div>
<div>
<input type="radio" name="onlineBanking2" value="maybank" >
<img class="img-responsive pull-right" src="https://assets.bharian.com.my/images/articles/Maybank.jpg.transformed_10.jpg" height="200" width="200"><br>
</div>
<div>
<input type="radio" name="onlineBanking3" value="publicbank" >
<img class="img-responsive pull-right" src="https://www.mstar.com.my/~/media/upload/2014/10/20/16/13/public%20bank.ashx?w=830&h=553&crop=1s" height="200" width="200">
</div>
</div>-->
<div>
<div>
<input type="radio" name="gender" value="male">
<img class="img-responsive pull-right" src="https://assets.bharian.com.my/images/articles/cimbank_1557489867.jpg" height="100" width="300"><br>
</div>
<div>
<input type="radio" name="gender" value="female">
<img class="img-responsive pull-right" src="https://assets.bharian.com.my/images/articles/Maybank.jpg.transformed_10.jpg" height="100" width="300"><br>
</div>
<div>
<input type="radio" name="gender" value="other">
<img class="img-responsive pull-right" src="https://www.mstar.com.my/~/media/upload/2014/10/20/16/13/public%20bank.ashx?w=830&h=553&crop=1s" height="100" width="300">
</div>
</div>
<script>
function CONFIRM() {

  var person = prompt("Please enter OTP:", " ");
  if (person == null || person == "") {
    prompt("Please enter OTP:", " ");
  }

  else{
    alert("Your payment has been made successfully" )
		window.location='Account.php' ;
  }

	
			}

</script>

<!--<button class="btn btn-success btn-lg btn-block" type="submit" href="payment1.html" >Make Payment</button>-->
<input  type ="button"  onClick="CONFIRM()" value="Make Payment " />


</div>
</div>

</div>



</div>

</form>
	<!-- If you're using Stripe for payments -->
<script type="text/javascript" src="https://js.stripe.com/v2/">
$('form').card({
    container: '.card-wrapper',
    width: 280,

    formSelectors: {
        nameInput: 'input[name="first-name"], input[name="last-name"]'
    }
});

</script>



</body>
  </html>
