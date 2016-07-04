# LondonChallenge/python

##  Dev console:

1. Go to http://clean-sprint-app.4thoffice.com/login and login with your Gmail or Exchange account
2. Go to https://clean-sprint-app.4thoffice.com/devconsole/login and login with the same account as in step 1
3. To create new application aka smart assistant click on Add new..
4. Enter your app name and URL where the app will be deployed (address of your amazone machine)
5. Add webhooks for 3 endpoints: 
  GET actionableResource/availability
  GET actionableResource
  POST action 


## API
http://clean-sprint-app.4thoffice.com/api

### Major endpoints

Name: "User_14"
Description: "User"
Href: "user/{userId}"
ContentTypes: 
- "application/vnd.4thoffice.user-4.0+xml"
- "application/vnd.4thoffice.user-4.0+json"
Methods: 
- 
  Type: "OPTIONS"
  Description: "Retrieve options available for resource 'User_14'."
  Parameters: []
- 
  Type: "GET"
  Description: "Get user resource."
  Parameters: []
- 
  Type: "POST"
  Description: "Register new user or create new contact."
  Parameters: []
- 
  Type: "DELETE"
  Description: "Delete existing contact."
  Parameters: []
- 
Name: "UserSettings_14"
Description: "User settings."
Href: "user/settings"
ContentTypes: 
- "application/vnd.4thoffice.user.settings-4.0+xml"
- "application/vnd.4thoffice.user.settings-4.0+json"
Methods: 
- 
  Type: "OPTIONS"
  Description: "Retrieve options available for resource 'UserSettings_14'."
  Parameters: []
- 
  Type: "GET"
  Description: "Get user settings resource."
  Parameters: []
- 
  Type: "PUT"
  Description: "Update user settings resource."
  Parameters: []

- 
Name: "StreamBase_17"
Description: "Stream."
Href: "stream/{streamId}"
ContentTypes: 
- "application/vnd.4thoffice.stream-5.3+xml"
- "application/vnd.4thoffice.stream-5.3+json"
Methods: 
- 
  Type: "OPTIONS"
  Description: "Retrieve options available for resource 'StreamBase_17'."
  Parameters: []
- 
  Type: "GET"
  Description: "Get stream resource."
  Parameters: []
- 
Name: "StreamUser_17"
Description: "User stream."
Href: "stream/{streamId}"
ContentTypes: 
- "application/vnd.4thoffice.stream.user-5.3+xml"
- "application/vnd.4thoffice.stream.user-5.3+json"
Methods: 
- 
  Type: "OPTIONS"
  Description: "Retrieve options available for resource 'StreamUser_17'."
  Parameters: []
- 
  Type: "GET"
  Description: "Get stream resource."
  Parameters: []
- 
  Type: "POST"
  Description: "Create stream resource."
  Parameters: []
- 
  Type: "PUT"
  Description: "Update stream resource."
  Parameters: []
- 
  Type: "DELETE"
  Description: "Delete stream resource."
  Parameters: []
- 
Name: "StreamGroup_17"
Description: "Group stream."
Href: "stream/{streamId}"
ContentTypes: 
- "application/vnd.4thoffice.stream.group-5.3+xml"
- "application/vnd.4thoffice.stream.group-5.3+json"
Methods: 
- 
  Type: "OPTIONS"
  Description: "Retrieve options available for resource 'StreamGroup_17'."
  Parameters: []
- 
  Type: "GET"
  Description: "Get stream resource."
  Parameters: []
- 
  Type: "POST"
  Description: "Create stream resource."
  Parameters: []
- 
  Type: "PUT"
  Description: "Update stream resource."
  Parameters: []
- 
  Type: "DELETE"
  Description: "Delete stream resource."
  Parameters: []

- 
Name: "AccessToken_14"
Description: "Access token info."
Href: "token"
ContentTypes: 
- "application/vnd.4thoffice.access.token-4.0+xml"
- "application/vnd.4thoffice.access.token-4.0+json"
Methods: 
- 
  Type: "OPTIONS"
  Description: "Retrieve options available for resource 'AccessToken_14'."
  Parameters: []
- 
  Type: "POST"
  Description: "Refresh access token."
  Parameters: 
    - 
      Type: "String"
      Name: "accessTokenScope"
      Description: "Specify access token scope."
      Required: true
      IsList: true

- 
Name: "Group_17"
Description: "Group"
Href: "group/{groupId}"
ContentTypes: 
- "application/vnd.4thoffice.group-5.3+xml"
- "application/vnd.4thoffice.group-5.3+json"
Methods: 
- 
  Type: "OPTIONS"
  Description: "Retrieve options available for resource 'Group_17'."
  Parameters: []
