# 导入模块
from wxpy import *

# 初始化机器人，扫码登陆
bot = Bot()

# 获取简单的好友统计
friends_total=bot.friends().stats_text()
print(friends_total)