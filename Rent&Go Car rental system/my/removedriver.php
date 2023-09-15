<?php
$servername = "localhost";
$userName = "root";
$password = "";
$dbname = "myrent_db";

// Create connection
$conn = new mysqli($servername, $userName, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}


//$re= mysqli_query($conn, "SELECT * FROM driver "); 

//$res = mysqli_fetch_array($re);




$result = mysqli_query($conn, "SELECT drivername FROM driver");
$row = $result->fetch_assoc();
$res = mysqli_fetch_array($result);


$sql = "DELETE FROM driver WHERE drivername=drivername";



if(mysqli_query($conn, $sql)){
	//$result = $conn->query($query);
  if ($row["Admin"] == '0')
  {
    header("Location:Account.php");
  }
  else
  {
    header("Location:Account2.php");
  }

} else{
    echo "ERROR: Could not able to execute $sql. " . mysqli_error($conn);
}






?>