<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm1.aspx.cs" Inherits="adapter.WebForm1" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    <link href="StyleSheet1.css" rel="stylesheet" type="text/css" />
</head>
<body>
    <form id="form1" runat="server">
            <div class="container2">
            <center><h1>View Reserved Facility<br /></h1></center>
            <br />
            <center>Select the type you want to view</center>
            &nbsp;
            <br />
            <br />
            <asp:Button ID="btnA" runat="server" Text="Alumni" Onclick="btn_alumni" />
            <br />
            <br />
            
            <asp:Button ID="btnE" runat="server" Text="Non Alumni" Onclick="btn_NonAlumni" />
        </div>
    </form>
</body>
</html>
