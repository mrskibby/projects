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
$drivername =  mysqli_real_escape_string($conn, $_POST['drivername']);
$type =  mysqli_real_escape_string($conn, $_POST['type']);
$ID =  mysqli_real_escape_string($conn, $_POST['ID']);


$sql="INSERT INTO `driver` (`drivername`, `Type`, `ID`)
VALUES('$drivername','$type','$ID')";

if(mysqli_query($conn, $sql)){
     header("Location:Account2.php");
} else{
    echo "ERROR: Could not able to execute $sql. " . mysqli_error($conn);
}


}



?>