using Cake.Data.Models;

namespace Cake.Data
{
    public class DataSource
    {
        private static DataSource instance;
        private DataSource()
        {
        }
        public static DataSource GetInstance()
        {
            if (instance == null)
            {
                instance = new DataSource();
            }
            return instance;
        }
        public List<Post> _posts = new List<Post>();
    }
}
