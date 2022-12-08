using kuznetsova.Domain;
using kuznetsova.Repository;
using Microsoft.AspNetCore.Mvc;

namespace kuznetsova.Controllers
{
    [ApiController]
    [Route("/feedback")]
    public class FeedbackController : ControllerBase
    {
        [HttpPut]
        public Feedback Create(Feedback feedback)
        {
            Storage.FeedbackStorage.Create(feedback);
            return feedback;
        }

        [HttpGet]
        public Feedback Read(int feedbackId)
        {
            return Storage.FeedbackStorage.Read(feedbackId);
        }

        [HttpPatch]
        public Feedback Update(int feedbackId, Feedback newFeedback)
        {
            return Storage.FeedbackStorage.Update(feedbackId, newFeedback);
        }

        [HttpDelete]
        public bool Delete(int feedbackId)
        {
            return Storage.FeedbackStorage.Delete(feedbackId);
        }
    }
}