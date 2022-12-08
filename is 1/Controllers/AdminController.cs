using kuznetsova.Domain;
using kuznetsova.Repository;
using Microsoft.AspNetCore.Mvc;

namespace kuznetsova.Controllers
{
    [ApiController]
    [Route("/admin")]
    public class AdminController : ControllerBase
    {
        [HttpPut]
        public Admin Create(Admin admin)
        {
            Storage.AdminStorage.Create(admin);
            return admin;
        }

        [HttpGet]
        public Admin Read(int adminId)
        {
            return Storage.AdminStorage.Read(adminId);
        }

        [HttpPost]
        public Admin Update(int adminId, Admin newAdmin)
        {
            return Storage.AdminStorage.Update(adminId, newAdmin);
        }

        [HttpDelete]
        public bool Delete(int adminId)
        {
            return Storage.AdminStorage.Delete(adminId); ;
        }

        [HttpGet("RegAuthors")]
        public string RegAuthors(string str)
        {
            return str;// "Метод регистрации на выставке"
        }
    }
}