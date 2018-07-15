from errbot import BotPlugin, cmdfilter, webhook, botcmd
from bottle import response
import dialogflow

class DFFilter(BotPlugin):
    """Pre filter commands via Dialogflow"""

    @cmdfilter(catch_unprocessed=True)
    def df_filter(self, msg, cmd, args, dry_run, emptycmd=False):
        if not emptycmd:
            return msg, cmd, args

    #     matched_prefix = False
    #     prefixes = self.bot_config.BOT_ALT_PREFIXES + (self._bot.bot_config.BOT_PREFIX,)

    #     for prefix in prefixes:
    #         if msg.body.startswith(prefix):
    #             matched_prefix = True

    #     if not matched_prefix:
    #         return msg, cmd, args

    #     res = self._detect_intent(msg.body, "newagent-e96a5")
    #     if res:
    #         return msg, res['intent'], [res['parameter']['service_name']]
    #     else:
    #         return msg, cmd, args


    # def _detect_intent(self, text, project_id, session_id="debot_test", lang="en"):
    #     """Returns the result of detect intent with texts as inputs.

    #     Using the same `session_id` between requests allows continuation
    #     of the conversaion."""
    #     session_client = dialogflow.SessionsClient()

    #     session = session_client.session_path(project_id, session_id)
    #     self.log.info('Session path: {}\n'.format(session))

    #     text_input = dialogflow.types.TextInput(text=text, language_code=lang)
    #     query_input = dialogflow.types.QueryInput(text=text_input)

    #     res = session_client.detect_intent(session=session, query_input=query_input)

    #     if res.query_result.all_required_params_present:
    #         return {
    #             "intent": res.query_result.intent.display_name,
    #             "parameter": res.query_result.parameters
    #         }
    #     else:
    #         self.log.error("Cannot determine the intent for '{}'".format(text))
    #         return
