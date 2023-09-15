<?php
if(isset($add))
{
	$sql=mysqli_query($con,"select * from halls where hall_no='$rno'");
	if(mysqli_num_rows($sql))
	{
	echo "this hall is already added";
	}
	else
	{
	$img=$_FILES['img']['name'];
	mysqli_query($con,"insert into halls values('','$rno','$type','$price','$details','$img')");
	move_uploaded_file($_FILES['img']['tmp_name'],"../image/rooms/".$_FILES['img']['name']);
	echo "Halls added successfully";
	}
}
?>

<form method="post" enctype="multipart/form-data">
<table class="table table-bordered">

	<tr>
		<th>Hall No</th>
		<td><input type="text" name="rno"  class="form-control"/>
		</td>
	</tr>

	<tr>
		<th>Hall Type</th>
		<td><input type="text" name="type"  class="form-control"/>
		</td>
	</tr>

	<tr>
		<th>Price</th>
		<td><input type="text" name="price"  class="form-control"/>
		</td>
	</tr>

	<tr>
		<th>Details</th>
		<td><textarea name="details"  class="form-control"></textarea>
		</td>
	</tr>

	<tr>
		<th>Images</th>
		<td><input type="file" name="img"  class="form-control"/>
		</td>
	</tr>

	<tr>
		<td colspan="2">
			<input type="submit" class="btn btn-primary" value="Add Hall Details" name="add"/>
		</td>
	</tr>
</table>
</form>
