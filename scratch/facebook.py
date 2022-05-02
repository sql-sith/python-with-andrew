import facebook, urllib3, requests

'''Demonstrate usage of Facebook graph API.

1. Create a Facebook developer account. See https://developers.facebook.com/docs/development/register.
2. Create a Facebook app. See https://developers.facebook.com/apps/.
    - type: business
    - display name: sql sith is all business
    - app contact email: chris@databaseguy.com
    - business account: no business manager account selected
3. Get your app id from the top of the "add products to your app" page
    - mine was 502422597913056
4. Setup Messenger for your app and link it to one or more pages. Copy the access keys.
    - People and Animals Against Butter Cow Vandals: EAAHI82B5yeABAKoiAt8CUHXHfQt8BtU0xNXw71JosTy2II6Ev3ZB8biVGmL8v0xTcVkHhkm8LytZAlt2BZAjTC9ZBiAGyHbtY6K8jfZAHFCwZAuRQGowZB4vHFT9ofjpEnIHsCktUvEc2ptOsLJMR1Rf6wfYNsEm6G6WbYNB6QpLcNo0vvdf3QJ
    - Light Day: EAAHI82B5yeABALVls4akj4b6zPtYCLAWAvYJYtyuPDsczGkF4WPqpbhgjaWCRo1EXR97qCeWQ2fTyxQnMVxROoFiOi1tfgkTpTQLTtnwMm9UiQvF3fKBny2bG6r5FUkPlJCvRYvZAGFAZAAv0R5MoEQBuwmvC4ZAsbRJGm8LeIX5lSm9xqj
 

'''
# api = GraphAPI(app_id="id", app_secret="secret", oauth_flow=True)