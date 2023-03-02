LOC_REGEX = r"\(\d{1,3},\d{1,3},\d{1,2}\)"
ADMIN_OSAY_EXP = r"made the ((?:\w+ ?)+) at ((?:\w+ ?)+) " + LOC_REGEX + r" say \"(.*)\"$"
ADMIN_STAT_CHANGE = r"((re-)|(de))?adminn?ed "
ADMIN_BUILD_MODE = r"has (entered|left) build mode."
GAME_BOMB_HORRIBLE_HREF = r"<a href='\?priv_msg=\w+'>([\w ]+)<\/a>\/\((.+)\)"
GAME_I_LOVE_BOMBS = r"The (?:self-destruct device|syndicate bomb) that (.+) had primed detonated!"
