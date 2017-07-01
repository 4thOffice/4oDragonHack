using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using System.Threading.Tasks;
using Marg.BusinessConnect.Sdk.Client.DataContract.WebService;
using Marg.BusinessConnect.Sdk.Client.WebServiceClient;
using Marg.BusinessConnect.Sdk.Client.WebServiceClient.Query.Post;

namespace Examples
{
  public static class CreatePost
  {
    public static async Task CreateCardAsync(string toUserEmail, string title, string content, string accessToken, List<string> attatchmentIds = null)
    {
      using (var webServiceClient = new WebServiceClient(Config.ApiUrl, accessToken))
      {
        var postBuilder = new PostBuilder<Post_22>(title, content)
          .AddShareToItem(toUserEmail);

        if (attatchmentIds != null)
        {
          foreach (var attatchmentId in attatchmentIds)
            postBuilder.AddAttachment(attatchmentId);
        }

        var post = await webServiceClient.CreatePostAsync(postBuilder);
      }
    }

    public static async Task CreateCardHtmlAsync(string toUserEmail, string title, string html, string accessToken, List<string> attatchmentIds = null)
    {
      using (var webServiceClient = new WebServiceClient(Config.ApiUrl, accessToken))
      {
        var postBuilder = new HtmlPostBuilder(title, new MemoryStream(Encoding.UTF8.GetBytes(html)))
          .AddShareToItem(toUserEmail);

        if (attatchmentIds != null)
        {
          foreach (var attatchmentId in attatchmentIds)
            postBuilder.AddAttachment(attatchmentId);
        }

        var post = await webServiceClient.CreateHtmlPostAsync(postBuilder);
      }
    }

    public static async Task CreateReplyAsync(string content, string parentId, string accessToken, List<string> attatchmentIds = null)
    {
      using (var webServiceClient = new WebServiceClient(Config.ApiUrl, accessToken))
      {
        var postReplyBuilder = new PostReplyBuilder<Post_22>(parentId, content);

        if (attatchmentIds != null)
        {
          foreach (var attatchmentId in attatchmentIds)
            postReplyBuilder.AddAttachment(attatchmentId);
        }

        var post = await webServiceClient.CreatePostAsync(postReplyBuilder);
      }
    }

    public static async Task<string> CreateAttatchmentAsync(string filePath, string accessToken)
    {
      using (var webServiceClient = new WebServiceClient(Config.ApiUrl, accessToken))
      {
        var document =
              await webServiceClient.UploadDocumentFileAsync(
                new MemoryStream(File.ReadAllBytes(filePath)),
                Path.GetFileName(filePath));

        return document.Id;
      }
    }
  }
}
