using kuznetsova.Domain;
using kuznetsova.Repository;
using Microsoft.AspNetCore.Mvc;

namespace kuznetsova.Controllers
{
    [ApiController]
    [Route("/schedule")]
    public class ScheduleController : ControllerBase
    {
        [HttpPut]
        public Schedule Create(Schedule schedule)
        {
            Storage.ScheduleStorage.Create(schedule);
            return schedule;
        }

        [HttpGet]
        public Schedule Read(int scheduleId)
        {
            return Storage.ScheduleStorage.Read(scheduleId);
        }

        [HttpPatch]
        public Schedule Update(int scheduleId, Schedule newSchedule)
        {
            return Storage.ScheduleStorage.Update(scheduleId, newSchedule);
        }

        [HttpDelete]
        public bool Delete(int scheduleId)
        {
            return Storage.ScheduleStorage.Delete(scheduleId);
        }
    }
}