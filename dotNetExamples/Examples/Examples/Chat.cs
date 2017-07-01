using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using Marg.BusinessConnect.Sdk.Client.DataContract.WebService;
using Marg.BusinessConnect.Sdk.Client.WebServiceClient;
using Marg.BusinessConnect.Sdk.Client.WebServiceClient.Query.Stream;
using Marg.BusinessConnect.Sdk.Client.WebServiceClient.Query.User;

namespace Examples
{
  public static class Chat
  {
    public static async Task<string> GetChatIdForEmail(string email, string accessToken)
    {
      using (var webServiceClient = new WebServiceClient(Config.ApiUrl, accessToken))
      {
        var user = new UserBuilder(email).GetCreateData();

        var userStream = await webServiceClient.CreateStreamAsync(new UserStreamBuilder<StreamUser_22>(user));
        return userStream.Id;
      }
    }

    public static async Task PostToChatAsync(string content, string chatId, string accessToken)
    {
      await CreatePost.CreateReplyAsync(content, chatId, accessToken);
    }
  }
}
