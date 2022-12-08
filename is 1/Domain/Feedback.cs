using System;

namespace kuznetsova.Domain
{

    public class Feedback
    {

        public int FeedbackId { get; set; }

        public DateTime DateRecall { get; set; }

        public int CoachsCode { get; set; }

        public int Estimation { get; set; }

        public string Comment { get; set; }
    }
}