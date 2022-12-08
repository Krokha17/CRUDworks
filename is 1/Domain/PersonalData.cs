using System;

namespace kuznetsova.Domain
{

    public class PersonalData
    {

        public int PersonalDataId { get; set; }

        public DateTime SubscriptionActivationDate { get; set; }

        public string Telephone { get; set; }

        public DateTime DateOfBirth { get; set; }

        public string Fio { get; set; }
    }
}