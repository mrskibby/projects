using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using DataSetTableAdapters;

/// <summary>
/// Summary description for User
/// </summary>

namespace Alumni
{
    public class User
    {

        private string userType;
        private int creditPoints;
        private int activityNum;
        private string addFree;

        public int CreditScoreApply(string userType,int activity)
        {
            AlumniTableAdapter adapter = new AlumniTableAdapter();

            if (userType[0] == 'R')
            {
                
                if (activity == 1)
                {
                    int hold;
                    hold =15;
                    return hold;
                }

                else if (activity > 10)
                {
                    int hold;
                    hold = 9;
                    return hold;
                }
                else if (activity < 10 )
                {
                    int hold;
                    hold = 5;
                    return hold;

                }
            }


            else if (userType[0] == 'V')
            {
                
                if (activity == 1)
                {
                    int hold;
                    hold = 30;
                    return hold;
                }

                else if (activity > 10)
                {
                    int hold;
                    hold = 20;
                    return hold;
                }
                else if (activity < 10 && activity > 1)
                {
                    int hold;
                    hold = 10;
                    return hold;
                }
            }
            return 10;
        }
        public User()
        {
            userType = "";
            creditPoints = 0;
            activityNum = 0;
            addFree = "";
    }

        public string ChooseString(int credit)
        {
            if (credit == 5)
            {
                return addFree = "Food";
            }
            else if (credit == 9)
            {
                return addFree = "Food&Drinks";
            }
            else if (credit == 10)
            {
                return addFree = "Food AND EXTRA 5 CREDITSCORE";
            }

            else if (credit == 15)
            {
                return addFree = "Drinks";
            }

            else if (credit == 20)
            {
                return addFree = "Food&Drinks AND EXTRA 10 CREDITSCORE";
            }

            else if (credit == 30)
            {
                return addFree = "Drinks AND EXTRA 15 CREDITSCORE";
            }
            return "";

        }
    }
}