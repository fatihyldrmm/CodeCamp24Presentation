using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System.Net.Http.Headers;
using System.Text.Json;

namespace case2_api.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class TestController : ControllerBase
    {
        private readonly HttpClient _httpClient;

        public TestController(HttpClient httpClient)
        {
            _httpClient = httpClient;
            _httpClient.BaseAddress = new Uri("https://gitlab-codecamp24.obss.io/api/v4/");
        }

        [HttpGet("projects")]
        public async Task<IActionResult> GetProjects()
        {
            _httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", "glpat-ExatJtF6_4uzB7Mi4Nzx");

            var response = await _httpClient.GetAsync("projects");
            response.EnsureSuccessStatusCode();

            var projects = await response.Content.ReadFromJsonAsync<object>();

            var directoryPath = Path.Combine(Directory.GetCurrentDirectory(), "json_files");
            Directory.CreateDirectory(directoryPath);

            var filePath = Path.Combine(directoryPath, "projects.json");
            var jsonString = JsonSerializer.Serialize(projects);
            await System.IO.File.WriteAllTextAsync(filePath, jsonString);

            return Ok(projects);
        }
    }
}
