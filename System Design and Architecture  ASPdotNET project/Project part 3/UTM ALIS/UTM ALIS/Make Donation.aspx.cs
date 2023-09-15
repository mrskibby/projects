using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using Business;
using DataSetTableAdapters;


public partial class Make_Donation : System.Web.UI.Page
{
    

    public Donation donation = new Donation(0);
    DonationTableAdapter adapter = new DonationTableAdapter();
    public Donation dnt;
    protected void Page_Load(object sender, EventArgs e)
    {

    }

    protected void TextBox1_TextChanged(object sender, EventArgs e)
    {

    }

    protected void Button1_Click(object sender, EventArgs e)
    {
        
        dnt = (Donation)donation.clone(float.Parse(Request["Text1"]));
        donation.AddDonation(dnt);
        ClientScript.RegisterStartupScript(Page.GetType(), "alert", "alert('Donation is successful.');window.location='Make Donation.aspx';", true);

    }

    protected void Button3_Click(object sender, EventArgs e)
    {

        dnt = (Donation)donation.clone(1);
        donation.AddDonation(dnt);
        ClientScript.RegisterStartupScript(Page.GetType(), "alert", "alert('Donation is successful.');window.location='Make Donation.aspx';", true);

    }

    protected void Button4_Click(object sender, EventArgs e)
    {

        dnt = (Donation)donation.clone(5);
        donation.AddDonation(dnt);
        ClientScript.RegisterStartupScript(Page.GetType(), "alert", "alert('Donation is successful.');window.location='Make Donation.aspx';", true);

    }

    protected void Button5_Click(object sender, EventArgs e)
    {

        dnt = (Donation)donation.clone(10);
        donation.AddDonation(dnt);
        ClientScript.RegisterStartupScript(Page.GetType(), "alert", "alert('Donation is successful.');window.location='Make Donation.aspx';", true);

    }

    protected void Button2_Click(object sender, EventArgs e)
    {
        Response.Redirect("MainPage.aspx");
    }
}