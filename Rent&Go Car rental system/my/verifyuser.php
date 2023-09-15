<?php
$username = $_GET['id'];
$user= $_GET['user'];

//including the database connection file
$servername = "localhost";
$userName = "root";
$password = "";
$dbname = "myrent_db";

//Create connection
$conn = new mysqli($servername, $userName, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}




//getting id of the data from url


//deleting the row from table$sql = "INSERT INTO user (FirstName, LastName, Email, username, password, Admin) VALUES ('$firstname','$lastname','$email','$username','$password', '0')";
$sql = "UPDATE user SET verified='1' WHERE username='$username'";
$query = "SELECT * FROM `user` WHERE username='$user'";
$result = $conn->query($query);
$row = $result->fetch_assoc();

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
