using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Web;

namespace adapter.Models
{
    public class AlumniContext : DbContext
    {
        public DbSet<Alumni> alumnis { get; set; }

        internal Alumni alumni()
        {
            throw new NotImplementedException();
        }
    }
}