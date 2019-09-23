# 导入模块
from wxpy import *

# 初始化机器人，扫码登陆
bot = Bot(cache_path=True)

# 获取简单的好友统计
# friends_total=bot.friends().stats_text()
# print(friends_total)

# 获取微信好友总数
wx_friends=bot.friends()
print("获取到的微信好友数据为", len(wx_friends))

# 获取微信群的总数
wx_groups=bot.groups()
print("获取到的微信群数据为", len(wx_groups),wx_groups)

# 获取微信公众号的总数
wx_mps=bot.mps()
print("获取到的微信公众号数据为", len(wx_mps),wx_mps)

