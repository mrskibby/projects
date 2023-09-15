<?php
    //DB parameters
    $servername = "localhost";
    $userName = "root";
    $password = "";
    $dbname = "myrent_db";

    //Create connection
    $mysqli=mysqli_connect($servername, $userName,$password, $dbname);

    // Check connection
	if (!$mysqli) {
    die("Connection failed: " . mysqli_connect_error());
	}
	

//$conn->close();

?>
