import minqlx
import logging
import os.path
import datetime
import os

from logging.handlers import RotatingFileHandler

class simplelog (minqlx.Plugin):
    def __init__(self):
        self.add_hook("player_connect", self.handle_player_connect, priority=minqlx.PRI_LOWEST)

        self.set_cvar_once("qlx_simplelog", "3")
        self.set_cvar_once("qlx_simplelogSize", str(3*10**6)) # 3 MB

        self.chatlog = logging.Logger(__name__)
        file_dir = os.path.join(minqlx.get_cvar("fs_homepath"), "chatlogs")
        if not os.path.isdir(file_dir):
            os.makedirs(file_dir)

        file_path = os.path.join(file_dir, "simplelog.log")
        maxlogs = minqlx.Plugin.get_cvar("qlx_simplelog", int)
        maxlogsize = minqlx.Plugin.get_cvar("qlx_simplelogSize", int)
        file_fmt = logging.Formatter("[%(asctime)s] %(message)s", "%Y-%m-%d %H:%M:%S")
        file_handler = RotatingFileHandler(file_path, encoding="utf-8", maxBytes=maxlogsize, backupCount=maxlogs)
        file_handler.setFormatter(file_fmt)
        self.chatlog.addHandler(file_handler)

    def handle_player_connect(self, player):
        self.chatlog.info("{} : {} : {}".format(player.clean_name, player.steam_id, player.ip))

