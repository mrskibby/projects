<%@ Page Language="C#" AutoEventWireup="true" CodeFile="AllActivity.aspx.cs" Inherits="AllActivity" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
        </div>
        <asp:GridView ID="GridView1" runat="server" AutoGenerateColumns="False" BackColor="White" BorderColor="#DEDFDE" BorderStyle="None" BorderWidth="1px" CellPadding="4" DataKeyNames="ActivityID" DataSourceID="SqlDataSource1" ForeColor="Black" GridLines="Vertical">
            <AlternatingRowStyle BackColor="White" />
            <Columns>
                <asp:BoundField DataField="ActivityID" HeaderText="ActivityID" ReadOnly="True" SortExpression="ActivityID" />
                <asp:BoundField DataField="Activityname" HeaderText="Activityname" SortExpression="Activityname" />
                <asp:BoundField DataField="Activitydate" HeaderText="Activitydate" SortExpression="Activitydate" />
                <asp:BoundField DataField="Totalparticipant" HeaderText="Totalparticipant" SortExpression="Totalparticipant" />
            </Columns>
            <FooterStyle BackColor="#CCCC99" />
            <HeaderStyle BackColor="#6B696B" Font-Bold="True" ForeColor="White" />
            <PagerStyle BackColor="#F7F7DE" ForeColor="Black" HorizontalAlign="Right" />
            <RowStyle BackColor="#F7F7DE" />
            <SelectedRowStyle BackColor="#CE5D5A" Font-Bold="True" ForeColor="White" />
            <SortedAscendingCellStyle BackColor="#FBFBF2" />
            <SortedAscendingHeaderStyle BackColor="#848384" />
            <SortedDescendingCellStyle BackColor="#EAEAD3" />
            <SortedDescendingHeaderStyle BackColor="#575357" />
        </asp:GridView>
        <asp:SqlDataSource ID="SqlDataSource1" runat="server" ConnectionString="<%$ ConnectionStrings:ConnectionString %>" SelectCommand="SELECT [ActivityID], [Activityname], [Activitydate], [Totalparticipant] FROM [Activity]"></asp:SqlDataSource>
        Alumni ID<asp:TextBox ID="UserID" runat="server" Height="24px" style="margin-left: 82px" OnTextChanged="UserID_TextChanged" Width="188px"></asp:TextBox>
        <br />
        <br />
        Activity ID<asp:TextBox ID="TextBox1" runat="server" Height="24px" style="margin-left: 82px" OnTextChanged="TextBox1_TextChanged" Width="188px"></asp:TextBox>
        <br />
        <asp:PlaceHolder ID="PlaceHolder1" runat="server">  
            <asp:TextBox ID="TextBox3" runat="server" Height="28px" Text=null OnTextChanged="TextBox3_TextChanged" style="margin-left: 463px" Width="188px"></asp:TextBox>
        </asp:PlaceHolder>
        <br />
        No of Pax to join<asp:TextBox ID="TextBox2" runat="server" Height="35px" style="margin-left: 27px; margin-top: 0px" OnTextChanged="TextBox2_TextChanged"></asp:TextBox>
        <br />
        <p>
            <asp:Button ID="Button1" runat="server" OnClick="Button1_Click" style="margin-left: 193px" Text="Join" Width="69px" />
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <asp:Button ID="Button2" runat="server" OnClick="Button2_Click" Text="Main Page" />
            &nbsp;</p>
        
    </form>
</body>
</html>
