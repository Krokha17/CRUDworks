using kuznetsova.Domain;
using kuznetsova.Repository;
using Microsoft.AspNetCore.Mvc;

namespace kuznetsova.Controllers
{
    [ApiController]
    [Route("/subscription")]
    public class SubscriptionController : ControllerBase
    {
        [HttpPut]
        public Subscription Create(Subscription subscription)
        {
            Storage.SubscriptionStorage.Create(subscription);
            return subscription;
        }

        [HttpGet]
        public Subscription Read(int subscriptionNumber)
        {
            return Storage.SubscriptionStorage.Read(subscriptionNumber);
        }

        [HttpPatch]
        public Subscription Update(int subscriptionNumber, Subscription newSubscription)
        {
            return Storage.SubscriptionStorage.Update(subscriptionNumber, newSubscription);
        }

        [HttpDelete]
        public bool Delete(int subscriptionNumber)
        {
            return Storage.SubscriptionStorage.Delete(subscriptionNumber);
        }
    }
}