using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.Web.Routing;
using adapter.Models;

namespace adapter.Controller
{
    public class HomeController : IController
    {
        public void Execute(RequestContext requestContext)
        {
            throw new NotImplementedException();
        }

        // GET: Home/Index
        public ActionResult Index()
        {
            AlumniContext ac = new AlumniContext();
            Alumni singleal = ac.alumnis.Single(predicate: al => al.Id==1);
            return View(singleal);
        }

        private ActionResult View(Alumni singleal)
        {
            throw new NotImplementedException();
        }
    }
}