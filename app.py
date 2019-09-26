# 导入模块
from wxpy import *

# 导入re模块
import re

# 初始化机器人，扫码登陆
bot = Bot(cache_path=True)

# 向文件传输助手发送消息
bot.file_helper.send('机器人已启动')

# 新人入群通知的匹配正则
rp_new_member_name = (
    re.compile(r'^"(.+)"通过'),
    re.compile(r'邀请"(.+)"加入'),
)

# 获取新群成员名称
def get_new_member_name(msg):
    # itchat 1.2.32 版本未格式化群中的 Note 消息
    from itchat.utils import msg_formatter
    msg_formatter(msg.raw, 'Text')

    for rp in rp_new_member_name:
        match = rp.search(msg.text)
        if match:
            return match.group(1)


# 新人入群的欢迎语
welcome_text = '''🎉 欢迎 @{0} 的加入！
😃 新人请见群公告
📖 {1}'''

# 设置新人进群自动@新人文本消息
# 打印所有*群聊*对象中的*文本*消息
@bot.register(Group, NOTE)
def welcome_name(msg):
    print("群的系统通知", msg)
    # 获取新成员的名称,方便群@新人
    name = get_new_member_name(msg)
    # 在群里回复文本
    msg.reply(welcome_text.format(name, "这是一新人进群的文本消息测试,第二次"))
# 仅仅堵塞线程
bot.join()