- 
  Type: "GET"
  Description: "Get user group."
  Parameters: []
- 
  Type: "POST"
  Description: "Create user group."
  Parameters: []
- 
  Type: "PUT"
  Description: "Update user group."
  Parameters: []
- 
  Type: "DELETE"
  Description: "Delete user group."
  Parameters: []

- 
Name: "Feed_20"
Description: "Feed resource."
Href: "feed"
ContentTypes: 
- "application/vnd.4thoffice.feed-5.15+xml"
- "application/vnd.4thoffice.feed-5.15+json"
Methods: 
- 
  Type: "OPTIONS"
  Description: "Retrieve options available for resource 'Feed_20'."
  Parameters: []
- 
  Type: "GET"
  Description: "Retrieve feed resource."
  Parameters: 
    - 
      Type: "String"
      Name: "feedscope"
      Description: "Specify feed scope. Available values are: 'Stream', 'Card', 'ChatStream'."
      Required: true
      IsList: false
    - 
      Type: "String"
      Name: "feedidentity"
      Description: "Specify feed identity."
      Required: true
      IsList: false
    - 
      Type: "String"
      Name: "htmlFormat"
      Description: "Mime format for html body of post resource."
      Required: false
      IsList: false
    - 
      Type: "Int32"
      Name: "unreadOnly"
      Description: "Load unread discussion cards only."
      Required: false
      IsList: false
    - 
      Type: "Int32"
      Name: "loadUnread"
      Description: "Count of unread items that should get loaded per each feed item."
      Required: false
      IsList: false
    - 
      Type: "Int32"
      Name: "size"
      Description: "Specify size of requested page."
      Required: true
      IsList: false
    - 
      Type: "Int32"
      Name: "offset"
      Description: "Specify offset of requested page."
      Required: true
      IsList: false

- 
Name: "Post_20"
Description: "Post."
Href: "post/{postId}"
ContentTypes: 
- "application/vnd.4thoffice.post-5.15+xml"
- "application/vnd.4thoffice.post-5.15+json"
Methods: 
- 
  Type: "OPTIONS"
  Description: "Retrieve options available for resource 'Post_20'."
  Parameters: []
- 
  Type: "GET"
  Description: "Retrieve post resource."
  Parameters: []
- 
  Type: "POST"
  Description: "Create new post."
  Parameters: 
    - 
      Type: "String"
      Name: "clientResourceId"
      Description: "Resource id generated by client-side. Required for double-post prevention on server-side."
      Required: false
      IsList: false
    - 
      Type: "DateTime"
      Name: "customDateTime"
      Description: "Specify custom create date time."
      Required: false
      IsList: false
    - 
      Type: "String"
      Name: "signatureId"
      Description: "Specify signature id"
      Required: false
      IsList: false
- 
  Type: "POST"
  Description: "Copy existing post."
  Parameters: 
    - 
      Type: "String"
      Name: "sourceResourceId"
      Description: "Specify id of source resource."
      Required: true
      IsList: false

- 
Name: "Document_14"
Description: "Document resorce."
Href: "document/{documentId}"
ContentTypes: 
- "application/vnd.4thoffice.document-v4.0+xml"
- "application/vnd.4thoffice.document-v4.0+json"
- "application/octet-stream"
- "application/pdf"
Methods: 
- 
  Type: "OPTIONS"
  Description: "Retrieve options available for resource 'Document_14'."
  Parameters: []
- 
  Type: "GET"
  Description: "Retrieve document."
  Parameters: []
- 
  Type: "POST"
  Description: "Create document."
  Parameters: []
  HttpHeaderList: 
    - 
      Name: "X-Upload-File-Name"
      Description: "Name of uploaded file."
      Required: false
- 
  Type: "PUT"
  Description: "Update document."
  Parameters: []
- 
  Type: "DELETE"
  Description: "Delete document."
  Parameters: []
- 
Name: "Document_18"
Description: "Document resorce."
Href: "document/{documentId}"
ContentTypes: 
- "application/vnd.4thoffice.document-v5.8+xml"
- "application/vnd.4thoffice.document-v5.8+json"
- "application/octet-stream"
- "application/pdf"
Methods: 
- 
  Type: "OPTIONS"
  Description: "Retrieve options available for resource 'Document_14'."
  Parameters: []
- 
  Type: "GET"
  Description: "Retrieve document."
  Parameters: []
- 
  Type: "POST"
  Description: "Create document."
  Parameters: []
  HttpHeaderList: 
    - 
      Name: "X-Upload-File-Name"
      Description: "Name of uploaded file."
      Required: false

- 
Name: "Menu_21"
Description: "Menu resource."
Href: "navigation"
ContentTypes: 
- "application/vnd.4thoffice.menu-v5.17+json"
Methods: 
- 
  Type: "OPTIONS"
  Description: "Retrieve options available for resource 'Menu_21'."
  Parameters: []
