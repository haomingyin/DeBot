from errbot import BotPlugin, webhook, botcmd
from bottle import response
from itertools import chain
import requests
import time

# Name of your class is what will make up the name of your plugin
CONFIG_TEMPLATE = {
    "HOST": "https://jenkins.haomingyin.com",
    "API_KEY": "xxx",
    "USERNAME": "xxx",
    "ORG": ""
    }

class Jenkins(BotPlugin):
    """Jenkins webhooks"""

    def get_configuration_template(self):
        return CONFIG_TEMPLATE

    def configure(self, configuration):
        if configuration is not None and configuration != {}:
            config = dict(chain(CONFIG_TEMPLATE.items(),
                                configuration.items()))
        else:
            config = CONFIG_TEMPLATE
        super(Jenkins, self).configure(config)

    @webhook('/jenkins/echo', raw=True)
    def echo(self, request):
        """Echo endpoint used for testing"""
        response.set_header("Content-Type", "application/json")
        if self.config:
            return {"request": request.json, "prefix": self.config["prefix"]}
        return {"request": request.json}

    @webhook('/jenkins/input', raw=True)
    def check_input(self, request):
        time.sleep(1)
        self.send(
            self.build_identifier("#general"),
            "You have a new pending input from jenkins: {}".format(str(request.json))
            )

    @botcmd(split_args_with=None)
    def build(self, msg, args):
        """!build {project} - Trigger a new build for the given Jenkins project"""
        print(args[0])
        if self._build_helper(args[0]):
            self.log.info("Triggered a new build for project '{}'".format(args[0]))
            self.send_card(
                title="Roger that!",
                body="A new build has been triggered for project '{}'".format(args[0]),
                in_reply_to=msg,
                color='green')
        else:
            self.send_card(
                title="Oops",
                body="Failed to trigger a new build for project '{}'".format(args[0]),
                in_reply_to=msg,
                color='red')

    def _build_helper(self, project):
        """Trigger a new job"""
        url = self._get_job_url(project) + '/build'
        res = requests.post(url, auth=self._get_auth())
        if res.status_code != 201:
            self.log.error("Failed to trigger a new build at {}, status code: {}".format(url, res.status_code))
        return res.status_code == 201

    def _get_auth(self) -> dict:
        """Get authorization header"""
        return (self.config["USERNAME"], self.config["API_KEY"])

    def _get_job_url(self, project, branch="master") -> str:
        """Get general Jenkins job URL"""
        host = self.config['HOST']
        org = self.config['ORG']
        if org is not "":
            url = "{}/job/{}/job/{}/job/{}".format(host, org, project, branch)
        else:
            url = "{}/job/{}".format(host, project)
        return url

    # @botcmd
    # def longcompute(self, mess, args):
    #     if self._bot.mode == "slack":
    #         self._bot.add_reaction(mess, "hourglass")
    #     else:
    #         yield "Finding the answer..."

    #     time.sleep(10)

    #     yield "The answer is: 42"
    #     if self._bot.mode == "slack":
    #         self._bot.remove_reaction(mess, "hourglass")