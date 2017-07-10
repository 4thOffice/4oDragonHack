using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using Marg.BusinessConnect.Sdk.Client.DataContract.WebService;
using Marg.BusinessConnect.Sdk.Client.WebServiceClient;

namespace Examples
{
  public static class Login
  {
    public static string LoginUser()
    {
      var clientApplication = new ClientApplication_14
      {
        CodeName = Config.ClientName,
        Type = ClientApplicationType.Unknown,
        Version = "1.0"
      };

      var authentication = new Authentication_13
      {
        AuthenticationId = Config.IntegrationKey,
        AuthenticationToken = Config.IntegrationSecret,
        AuthenticationType = AuthenticationType.Integration
      };

      var logOnUserV14 = new LogOnUser_14 { Authentication = authentication, ClientApplication = clientApplication };
      using (var webServiceClient = new WebServiceClient(Config.ApiUrl, logOnUserV14))
      {
        return webServiceClient.AccessToken;
      }
    }
  }
}
