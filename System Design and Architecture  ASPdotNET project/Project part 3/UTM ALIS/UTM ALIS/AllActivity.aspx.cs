using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using Alumni;

using DataSetTableAdapters;

public partial class AllActivity : System.Web.UI.Page
{
    ActivityTableAdapter adapter = new ActivityTableAdapter();
    AlumniTableAdapter alumni = new AlumniTableAdapter();
    public User user= new Alumni.User();
    int credit, updated;
    int activityNum;
    string message, id;
    protected void Page_Load(object sender, EventArgs e)
    {

    }

    protected void Page_PreRender(object sender, EventArgs e)
    {
        if (TextBox3.Text == "null")
        {
            PlaceHolder1.Visible = false;
        }
        else
        {
            PlaceHolder1.Visible = true;
        }

    }

    protected void SqlDataSource2_Selecting(object sender, SqlDataSourceSelectingEventArgs e)
    {

    }

    protected void Button1_Click(object sender, EventArgs e)
    {
        ActivityTableAdapter adapter = new ActivityTableAdapter();
        AlumniTableAdapter alumni = new AlumniTableAdapter();
        


        if (Convert.ToInt32(adapter.CheckActivity(int.Parse(TextBox1.Text))) > 0)
        {
            id = UserID.Text;
            adapter.UpdateTotal(int.Parse(TextBox2.Text), int.Parse(TextBox1.Text));
            alumni.UpdateActivity(1, id);
            activityNum = (int)alumni.ReturnActivity(id);
            credit=user.CreditScoreApply(id,activityNum);
            alumni.UpdateCredit(credit, id);
            message = user.ChooseString(credit);
            TextBox3.Text = "Participation has been added.";
            ClientScript.RegisterStartupScript(Page.GetType(), "alert", "alert('Participation has been added. \\nYou get " + message+"');window.location='MainPage.aspx';", true);
        }
        else
        {
            TextBox3.Text="Activity Not Exist.";
        }
        
        



    }

    protected void TextBox1_TextChanged(object sender, EventArgs e)
    {

    }

    protected void TextBox2_TextChanged(object sender, EventArgs e)
    {

    }

    protected void TextBox3_TextChanged(object sender, EventArgs e)
    {

    }

    protected void Button2_Click(object sender, EventArgs e)
    {
       Response.Redirect("MainPage.aspx");
    }

    protected void UserID_TextChanged(object sender, EventArgs e)
    {

    }
}