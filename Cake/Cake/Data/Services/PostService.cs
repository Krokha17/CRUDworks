using Cake.Data.Models;

namespace Cake.Data.Services
{
    public class PostService
    {
        public async Task<Post> AddPost(Post author)
        {
            DataSource.GetInstance()._posts.Add(author);
            return await Task.FromResult(author);
        }
        public async Task<Post> GetPost(int id)
        {
            var result = DataSource.GetInstance()._posts.Find(a => a.Id == id);
            return await Task.FromResult(result);
        }
        public async Task<Post?> UpdatePost(Post newPost)
        {
            var post = DataSource.GetInstance()._posts.FirstOrDefault(au => au.Id == newPost.Id);
            if (post != null)
            {
                post.Name = newPost.Name;
                post.Description = newPost.Description;
                return post;
            }
            return null;
        }

    }
}
