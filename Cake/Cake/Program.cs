using Cake.Data;
using Cake.Data.Services;

namespace Cake 
{
    public class Program
    {
        static void Main(string[] args)
        {
            var builder = WebApplication.CreateBuilder(args);
            builder.Services.AddControllers();
            builder.Services.AddEndpointsApiExplorer();
            builder.Services.AddSwaggerGen();
            //builder.Services.AddDbContext<EducationContext>();
            builder.Services.AddDatabaseDeveloperPageExceptionFilter();
            //builder.Services.AddTransient<AffiliationService>();
            //builder.Services.AddTransient<ArticleService>();
            builder.Services.AddTransient<PostService>();
            builder.Services.AddControllers().AddNewtonsoftJson(options =>
                options.SerializerSettings.ReferenceLoopHandling = Newtonsoft.Json.ReferenceLoopHandling.Ignore
            );
            var app = builder.Build();
            if (app.Environment.IsDevelopment())
            {
                app.UseSwagger();
                app.UseSwaggerUI();
            }
            app.UseAuthorization();
            app.MapControllers();
            app.UseCors(policy => policy
                .AllowAnyOrigin());
        }       
    }
}