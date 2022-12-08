using kuznetsova.Domain;
using kuznetsova.Repository;
using Microsoft.AspNetCore.Mvc;

namespace kuznetsova.Controllers
{
    [ApiController]
    [Route("/coach")]
    public class CoachController : ControllerBase
    {
        [HttpPut]
        public Coach Create(Coach coach)
        {
            Storage.CoachStorage.Create(coach);
            return coach;
        }

        [HttpGet]
        public Coach Read(int coachId)
        {
            return Storage.CoachStorage.Read(coachId);
        }

        [HttpPatch]
        public Coach Update(int coachId, Coach newCoach)
        {
            return Storage.CoachStorage.Update(coachId, newCoach);
        }

        [HttpDelete]
        public bool Delete(int coachId)
        {
            return Storage.CoachStorage.Delete(coachId);
        }
    }
}