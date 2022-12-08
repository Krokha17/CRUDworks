using kuznetsova.Domain;
using kuznetsova.Repository;
using Microsoft.AspNetCore.Mvc;

namespace kuznetsova.Controllers
{
    [ApiController]
    [Route("/news")]
    public class NewsController : ControllerBase
    {
        [HttpPut]
        public News Create(News news)
        {
            Storage.NewsStorage.Create(news);
            return news;
        }

        [HttpGet]
        public News Read(int newsId)
        {
            return Storage.NewsStorage.Read(newsId);
        }

        [HttpPatch]
        public News Update(int newsId, News newNews)
        {
            return Storage.NewsStorage.Update(newsId, newNews);
        }

        [HttpDelete]
        public bool Delete(int newsId)
        {
            return Storage.NewsStorage.Delete(newsId);
        }
    }
}