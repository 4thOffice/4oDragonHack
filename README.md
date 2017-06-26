# Lisbon challenge - python examples

## API URL (with all endpoints and content types)
http://clean-sprint-app.4thoffice.com/api

## Data contract
XSD format: https://github.com/4thOffice/4thOfficeClient/blob/master/src/DataContract/ApiDataContract.xsd

TS format: https://github.com/4thOffice/4thOfficeClient/blob/master/src/DataContract/ApiDataContract.ts

## Content types
4th Office API is build in a way, that you can request different content types on the same endpoint. For example if I want to get a user's settings, I can specify which types of settings I want. I would always do a `GET` request to `/user/settings` endpoint, but if I wanted general settings, I would set the `Accept` HTTP header as `application/vnd.4thoffice.user.settings-4.0+json` and if I wanted settings for notifications, I would set the `Accept` HTTP header as `application/vnd.4thoffice.user.settings.notification-5.15+json`. The same goes for `POST`, `PUT` and `DELETE` requests. There you might need to also set the `Content-Type` HTTP header. 

## SDKs

We offer you C# and Python SDKs. If you will be using any other programming language, raw HTTP requests are still possible (also included in examples).

Python SDK is available through pip install SnappEmailApiClient

C# SDK is available on demand (just ask Kaja or Simon if you want it).

##  Getting started:

1. In your desktop app go to Development->Change API base->Clean sprint. This will connect you to sandbox environment. Login with your Gmail or Exchange account
2. Go to https://clean-sprint-app.4thoffice.com/devconsole/login and login with the same account as in step 1 (we do not save your password and it is a sandbox environment so you can put in a random password)
3. To create new application (integration) click on Add new..
4. Enter your app name.
5. If you will use actions enter the URL of your server (can be done later)
6. Add webhooks for endpoint (if you are using actions, can also be done later): 
    - POST action 
7. Look at examples in this repository