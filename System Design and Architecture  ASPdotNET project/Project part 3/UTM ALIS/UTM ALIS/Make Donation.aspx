<%@ Page Language="C#" AutoEventWireup="true" CodeFile="Make Donation.aspx.cs" Inherits="Make_Donation" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    <style type="text/css">
        #Text1 {
            width: 61px;
        }
    </style>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <strong>Make Donation</strong><br />
            <br />
            <div class="form-group col-md-2">
                <asp:Label ID="Label5" runat="server" Text="Amount of donation (RM): "></asp:Label>
                <input id="Text1" type="text" class="form-control" placeholder="amount" runat="server"/>
            <asp:Button ID="Button1" runat="server" Text="Donate" OnClick="Button1_Click" />
            </div>
            <br />
            <br />
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<asp:Button ID="Button3" runat="server" Text="RM1" OnClick="Button3_Click" />
            &nbsp;&nbsp;&nbsp;
            <asp:Button ID="Button4" runat="server" Text="RM5" OnClick="Button4_Click" />
            &nbsp;&nbsp;&nbsp;
            <asp:Button ID="Button5" runat="server" Text="RM10" OnClick="Button5_Click" />
            &nbsp;&nbsp;&nbsp;
            <asp:Button ID="Button2" runat="server" OnClick="Button2_Click" Text="Main Page" />
            <br />
            <br />
            <asp:GridView ID="GridView1" runat="server" AutoGenerateColumns="False" BackColor="LightGoldenrodYellow" BorderColor="Tan" BorderWidth="1px" CellPadding="2" DataKeyNames="DonationID" DataSourceID="SqlDataSource1" ForeColor="Black" GridLines="None">
                <AlternatingRowStyle BackColor="PaleGoldenrod" />
                <Columns>
                    <asp:BoundField DataField="DonationID" HeaderText="DonationID" InsertVisible="False" ReadOnly="True" SortExpression="DonationID" />
                    <asp:BoundField DataField="Donateamount" HeaderText="Donateamount" SortExpression="Donateamount" />
                </Columns>
                <FooterStyle BackColor="Tan" />
                <HeaderStyle BackColor="Tan" Font-Bold="True" />
                <PagerStyle BackColor="PaleGoldenrod" ForeColor="DarkSlateBlue" HorizontalAlign="Center" />
                <SelectedRowStyle BackColor="DarkSlateBlue" ForeColor="GhostWhite" />
                <SortedAscendingCellStyle BackColor="#FAFAE7" />
                <SortedAscendingHeaderStyle BackColor="#DAC09E" />
                <SortedDescendingCellStyle BackColor="#E1DB9C" />
                <SortedDescendingHeaderStyle BackColor="#C2A47B" />
            </asp:GridView>
            <asp:SqlDataSource ID="SqlDataSource1" runat="server" ConnectionString="<%$ ConnectionStrings:ConnectionString %>" SelectCommand="SELECT [DonationID], [Donateamount] FROM [Donation]"></asp:SqlDataSource>
            <br />
        </div>
    </form>
</body>
</html>
