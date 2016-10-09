#cmdlist
import minqlx

class cmdlist(minqlx.Plugin):
    def __init__(self):
        self.add_command(("commandlist", "cmdlist"), self.cmd_cmdlist)

    def cmd_cmdlist(self, player, msg, channel):
        player.tell("^5!checkban                ^3- ^7Checks whether a player has been banned, and if so, why.\n"
                    "^5!checksilence            ^3- ^7Checks whether a player has been silenced, and if so, why. \n"
                    "^5!clan                    ^3- ^7Set your clan name i.e - !clan ABC\n"
                    "^5!info                    ^3- ^7Shows your statistics\n"
                    "^5!seen                    ^3- ^7Wanna stalk a mofo, use this. Usage: !seen <steam_id> \n"
                    "^5!elo                     ^3- ^7Check your qlstats.net elo \n"
                    "^5!myperm                  ^3- ^7Displays your admin permision levels \n"
                    "^5!sounds                  ^3- ^7Disables ingame bot/chat sounds\n"
                    "^5!allmaps                 ^3- ^7Shows the alternative maps available\n"
                    "^5!name                    ^3- ^7Set your name Usage: !name <name> \n"
                    "^5!queue/!q                ^3- ^7Shows waiting and AFK/away players\n"
                    "^5!afk                     ^3- ^7List yourself as AFK in the !queue\n"
                    "^5!here                    ^3- ^7Mark yourself as Playing/back\n"
                    "^5")
        return minqlx.RET_STOP_ALL

