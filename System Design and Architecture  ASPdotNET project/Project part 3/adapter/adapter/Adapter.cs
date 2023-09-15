using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Web;

namespace adapter
{
    [Table("Table")]
    public class Alumni
    {
        
        public Alumni(string Name, string Add, int Id, int Phone,string Email, string Facility)
        {
            this.name = Name;
            this.id = Id;
            this.address = Add;
            this.email = Email;
            this.phoneNo = Phone;
            this.facility = Facility;
            
        }
        public string name { get; set; }
        public string address { get; set; }
        public int id { get; set; }
        public int Id { get; internal set; }
        public int phoneNo { get; set; }
        public string email { get; set; }
        public string facility { get; set; }
        override
        public string ToString()
        {
            return name +" "+ address+" "+ id+" "+ phoneNo+" "+facility+" "+ email;
        }
    }
    public class NonAlumni
    {

        public NonAlumni(string Name,  int Phone, string Facility, string Email)
        {
            this.name = Name;
          
            this.email = Email;
            this.phoneNo = Phone;
            this.facility = Facility;
        }
        public string name { get; set; }
        
        
        public int phoneNo { get; set; }
        public string facility { get; set; }
        public string email { get; set; }
        override
        public string ToString()
        {
            return name + " " + phoneNo  + " " +facility+" "+ email;
        }
    }
    interface ITarget
    {
        List<string> GetAlumni();
        
    }
    interface ETarget
    {
        List<string> GetNonAlumni();
    }
    public class NonAlumniAdaptee
    {
        public List<string> GetListOfNonAlumni()
        {
            List<string> Emp = new List<string>();
            NonAlumni emp1 = new NonAlumni("Haziq", 011456215, "DSI", "Haziq@gmail.com");
            NonAlumni emp2 = new NonAlumni("Jasim", 018456245, "Resak", "Jasim@yahoo.com");
            NonAlumni emp3 = new NonAlumni("Sakib", 018456245, "Dewan Perdana", "Sakib@yahoo.com");
            string connection1 = emp1.ToString();
            string connection2 = emp2.ToString();
            string connection3 = emp3.ToString();
            Emp.Add(" "+ connection1 + " ");
            Emp.Add("\n");
            Emp.Add(" "+ connection2 + " ");
            Emp.Add("\n");
            Emp.Add(" " + connection3 + " ");
            Emp.Add("\n");
            return Emp;


        }
    }


    public class AlumniAdaptee
    {
        public List<string> GetListOfAlumni()
        {
            List<string> products = new List<string>();
            Alumni u1 = new Alumni("Sakib","klg", 1, 01151166160,"Dewan Resak","Sakib@gmail.com");
            Alumni u2 = new Alumni("Liknesh", "KTDI", 2, 018452135, "Sports Hall 1", "Liknesh@gmail.com");
            Alumni u3 = new Alumni("Jasim", "KTDI", 2, 018452135, "Dewan KTHO", "Jasim@gmail.com");
            Alumni u4 = new Alumni("Sakib", "KLG", 2, 018452135, "DSI", "Sakib@gmail.com");

            string newL = Environment.NewLine;
            string a = u1.ToString();
            string b = u2.ToString();
            string c = u3.ToString();
            string d = u4.ToString();

            products.Add(" "+a+" ");
            products.Add("\n");
            
            products.Add(" "+ b + " ");
            products.Add("\n");
            
            products.Add(" " + c + " ");
            products.Add("\n");
            
            products.Add(" " + d + " ");
            products.Add("\n");
            return products;
        }
    }


    class UserAdapter : ITarget,ETarget
    {
        public List<string> GetAlumni()
        {
            AlumniAdaptee adaptee = new AlumniAdaptee();
            return adaptee.GetListOfAlumni();
        }
        public List<string> GetNonAlumni()
        {
            NonAlumniAdaptee adapt = new NonAlumniAdaptee();
            return adapt.GetListOfNonAlumni();
        }
    }


    
}