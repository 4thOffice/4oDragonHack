using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using Marg.BusinessConnect.Sdk.Client.WebServiceClient;
using Marg.BusinessConnect.Sdk.Client.WebServiceClient.Query.Notification;

namespace Examples
{
  public static class Sync
  {
    public static async Task<string> GetLatestSinceIdAsync(string accessToken)
    {
      using (var webServiceClient = new WebServiceClient(Config.ApiUrl, accessToken))
      {
        // Get initial last notification id.
        var listOfNotificationsPageV22 =
          await webServiceClient.GetNotificationListPageAsync(new NotificationQuery(null, 0, 0));

        var lastNotificationId = listOfNotificationsPageV22.LastNotificationId;
        return lastNotificationId;
      }
    }

    public static async Task GetNotificationSyncNormalAsync(string sinceId, string accessToken, int offset = 0, int size = 0)
    {
      using (var webServiceClient = new WebServiceClient(Config.ApiUrl, accessToken))
      {
        var listOfNotificationsPageV22 = 
          await webServiceClient.GetNotificationListPageAsync(new NotificationQuery(sinceId, offset, size));
      }
    }

    public static async Task GetNotificationSyncLongPollingAsync(string sinceId, string accessToken, int offset = 0, int size = 0)
    {
      using (var webServiceClient = new WebServiceClient(Config.ApiUrl, accessToken))
      {
        var listOfNotificationsPageV22 =
          await webServiceClient.GetNotificationListPageAsync(new NotificationQuery(sinceId, offset, size).SetLongPolling(true));
      }
    }
  }
}
