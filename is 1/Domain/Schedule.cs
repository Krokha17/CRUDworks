using System;

namespace kuznetsova.Domain
{

    public class Schedule
    {
 
        public int ScheduleId { get; set; }

        public DateTime FreeDays { get; set; }

        public DateTime BusyDays { get; set; }

        public int CouchCode { get; set; }
    }
}