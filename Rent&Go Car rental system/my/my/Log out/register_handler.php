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
$username = $_POST['username'];
$password = $_POST['password'];
$firstname = $_POST['firstname'];
$lastname = $_POST['lastname'];
$pnum = $_POST['pnum'];
$email = $_POST['email'];
$link = $_POST['link'];



$sql = "INSERT INTO user (FirstName, LastName, Email, pnum, username, password, Admin, link) VALUES ('$firstname','$lastname','$email','$pnum', '$username','$password', '0', '$link')";


if(mysqli_query($conn, $sql)){
    echo "<script type='text/javascript'>alert('Account created successfully!')</script>";
} else{
    echo "<script type='text/javascript'>alert('Failed to create account. Please try again!')</script>";
}

//3.1.2 Checking the values are existing in the database or not
$query = "SELECT * FROM user WHERE username='$username' and password='$password'";

$result = mysqli_query($conn, $query) or die(mysqli_error($conn));
$count = mysqli_num_rows($result);
//3.1.2 If the posted values are equal to the database values, then session will be created for the user.
if ($count == 1){
$_SESSION['username'] = $username;
}else{
//3.1.3 If the login credentials doesn't match, he will be shown with an error message.
$fmsg = "Invalid Login Credentials.";
}
//3.1.4 if the user is logged in Greets the user with message
if (isset($_SESSION['username']))
{
	$query = "SELECT Firstname, Lastname, Email, Admin FROM `user` WHERE username='$username'";
	$result = $conn->query($query);
	if ($result->num_rows > 0)
	{
    // output data of each row
		while($row = $result->fetch_assoc())
		{
			if ($row["Admin"] == '0')
			{

			     header("Location:..\Account.php");
			}
			else
			{
				echo "<p class=\"welcomepage\">You are logged in as a Admin. <br><p>";
				header("Location:..\Account2.php");
			}
		}
	}
}
else
{
	echo "<p class=\"topparagraph\">Wrong Username / Password !</p>";
	$landingpage = "register.php";
//3.2 When the user visits the page first time, simple login form will be displayed
}
?>

<form align="middle" action="<?php echo $landingpage;?>" method="post">
	<input type="hidden" name="username" value="<?php echo $username;?>"><br>
	<input class="button" type="submit" value="Continue">
</form>

</body>
</html>
