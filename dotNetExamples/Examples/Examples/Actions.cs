using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using Marg.BusinessConnect.Sdk.Client.DataContract.WebService;
using Marg.BusinessConnect.Sdk.Client.WebServiceClient;

namespace Examples
{
  public static class Actions
  {
    public static async Task CreateActionAsync(string actionId, string actionName, string postId, string impersonateUserId, string accessToken)
    {
      using (var webServiceClient = new WebServiceClient(Config.ApiUrl, accessToken))
      {
        webServiceClient.AddHttpHeader(HttpHeader.XImpersonateUser, impersonateUserId);
        var post = new Post_22 { Id = postId };
        var action = new Action_18
        {
          Id = actionId,
          Name = actionName,
          ActionType = ActionType.Positive.ToString(),
          AssistantEmail = Config.IntegrationKey,
          Description = actionName
        };
        var reminderV22 = new Reminder_22 { Resource = post, ActionList = new ListOfActions_18 { action } };

        reminderV22 = await webServiceClient.CreateReminderAsync(reminderV22);
      }
    }

    public static async Task DeleteActionsAsync(string reminderId, string impersonateUserId, string accessToken)
    {
      using (var webServiceClient = new WebServiceClient(Config.ApiUrl, accessToken))
      {
        webServiceClient.AddHttpHeader(HttpHeader.XImpersonateUser, impersonateUserId);
        await webServiceClient.DeleteReminderAsync<Reminder_22>(reminderId);
      }
    }
  }
}
