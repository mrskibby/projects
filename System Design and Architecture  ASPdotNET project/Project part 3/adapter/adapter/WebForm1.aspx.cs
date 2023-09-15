using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace adapter
{
    public partial class WebForm1 : System.Web.UI.Page
    {
        protected void btn_alumni(object sender, EventArgs e)
        {
            // Add this in onclick function for list of alumni.
            
            Response.Redirect("Alumni.aspx");
           
        }

        protected void btn_NonAlumni(object sender, EventArgs e)
        {
            //Add this in onclick function for list of employers
            Response.Redirect("NonAlumni.aspx");
        }
    }
}