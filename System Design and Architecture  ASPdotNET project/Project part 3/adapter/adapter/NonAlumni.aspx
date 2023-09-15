<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="NonAlumni.aspx.cs" Inherits="adapter.NonAlumni1" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    <link href="StyleSheet1.css" rel="stylesheet" type="text/css" />
</head>
<body>
    <form id="form1" runat="server">
        <div class="container2">
            <center><h1>View Reserved Facilities By NonAlumni<br /></h1></center>
            <center><h3>From SRAD Database<br /></h3></center>
            <style>
                table {
                    border-collapse: collapse;
                    width: 100%;
                }

                th, td {
                    padding: 8px;
                    text-align: left;
                    border-bottom: 1px solid #ddd;
                }

                tr:hover {
                    background-color: #f5f5f5;
                }
            </style>
            <br />
            &nbsp;
            <asp:GridView ID="GridView1" runat="server" AutoGenerateColumns="False" DataKeyNames="Id" DataSourceID="SqlDataSource1" BorderColor="Black" BorderStyle="Double" BorderWidth="2px">
                <Columns>
                    <asp:BoundField DataField="Id" HeaderText="Id" ReadOnly="True" SortExpression="Id" />
                    <asp:BoundField DataField="Name" HeaderText="Name" SortExpression="Name" />
                    <asp:BoundField DataField="Email" HeaderText="Email" SortExpression="Email" />
                    <asp:BoundField DataField="Phone" HeaderText="Phone" SortExpression="Phone" />
                    <asp:BoundField DataField="Facility Reserved" HeaderText="Facility Reserved" SortExpression="Facility Reserved" />
                </Columns>
            </asp:GridView>
            <asp:SqlDataSource ID="SqlDataSource1" runat="server" ConnectionString="<%$ ConnectionStrings:ConnectionString2 %>" SelectCommand="SELECT * FROM [Table]"></asp:SqlDataSource>
            <br />
            <br />
            <asp:Button ID="btnA" runat="server" Text="Back to Main Page" OnClick="btn_back" />

        </div>
    </form>
</body>
</html>