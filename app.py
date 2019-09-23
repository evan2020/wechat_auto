# 导入模块
from wxpy import *

# 初始化机器人，扫码登陆
bot = Bot(cache_path=True)

# 获取简单的好友统计
# friends_total=bot.friends().stats_text()
# print(friends_total)

# 获取微信的好友
friends_num=bot.friends()
print("获取的微信好友", friends_num)
friend_total = 0
for friend in friends_num:
    friend_total=friend_total+1
print("当前的好友总数", friend_total)

# 获取微信群的总数
groups_num=bot.groups()
print("获取的微信群", groups_num)
group_total = 0
for group in groups_num:
    group_total=group_total+1
print("当前的微信群", group_total)

# 获取微信公众号的总数
mps_num=bot.mps()
print("获取的微信公众号", mps_num)
mp_total = 0
for group in mps_num:
    mp_total=mp_total+1
print("当前的微信公众号", mp_total)
