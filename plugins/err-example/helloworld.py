import re
from errbot import arg_botcmd, BotPlugin, botcmd, re_botcmd

# Name of your class is what will make up the name of your plugin
class HelloWorld(BotPlugin):
    """Example 'Hello, world!' plugin for Errbot"""
    # The class' docstring is used to automatically populate the built-in
    # command documentation when issuing the !help command.

    @botcmd
    def hello(self, msg, args):
        """Say hello to the world"""
        return "Hello world!"

    @botcmd(split_args_with=None)
    def hello_names(self, msg, args):
        """Say hello to given names"""
        for name in args:
            yield "Hello, {}!".format(name)

    @arg_botcmd('first_name', type=str)
    @arg_botcmd('--age', dest='age', type=int)
    @arg_botcmd('--gender', dest='gender', type=str, default='Male')
    # def hello_title(self, msg, **args):
    def hello_title(self, msg, first_name, age, gender):
        """Say hello to a person with age and gender"""
        title = 'Ms.'
        if gender.lower() in ['male', 'm', 'guy', 'boy', 'man']:
            title = 'Mr.'

        if first_name:
            yield "Hello, {} {}!".format(title, first_name)

        if age:
            yield "You are {} year-old.".format(age)

    @re_botcmd(pattern=r"^(please )?say (hi)|(hello)( to me)?$", prefixed=False, flags=re.IGNORECASE)
    def ask_for_hi(self, msg, match):
        """Ask bot to say hi to you"""
        yield "Well well well... Hi"