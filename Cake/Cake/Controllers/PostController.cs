using Microsoft.AspNetCore.Mvc;
using Cake.Data.Services;
using Cake.Data.Models;
using Microsoft.EntityFrameworkCore;

namespace Cake.Controllers
{
    public class PostController : Controller
    {
        [ApiController]
        [Route("api/[controller]")]
        public class PostsController : ControllerBase
        {
            private readonly PostService _context;

            public PostsController(PostService context)
            {
                _context = context;
            }

            [HttpGet("{id}")]
            public async Task<ActionResult<Post>> GetPost(int id)
            {
                var post = await _context.GetPost(id);

                if (post == null) return NotFound();
                return post;
            }
            
            [HttpPut("{id}")]
            public async Task<ActionResult<Post>> PutAuthor(int id, [FromBody] Post post)
            {
                var result = await _context.UpdatePost(id, post);
                if (result == null) return BadRequest();
                return Ok(result);
            }

            [HttpPost]
            public async Task<ActionResult<Post>> PostAuthor([FromBody] Post post)
            {
                var result = await _context.AddPost(post);
                if (result == null) BadRequest();
                return Ok(result);
            }
            
            [HttpDelete("{id}")]
            public async Task<IActionResult> DeletePost(int id)
            {
                var post = await _context.DeletePost(id);
                if (post)return Ok();
                return BadRequest();
            }
        }
    }
}
