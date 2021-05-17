# Basic example of Notion OAuth with Flask

A trivial example of using Flask-Dance to perform Notion public API authentication.

Documentation by Notion available here - https://developers.notion.com/docs

Documentation for specific public integration is here - https://developers.notion.com/docs/authorization#authorizing-public-integrations

1. Create a public integration in Notion
2. Obtain client ID and client secret and popular `NOTION_OAUTH_CLIENT_ID` and `NOTION_OAUTH_CLIENT_ID` respectively as environment variables
3. Install dependencies in requirements.txt
4. Run `python3 app.py`
5. Use localhost.run (or similar) to expose local endpoint to the web, something like:

```
➜  notion-flask-oauth git:(main) ✗ ssh -R 80:localhost:5000 nokey@localhost.run

===============================================================================
Welcome to localhost.run!

Follow your favourite reverse tunnel at [https://twitter.com/localhost_run].

**You need a SSH key to access this service.**
If you get a permission denied follow Gitlab's most excellent howto:
https://docs.gitlab.com/ee/ssh/
*Only rsa and ed25519 keys are supported*

To set up and manage custom domains go to https://admin.localhost.run/

More details on custom domains (and how to enable subdomains of your custom
domain) at https://localhost.run/docs/custom-domains

To explore using localhost.run visit the documentation site:
https://localhost.run/docs/

===============================================================================


** your connection id is e1d40983-3c94-4b5f-94a8-3d8808c1becd, please mention it if you send me a message about an issue. **

e4e403016c7880.localhost.run tunneled with tls termination, https://e4e403016c7880.localhost.run
```

6. Enter `https://e4e403016c7880.localhost.run` in as the redirect URI in the Notion app
7. Visit `https://e4e403016c7880.localhost.run` in your browser and go through the OAuth loop
