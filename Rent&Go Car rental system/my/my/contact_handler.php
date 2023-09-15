<html>
<title>Rent&Go</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="style.css">
<body style="background-color:#FAFAFA;">
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

session_start();

//3.1.1 Assigning posted values to variables.
$fullname = $_POST['fullname'];
$email = $_POST['email'];
$pnum = $_POST['pnum'];
$subject = $_POST['subject'];
$mess = $_POST['mess'];

$sql = "INSERT INTO message (Fullname, email, pnum, subject, mess) VALUES ('$fullname','$email','$pnum', '$subject','$mess')";


if(mysqli_query($conn, $sql)){
    echo "<script type='text/javascript'>alert('Message Sent Successfully')</script>";
    header("Location:Account.php");
} else{
    echo "<script type='text/javascript'>alert('Failed to send message. Check your internet connection and please try again!')</script>";
    header("Location:contact.html");
}

//3.1.2 Checking the values are existing in the database or not
header("Location:Account.php");
?>
</body>
</html>
