<?php session_start(); ?>
<?php 
	include ('PHP/carrental.php');

	$found= false;
	
	//admin
	$sql="SELECT * FROM register";
	$result=$conn->query($sql);
	//$result=mysqli_query($mysqli,$sql);
	while($row= $result->fetch_assoc()){
		if($_POST["u_username"]==$row['username'] && $_POST["u_password"]==$row['password'] ){
			$found= true;
		
			$_SESSION["Login"]= "register";
			$_SESSION["Username"]= $row['username'];
			$_SESSION["Password"]= $row['password'];
			
			header("Location: index3.php");
			exit();
		}
    }
    
    	//not found	
	if(!$found){
		
		$_SESSION["Login"]= "Error";
		header("Location: login.php"); /* Redirect homepage */
		exit();
	}
	
?>

