using System;

namespace kuznetsova.Domain
{

    public class Coach
    {

        public int CoachId { get; set; }

        public DateTime BirthDate { get; set; }

        public string FullName { get; set; }

        public string Schedule { get; set; }

        public int Experience { get; set; }

        public float Rating { get; set; }
    }
}