- 
  Type: "GET"
  Description: "Get menu."
  Parameters: 
    - 
      Type: "String"
      Name: "menuScope"
      Description: "Specify menu scope. Available values are: 'Important', 'Others'."
      Required: true
      IsList: false
    - 
      Type: "Int32"
      Name: "badgeUnreadVersion"
      Description: "Version string that defines which logic to use for setting of unread badge count value on menu items and unread separator on feed. Available values are: 'V18', 'V19'."
      Required: false
      IsList: false
    - 
      Type: "Int32"
      Name: "streamReadFilter"
      Description: "Search filter by stream read status. Available values are: 'All', 'Read', 'Unread'."
      Required: false
      IsList: false
    - 
      Type: "Boolean"
      Name: "groupStreamOnly"
      Description: "Return group streams only."
      Required: false
      IsList: false
    - 
      Type: "Int32"
      Name: "size"
      Description: "Specify size of requested page."
      Required: true
      IsList: false
    - 
      Type: "Int32"
      Name: "offset"
      Description: "Specify offset of requested page."
      Required: true
      IsList: false

- 
Name: "MenuItem_21"
Description: "Menu item resource."
Href: "navigation/{streamId}"
ContentTypes: 
- "application/vnd.4thoffice.menu.item-v5.17+json"
Methods: 
- 
  Type: "OPTIONS"
  Description: "Retrieve options available for resource 'MenuItem_20'."
  Parameters: []
- 
  Type: "GET"
  Description: "Get menu item."
  Parameters: 
    - 
      Type: "Int32"
      Name: "badgeUnreadVersion"
      Description: "Version string that defines which logic to use for setting of unread badge count value on menu items and unread separator on feed. Available values are: 'V18', 'V19'."
      Required: false
      IsList: false

- 
Name: "NotificationReminderListUpdated_20"
Description: "Notification about updated reminder list."
Href: "notification"
ContentTypes: 
- "application/vnd.4thoffice.notification.reminder.list.updated-v5.15+xml"
- "application/vnd.4thoffice.notification.reminder.list.updated-v5.15+json"
Methods: 
- 
  Type: "OPTIONS"
  Description: "Retrieve options available for resource 'NotificationReminderListUpdated_20'."
  Parameters: []
- 
  Type: "POST"
  Description: "Crete notification."
  Parameters: []

- 
Name: "NotificationActionListUpdated_18"
Description: "Notification about updated action list."
Href: "notification"
ContentTypes: 
- "application/vnd.4thoffice.notification.action.list.updated-v5.8+xml"
- "application/vnd.4thoffice.notification.action.list.updated-v5.8+json"
Methods: 
- 
  Type: "OPTIONS"
  Description: "Retrieve options available for resource 'NotificationActionListUpdated_18'."
  Parameters: []
- 
  Type: "POST"
  Description: "Crete notification."
  Parameters: []
- 
Name: "NotificationActionListUpdatedLast_18"
Description: "Last notification about updated action list."
Href: "notification"
ContentTypes: 
- "application/vnd.4thoffice.notification.action.list.updated.last-v5.8+xml"
- "application/vnd.4thoffice.notification.action.list.updated.last-v5.8+json"
Methods: 
- 
  Type: "OPTIONS"
  Description: "Retrieve options available for resource 'NotificationActionListUpdatedLast_18'."
  Parameters: []
- 
  Type: "GET"
  Description: "Get last notification about updated action list."
  Parameters: []

- 
Name: "ActionFinishWorkflow_18"
Description: "Action to finish given workflow."
Href: "action"
ContentTypes: 
- "application/vnd.4thoffice.action.finish.workflow-v5.8+xml"
- "application/vnd.4thoffice.action.finish.workflow-v5.8+json"
Methods: 
- 
  Type: "OPTIONS"
  Description: "Retrieve options available for resource 'ActionFinishWorkflow_18'."
  Parameters: []
- 
  Type: "POST"
  Description: "Action to finish fiven worflow."
  Parameters: []

- 
Name: "ActionNextStep_18"
Description: "Action to continue with next step of given workflow."
Href: "action"
ContentTypes: 
- "text/xml"
- "text/json"
Methods: 
- 
  Type: "OPTIONS"
  Description: "Retrieve options available for resource 'ActionNextStep_18'."
  Parameters: []
- 
  Type: "POST"
  Description: "Continue with next workflow step."
  Parameters: []
