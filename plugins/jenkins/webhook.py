from errbot import BotPlugin, botcmd, webhook
from bottle import response

# Name of your class is what will make up the name of your plugin
class Webhook(BotPlugin):
    """Jenkins webhooks"""

    @webhook('jenkins/echo', raw=True)
    def echo(self, request):
        """Webhook of jenkins endpoint - echo"""
        response.set_header("Content-Type", "application/json")
        return {"request": request.json}