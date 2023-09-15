using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace adapter
{
    public partial class NonAlumni1 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void btn_back(object sender, EventArgs e)
        {
            Response.Redirect("WebForm1.aspx");
        }

    }
}