- 
Name: "ListOfActionableResourcesPage_21"
Description: "Page of actionable resources list."
Href: "action"
ContentTypes: 
- "application/vnd.4thoffice.actionable.resource.list.page-v5.17+xml"
- "application/vnd.4thoffice.actionable.resource.list.page-v5.17+json"
Methods: 
- 
  Type: "OPTIONS"
  Description: "Retrieve options available for resource 'ListOfActionableResourcesPage_21'."
  Parameters: []
- 
  Type: "GET"
  Description: "Retrieve list of actionable resources."
  Parameters: 
    - 
      Type: "String"
      Name: "timeframe"
      Description: "Timeframe for requested reminder list. Available values are: 'Pending', 'Today', 'Tomorrow', 'Later', 'Completed'."
      Required: true
      IsList: false
    - 
      Type: "Int32"
      Name: "size"
      Description: "Specify size of requested page."
      Required: true
      IsList: false
    - 
      Type: "Int32"
      Name: "offset"
      Description: "Specify offset of requested page."
      Required: true
      IsList: false
- 
Name: "ActionableResource_21"
Description: "Actionable resource."
Href: "action/{actionableResourceId}"
ContentTypes: 
- "application/vnd.4thoffice.actionable.resource-v5.17+xml"
- "application/vnd.4thoffice.actionable.resource-v5.17+json"
Methods: 
- 
  Type: "OPTIONS"
  Description: "Retrieve options available for resource 'ActionableResource_21'."
  Parameters: []
- 
  Type: "GET"
  Description: "Retrieve actionable resource."
  Parameters: 
    - 
      Type: "String"
      Name: "contextType"
      Description: "Specify type of context. Available values are: 'Discussion', 'NewPost', 'Post', 'Stream', 'ChatStream', 'GroupList', 'File', 'BoardList', 'ReminderList', 'StreamList', 'StreamListMuted', 'StreamListImportant', 'StreamListImportantUnread'."
      Required: false
      IsList: false
    - 
      Type: "String"
      Name: "contextId"
      Description: "Specify context id."
      Required: false
      IsList: false
- 
  Type: "POST"
  Description: "Create arbitrary action."
  Parameters: []
- 
Name: "ActionableResourceOverview_21"
Description: "Actionable resource overview."
Href: "action"
ContentTypes: 
- "application/vnd.4thoffice.actionable.resource.overview-v5.17+xml"
- "application/vnd.4thoffice.actionable.resource.overview-v5.17+json"
Methods: 
- 
  Type: "OPTIONS"
  Description: "Retrieve options available for resource 'ActionableResourceOverview_21'."
  Parameters: []
- 
  Type: "GET"
  Description: "Get actionable resource overview"
  Parameters: 
    - 
      Type: "String"
      Name: "contextType"
      Description: "Specify type of context. Available values are: 'Discussion', 'NewPost', 'Post', 'Stream', 'ChatStream', 'GroupList', 'File', 'BoardList', 'ReminderList', 'StreamList', 'StreamListMuted', 'StreamListImportant', 'StreamListImportantUnread'."
      Required: false
      IsList: false
    - 
      Type: "String"
      Name: "contextId"
      Description: "Specify context id."
      Required: false
      IsList: false

- 
Name: "ActionableResourceAvailability_20"
Description: "Actionable resource availability."
Href: "action"
ContentTypes: 
- "application/vnd.4thoffice.actionable.resource.availability-v5.15+xml"
- "application/vnd.4thoffice.actionable.resource.availability-v5.15+json"
Methods: 
- 
  Type: "OPTIONS"
  Description: "Retrieve options available for resource 'ActionableResource_20'."
  Parameters: []
- 
  Type: "GET"
  Description: "Retrieve actionable resource."
  Parameters: 
    - 
      Type: "String"
      Name: "contextType"
      Description: "Specify type of context. Available values are: 'Discussion', 'NewPost', 'Post', 'Stream', 'ChatStream', 'GroupList', 'File', 'BoardList', 'ReminderList', 'StreamList', 'StreamListMuted', 'StreamListImportant', 'StreamListImportantUnread'."
      Required: false
      IsList: false
    - 
      Type: "String"
      Name: "contextId"
      Description: "Specify context id."
      Required: false
      IsList: false

- 
Name: "Reminder_21"
Description: "Reminder resource."
Href: "reminder/{reminderId}"
ContentTypes: 
- "application/vnd.4thoffice.reminder.base-v5.17+xml"
- "application/vnd.4thoffice.reminder.base-v5.17+json"
Methods: 
- 
  Type: "OPTIONS"
  Description: "Retrieve options available for resource 'Reminder_21'."
  Parameters: []
- 
  Type: "GET"
  Description: "Get reminder"
  Parameters: []
- 
  Type: "POST"
  Description: "Create reminder"
  Parameters: []
- 
  Type: "DELETE"
  Description: "Delete reminder"
  Parameters: []
