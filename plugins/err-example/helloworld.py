from errbot import BotPlugin, botcmd

# Name of your class is what will make up the name of your plugin
class HelloWorld(BotPlugin):
    """Example 'Hello, world!' plugin for Errbot"""
    # The class' docstring is used to automatically populate the built-in
    # command documentation when issuing the !help command.

    @botcmd
    def hello(self, msg, args):
        """Say hello to the world"""
        return "Hello, world! {}".format(msg)