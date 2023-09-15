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




if ( isset( $_POST['submit'] ) )

{
$carname =  mysqli_real_escape_string($conn, $_POST['carname']);
$type =  mysqli_real_escape_string($conn, $_POST['type']);
$rent =  mysqli_real_escape_string($conn, $_POST['rent']);
$ID =  mysqli_real_escape_string($conn, $_POST['ID']);


$sql="INSERT INTO `cars` (`carname`, `Type`, `Rent`, `ID`)
VALUES('$carname','$type','$rent','$ID')";

if(mysqli_query($conn, $sql)){
     header("Location:Account2.php");
} else{
    echo "ERROR: Could not able to execute $sql. " . mysqli_error($conn);
}


}



?>