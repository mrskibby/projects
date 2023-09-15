<?php
$username = $_GET['Id'];
//including the database connection file
include('carrental.php');


if(isset($_POST["bookCar"])) {

	$location = mysqli_real_escape_string($mysqli, $_POST['location']);
	$pick_date = mysqli_real_escape_string($mysqli, $_POST['pick_date']);
	$return_date = mysqli_real_escape_string($mysqli, $_POST['return_date']);
	$car = mysqli_real_escape_string($mysqli, $_POST['car']);


	$pickdate = date('Y-m-d', strtotime($_POST['pick_date']));
	$returndate = date('Y-m-d', strtotime($_POST['pick_date']));

	$sql=mysqli_query($mysqli, "INSERT INTO booking(bookID,username,location,pickdate,returndate,car)
	VALUES(NULL,'$username','$_POST[location]','$pickdate','$returndate','$_POST[car]')");


	echo "<font color='green'>Car successfully booked.";


	header("Location:Account.php");

}

?>
