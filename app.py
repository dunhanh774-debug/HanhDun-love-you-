import discord
from discord.ext import commands
import random
from discord.ext import tasks
import datetime
from datetime import time
from datetime import datetime
import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError
import json, os
import requests
import math
from sympy import symbols, Matrix, lcm
import re
import nacl
import asyncio
import string
import traceback
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple, cast
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import yt_dlp
import aiohttp
from bs4 import BeautifulSoup
from TikTokApi import TikTokApi
import qrcode
import io
from discord import app_commands
API_KEY= "api requests"

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
intents = discord.Intents.all()

DATA_FILE= "data.json"
def load_data():
    if not os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "w") as f:
                json.dump({}, f)
        except PermissionError:
            print(f"no write permission {DATA_FILE}")
            return {}
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (PermissionError, json.JSONDecodeError) as e:
        print(f"❌ Lỗi đọc file {DATA_FILE}: {e}")
        return {}
def save_data(data):
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except PermissionError:
        print(f"no write permission {DATA_FILE}")



bot = commands.Bot(
    command_prefix= ["eiu", "Eiu", "E", "e"],
    intents=intents,
    strip_after_prefix=True,
    help_command=None
)
emoji_1= "<:416043450337853441:1455198475183587349>"
emoji_2= "<:votay:1455180079373226056>"
emoji_3= "<a:hon:1456269575728533584>"
emoji_4= "<:co4la:1455185457548886108>"
emoji_5= "<a:hug:1456272950062878843>"
emoji_6= "<a:slap:1456641153213534229>"
emoji_7= "<:Hcoin:1457356246406402224>"
emoji_8= "<:wifi:1463532432459432018>"
emoji_10= "<a:thankyou:1456562416497328138>"
emoji_9= "<a:BunnyILoveYouStickerBunnyILoveYo:1463885284490870907>"
emoji_11= "<a:Newkitten:1456562014372626464>"
emoji_12= "<a:phapluat:1469316378493456447>"
emoji_13= "<:youtube:1469320914310004870>"


stoneicon= "<:stone:1464970469227626684>"
thanicon= "<:than:1464971302778572860>"
quangsaticon= "<:sat:1464972064372031498>"
quangdongicon= "<:quangdong:1464972527389380831>"
redstoneicon= "<:redstone:1464973996968640705>"
quangvang= "<:quangvang:1464974127554105625>"
lapidicon= "<:lapid:1464974399332679826>"
kimcuongicon= "<:kimcuong:1464974694338920687>"
ngoclucbaoicon= "<:ngoclucbao:1464974844595798069>"

cupkcicon= "<:cupkimcuong:1466772677925797909>"

avcute= "https://cdn.discordapp.com/avatars/1437791571641630733/e45c5dd9a9f61a6533200fedf91e38ba.png?size=4096"
cuoi= [
    "https://cdn.discordapp.com/attachments/1439931543710597201/1463529239826399334/Gif.gif?ex=69722951&is=6970d7d1&hm=8f4a290986bd96aab23372b73cfa85a04a9903ed11caa18b36cbe3d453079374",
    "https://cdn.discordapp.com/attachments/1439931543710597201/1463529239826399334/Gif.gif?ex=69722951&is=6970d7d1&hm=8f4a290986bd96aab23372b73cfa85a04a9903ed11caa18b36cbe3d453079374",
    "https://cdn.discordapp.com/attachments/1439931543710597201/1463529534971187365/Happy_I_Love_You_Sticker_by_jerseycouple_-_Find__Share_on_GIPHY.gif?ex=69722998&is=6970d818&hm=dc63e426fd84026a9681e5edbbbf4b8946e31996cfbd810ef55a40be5062f80a&"    
]
tat1= [
    "https://cdn.discordapp.com/attachments/1439931543710597201/1456638342576738335/download.gif?ex=695917ab&is=6957c62b&hm=f273e102981342f301e1dbc629d167c6ae40d6164b4fd8c5c345ecf71d979361",
    "https://cdn.discordapp.com/attachments/1439931543710597201/1456638463364305001/download_1.gif?ex=695917c8&is=6957c648&hm=72542f5c9fbcdc057da1d04909fb6a98121b246e57afbaad0fdd616103d76436",
    "https://cdn.discordapp.com/attachments/1439931543710597201/1456638566309429393/download_2.gif?ex=695917e1&is=6957c661&hm=dd38017c45b1f7eeeb97fcd196781850e51d95b1f76cd15b209b3c77c81ca0eb",
    "https://cdn.discordapp.com/attachments/1439931543710597201/1456638794047684779/Anime_Box.gif?ex=69591817&is=6957c697&hm=6df3b80b7ee31bfeb7ed32dfbea1636c54b843d56fe49b653d98dd7f473bbd79,"
]
hon= [
    "https://cdn.discordapp.com/attachments/1439931543710597201/1455189763953791160/Kiss_Kissing_GIF_-_Kiss_Kissing_Anime_Kiss_-_Discover__Share_GIFs.gif?ex=6953d293&is=69528113&hm=a24f14cb248ce0f43f6c9a082baf16661980edd6a7f57cd7b0c1022aaa2bd269",
    "https://cdn.discordapp.com/attachments/1439931543710597201/1455189852130902168/Akagami_no_Shirayuki-hime____Shirayuki_and_Zen____KYAAAAAAAAAAAAAA__Incoherent_fangirl_noises_.gif?ex=6953d2a8&is=69528128&hm=644fa93e7b81c3d43be6f16ad49e7a78bc4ced9168cdc4efcf105cf3bf48eb88",
    "https://cdn.discordapp.com/attachments/1439931543710597201/1455190073736958116/-_Find__Share_on_GIPHY.gif?ex=6953d2dd&is=6952815d&hm=2410fab0d362aa999dbe1c7130c308c27803d636dccf9d39b528924b9cfe7881",
    "https://cdn.discordapp.com/attachments/1439931543710597201/1456270523339378709/download_1.gif?ex=6957c11c&is=69566f9c&hm=d52a6a9939408e61a81a7a5a815306fd1da5370cfc55085422d2a37128a1bab6",
    "https://cdn.discordapp.com/attachments/1439931543710597201/1456270658282459229/download_2.gif?ex=6957c13d&is=69566fbd&hm=a00fe5e0a4d249e7b0bf2e058d016052c66f67c0a8992fb4f2601ea991f30747",
    "https://cdn.discordapp.com/attachments/1439931543710597201/1456270768060235955/download_3.gif?ex=6957c157&is=69566fd7&hm=d86a67edb19e2ca22e74ce251f875e58c2784f01424a5be1e4b05296cbc9b477"
]
oms= [
    "https://cdn.discordapp.com/attachments/1439931543710597201/1456271743130931210/download_4.gif?ex=6957c23f&is=695670bf&hm=6c6f4723e6ae7e8185e36a0f62f5a141c9df23fc1adc9ea65bb75a6112c7640d",
    "https://cdn.discordapp.com/attachments/1439931543710597201/1456271866216972433/Nanami__Tomoe_-_Kamisama_Hajimemashita.gif?ex=6957c25d&is=695670dd&hm=8d4286aa0a75d26ceb93c9ce04e9541b6305604d579d873e3ffa82af8f6d0ee3",
    "https://cdn.discordapp.com/attachments/1439931543710597201/1456272042600173772/download_5.gif?ex=6957c287&is=69567107&hm=8c735f0d6d67a7b17707f62c78dc5eed7cd2b6462fb9370426ae4227849def2a",
    "https://cdn.discordapp.com/attachments/1439931543710597201/1456272195167719575/download_6.gif?ex=6957c2ab&is=6956712b&hm=cb5b88c2786cae729b123661989c096fbb18d786a6fc1df4268219c6796eb0ed",
    "https://cdn.discordapp.com/attachments/1439931543710597201/1456272372536578089/download_7.gif?ex=6957c2d5&is=69567155&hm=3610056533ff8a8f48526e2891c628c58893cb4b8af0402b29a68a8a87e44ad4",
    "https://cdn.discordapp.com/attachments/1439931543710597201/1456272658177196202/download_8.gif?ex=6957c319&is=69567199&hm=9b1f0d7e1433f0f5bd74ea71a6f5cc1b7bd2784a41704ca432c2feaa4a793237"
]
rickroll= "https://cdn.discordapp.com/attachments/1439931543710597201/1455187780354441318/Rick_Roll_Rick_Ashley_GIF_-_Rick_Roll_Rick_Ashley_Never_Gonna_Give_You_Up_-_GIF.gif?ex=6953d0ba&is=69527f3a&hm=db76a94f8c7ad196bbb9807086767cb8e55500341b7ebb254159cb4851d49f22"

dabthicon= "<:stonebth:1465336488160923864>"
thoisaticon= "<:thoisat:1465702554276069487>"
dongbthicon= "<:dongbth:1465938536204210423>"
thoivangicon= "<:thoivang:1466054420914634804>"


khoangsan= [
    f"Đá Cuội {stoneicon} [#1]",
    f"Than {thanicon} [#2]",
    f"Quặng Sắt {quangsaticon} [#3]",
    f"Quặng Đồng {quangdongicon} [#4]",
    f"Redstone {redstoneicon} [#5]",
    f"Quặng Vàng {quangvang} [#6]",
    f"Lapis Lazuli {lapidicon} [#7]",
    f"Kim cương {kimcuongicon} [#8]",
    f"Ngọc lục bảo {ngoclucbaoicon} [#9]"
]

weights= [55, 15, 12, 8, 2, 4, 3, 0.8, 0.2]

@bot.event
async def on_ready():
    await bot.tree.sync()
    if not update_stock_price.is_running():
        update_stock_price.start()
    if not send_stock_chart.is_running():
        send_stock_chart.start()
    await bot.change_presence(
        status=discord.Status.idle,
        activity=discord.Game(name="eiuhelp")
    )
    print("logged in")
        

@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    if ctx.guild.me.top_role <= member.top_role:
        await ctx.send(f"Không thể kick **{member.name}** do thiếu quyền hoặc role của {ctx.guild.me} thấp")
        return
    if ctx.author.guild_permissions.kick_members:
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} đã bị **{ctx.author}** kick, lý do: {reason}')
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Tag thành viên đi baaaa")
    if isinstance(error, commands.MissingRole):
        await ctx.send("Bạn không có quyền kick thành viên")
@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    if ctx.guild.me.top_role <= member.top_role:
        await ctx.send(f"Không thể ban **{member.name}** do thiếu quyền hoặc role của {ctx.guild.me} thấp")
        return
    if ctx.author.guild_permissions.ban_members:
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} đã bị {ctx.author} ban, lý do: {reason}')
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Tag thành viên đi baaaa")
    if isinstance(error, commands.MissingRole):
        await ctx.send("Bạn không có quyền ban thành viên")
@bot.command()
async def role(ctx, member: discord.Member, *, role: discord.Role):
    if role is None:
        await ctx.send(f'role not defined')
        return
    if ctx.author.guild_permissions.manage_roles:
        await member.add_roles(role)
        await ctx.send(f'added role to {member.mention}')
        return
@role.error
async def role_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Tag thành viên đi baaaa")
    if isinstance(error, commands.MissingRole):
        await ctx.send("Bạn không có quyền role thành viên")
class HelpSelect(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="Kinh tế",
                description="Hệ thống Hcoin, tiền ảo,...",
                emoji=f"{emoji_7}",
                value="minigame"
            ),
            discord.SelectOption(
                label=f"Pháp luật",
                description="Kick, ban, role",
                emoji=f"{emoji_12}",
                value="admin"
            ),
            discord.SelectOption(
                label="Giải trí",
                description="Hug, kiss, meme...",
                emoji="❤️‍🔥",
                value="fun"
            ),
            discord.SelectOption(
                label="Thông tin",
                description="Weather, News,...",
                emoji="❄️",
                value="info"
            ),
            discord.SelectOption(
                label= "Toán",
                description= "Giải phương trình, Viết phương trình tổng quát, tham số,...",
                emoji= "📐",
                value= "toan"
            ),
            discord.SelectOption(
                label= "Hoá Học",
                description= "Cân bằng phương trình,..",
                emoji= "🧪",
                value= "hoahoc"
            ),
            discord.SelectOption(
                label= "Vật Lý",
                description= "Tính moment lực,..",
                emoji= "🛸",
                value= "vatly"
            ),
            discord.SelectOption(
                label= "Minecraft",
                description= "Các lệnh đào, nung, bán khoáng sản,...",
                emoji= cupkcicon,
                value= "minecraft"
            ),
            discord.SelectOption(
                label= "Đầu tư",
                description= "Hệ thống MiniGame chứng khoán",
                emoji= "🤑",
                value= "dautu"
            ),
            discord.SelectOption(
                label= "Tình Yêu",
                description= "Hãy bày tỏ tình cảm thật sự của bạn",
                emoji= "❤️",
                value= "tinhyeu"
            ),
            discord.SelectOption(
                label= "Đấu trường",
                description= "Hãy chiến đấu thật phong cách",
                emoji= "⚔️",
                value= "dautruong"
            ),
            discord.SelectOption(
                label= "Slash Commands",
                description= "Xem slash của bot tại đây",
                emoji= "💤",
                value= "slashcommand"
            )
        ]
        super().__init__(
            placeholder=f"Bạn muốn xem danh mục gì nào?",
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        value = self.values[0]

        if value == "minigame":
            embed = discord.Embed(
                title=f"{emoji_7} Kinh tế",
                description=(
                    "**eiucash**: Xem số tiền hiện có.\n\n"
                    "**eiupack**: Xem túi đồ của bạn.\n\n"
                    "**eiucf <Số tiền>**: Tung đồng xu.\n\n"
                    "**eiugive <member> <cash>**: Tặng một thành viên Hcoin.\n\n"
                    "**eiushop**: Mở shop mua vật phẩm.\n\n"
                    "**eiuevent**: Sự Kiện Hội Trợ Hè"
                ),
                color=0xFFC0CB
            )

        elif value == "admin":
            embed = discord.Embed(
                title=f"{emoji_12} Pháp luật",
                description=(
                    "**eiukick <@member> [reason]**: Đuổi một thành viên khỏi server.\n\n"
                    "**eiuban <@member> [reason]**: Cấm một thành viên khỏi server.\n\n"
                    "**eiurole <@member> <role_name>**: Gán vai trò cho thành viên.\n\n"
                    "**eiumute <@member> <time>**: mute member"
                ),
                color=0xFFC0CB
            )

        elif value == "fun":
            embed = discord.Embed(
                title="❤️‍🔥 Giải trí",
                description=(
                    "**eiuserverinfo**: Xem thông tin server.\n\n"
                    "**eiujoin**: Treo trong voice.\n\n"
                    "**eiuroidi**: Rời khỏi kênh voice.\n\n"
                    "**eiuplay <url SoundCloud>**: Phát nhạc trên SoundCloud.\n\n"
                    "**eiudailystudy**: Xem bạn hôm nay sẽ phải học gì.\n\n"
                ),
                color=0xFFC0CB
            )

        elif value == "info":
            embed = discord.Embed(
                title="❄️ Thông tin",
                description=(
                    "**eiusearch <topic>**: Tìm kiếm Wikipedia.\n\n"
                    "**eiuhocba**: Xem học bạ của bạn.\n\n"
                    "**eiufb <url Facebook>**: Lấy thông tìn Facebook của một người dùng.\n\n"
                    "**eiutik <user name>**: Lấy thông tin tiktok của một người dùng"
                ),
                color=0xFFC0CB
            )
        elif value == "toan":
            embed= discord.Embed(
                title= "📐 Toán Học",
                description=(
                    "**eiugiaipt**: Giải PT bậc 2.\n\n"
                    "**eiutongquat**: PT tổng quát đường thẳng.\n\n"
                    "**eiuthamso**: PT tham số đường thẳng."
                ),
                color= 0x38EBE2
            )
        elif value == "hoahoc":
            embed= discord.Embed(
                title= "🧪 Hoá Học",
                description=(
                    "**eiucanbang <PTHH>**: Cân bằng PTHH."
                ),
                color= 0xCCFF00
            )
        elif value == "vatly":
            embed= discord.Embed(
                title= "🛸 Vật Lý",
                description=(
                    "**eiumoment <độ lớn lực tác dụng> <cánh tay đòn>**: Tính moment lực."
                ),
                color= 0xFFFF00
            )
        elif value == "minecraft":
            embed= discord.Embed(
                title= f"{cupkcicon} Minecraft",
                description=(
                    "**eiumine**: Đào khoáng sản.\n\n"
                    "**eiunung**: Nung khoáng sản.\n\n"
                    "**eiusell**: Xem bảng giá thành các loại khoáng sản."
                ),
                color= 0x38EBE2
            )
        elif value == "dautu":
            embed= discord.Embed(
                title= "🤑 Đầu tư",
                description=(
                    "**eiusetupchannel <id channel>**: Set channel để cập nhật thông tin chứng khoán.\n\n"
                    "**eiusellstock <số cổ phiếu>**: Bán cổ phiếu.\n\n"
                    "**eiubuy <số cổ phiếu>**: Mua cổ phiếu.\n\n"
                    "**eiucophieu**: Xem số cổ phiếu bạn đang có."
                ),
                color= 0xCCFF00
            )
        elif value == "tinhyeu":
            embed= discord.Embed(
                title= "❤️ Tình Yêu",
                description=(
                    "**eiukiss <@member>**: Hôn 1 thành viên.\n\n"
                    "**eiuhug <@member>**: Ôm 1 thành viên.\n\n"
                    "**eiuslap <@member>**: Tát 1 thành viên.\n\n"
                    "**eiudailylove <@member>**: Love member.\n\n"
                    "**eiusetlove <@member>**: Kết hôn.\n\n"
                    "**eiuchecklove**: Xem giấy chứng nhận tình yêu.\n\n"
                    "**eiuchiatay**: Chia tay."
                ),
                color= 0xFFC0CB
            )
        elif value == "dautruong":
            embed= discord.Embed(
                title= "⚔️ Đấu trường",
                description=(
                    "**eiupick**: Chọn tướng.\n\n"
                    "**eiufight <@member>**: Chiến đấu với một người.\n\n"
                    "**eiuup**: Nâng cấp tướng của bạn"
                ),
                color= 0x38EBE2
            )
        elif value == "slashcommand":
            embed= discord.Embed(
                title= "Slash Commands",
                description=(
                    "**/makeqr <url>**: Tạo mã QR cho một link bất kì.\n\n"
                    "**/weather <tên thành phố>**: Xem thời tiết.\n\n"
                    "**/avatar <@member>**: Xem avatar thành viên.\n\n"

                    
                ),
                color= 0x38EBE2
            )

        if interaction.response.is_done():
            await interaction.edit_original_response(embed=embed, view=self.view)
        else:
            await interaction.response.edit_message(embed=embed, view=self.view)
class HelpView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)
        self.add_item(HelpSelect())
        
@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def help(ctx):
    embed = discord.Embed(
        title="💖 Trung Tâm Trợ Giúp",
        description=(
            f"{emoji_10} Xin chào tôi là Bot giải trí được phát triển bởi một **Youtuber**, **Tiktoker** đến từ **Việt Nam** [{emoji_13} HanhDun]( https://www.youtube.com/@hanhdun ).\n"
            f"{emoji_11} Tự hào khi được sinh ra và nuôi lớn bởi công dân Việt Nam, tôi đến đây mang đến cho bạn trải nghiệm tuyệt vời, mượt mà và vui vẻ nhất.\n\n"
            "Vui lòng chọn một danh mục bên dưới để xem chi tiết các lệnh.\n\n"
            "🎐**Bạn Nên Bắt Đầu Như Thế Nào?**\n"
            "• Dùng eiudaily mỗi ngày để nhận thêm xu.\n"
            "• Dùng eiucash để xem tình hình kinh tế của bạn.\n"
            "• Dùng eiutut để xem cách đầu tư chứng khoán.\n"
            "• Dùng eiuevent để xem sự kiện đang diễn ra.\n"
        ),
        color=0xFFC0CB
    )

    await ctx.send(embed=embed, view=HelpView())

@help.error
async def giuptoi_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Chờ thêm **{int(error.retry_after)}s** nữa mới dùng lại được")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def serverinfo(ctx):
    guild = ctx.guild
    owner = guild.owner
    embed = discord.Embed(
        title=guild.name,
        description=(
            f"**Owner:** {owner}.\n"
            f"**Members:** {guild.member_count}.\n"
            f"**Roles:** {len(guild.roles) - 1}.\n"
            f"**Categories:** {len(guild.categories)}.\n"
            f"**Text Channels:** {len(guild.text_channels)}.\n"
            f"**Voice Channels:** {len(guild.voice_channels)}.\n"
        ),
        color= 0xFFC0CB
    )
    embed.set_thumbnail(url= guild.icon.url)
    embed.set_footer(text= f"ID: {guild.id} | Server Created: {guild.created_at}")
    await ctx.send(embed=embed)
@serverinfo.error
async def serverinfo_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Chờ thêm **{int(error.retry_after)}s** nữa mới dùng lại được")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def kiss(ctx, member: discord.Member):
    data= load_data()
    user= str(ctx.author.id)
    thanhvien= str(member.id)
    if user not in data:
        embed= discord.Embed(
            title= "Bạn chưa có người yêu",
            color= 0x000000
        )
        await ctx.send(embed=embed)
        return
    if thanhvien not in data:
        embed= discord.Embed(
            title= f"{member.name} chưa có người yêu nên không thể hôn",
            color= 0x000000
        )
        await ctx.send(embed=embed)
        return
    if member.id == ctx.author.id:
        embed=discord.Embed(
            title= "Bạn không thể hôn chính mình",
            color= 0x000000
        )
        await ctx.send(embed=embed)
        return
    if data[user]["ny"] != str(member.id):
        embed=discord.Embed(
            title= "Bạn định ngoại tình hả bạn ? 💔",
            color= 0x000000
        )
        await ctx.send(embed=embed)
        return
    if data[thanhvien]["ny"] != str(ctx.author.id):
        embed=discord.Embed(
            title= f" {member.name} có người yêu rồi, chia buôn với bạn 💔",
            color= 0x000000
        )
        await ctx.send(embed=embed)
        return
    tinhyeu= random.randint(1, 10)
    data[user]["love"] += tinhyeu
    data[thanhvien]["love"] += tinhyeu
    nuhon= random.choice(hon)
    embed= discord.Embed(
        title= f"{emoji_3} {ctx.author} kiss {member.name} 💘",
        description= f"Tình yêu của 2 bạn đã tăng thêm {tinhyeu}%",
        color=0xFFC0CB
    )
    embed.set_image(url= nuhon)
    await ctx.send(embed=embed)
    save_data(data)
@kiss.error
async def kiss_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Chờ thêm **{int(error.retry_after)}s** nữa mới dùng lại được")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Tag thành viên đi baaaa")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def hug(ctx, member: discord.Member):
    data= load_data()
    user= str(ctx.author.id)
    thanhvien= str(member.id)
    if user not in data:
        embed= discord.Embed(
            title= "Bạn chưa có người yêu",
            color= 0x000000
        )
        await ctx.send(embed=embed)
        return
    if thanhvien not in data:
        embed= discord.Embed(
            title= f"{member.name} chưa có người yêu nên không thể ôm",
            color= 0x000000
        )
        await ctx.send(embed=embed)
        return
    if member.id == ctx.author.id:
        embed=discord.Embed(
            title= "Bạn không thể ôm chính mình",
            color= 0x000000
        )
        await ctx.send(embed=embed)
        return
    if data[user]["ny"] != str(member.id):
        embed=discord.Embed(
            title= "Bạn định ngoại tình hả bạn ? 💔",
            color= 0x000000
        )
        await ctx.send(embed=embed)
        return
    if data[thanhvien]["ny"] != str(ctx.author.id):
        embed=discord.Embed(
            title= f" {member.name} có người yêu rồi, chia buôn với bạn 💔",
            color= 0x000000
        )
        await ctx.send(embed=embed)
        return
    om= random.choice(oms)
    tinhyeu= random.randint(1,5)
    data[user]["love"] += tinhyeu
    data[thanhvien]["love"] += tinhyeu
    embed= discord.Embed(
        title= f"{emoji_5} {ctx.author} hug {member.name} ❤️, tình yêu của 2 bạn đã tăng lên {tinhyeu}%",
        color= 0xFFC0CB
    )
    embed.set_image(url= om)
    await ctx.send(embed=embed)
    save_data(data)
@hug.error
async def hug_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Chờ thêm **{int(error.retry_after)}s** nữa mới dùng lại được")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Tag thành viên đi baaaa")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def slap(ctx, member:discord.Member):
    data= load_data()
    user= str(ctx.author.id)
    thanhvien= str(member.id)
    
    if user not in data:
        tat2= random.choice(tat1)
        embed= discord.Embed(
            title= f"{emoji_6} {ctx.author} slap {member.name}",
            color=0xFFC0CB
        )
        embed.set_image(url= tat2)
        await ctx.send(embed=embed)
        return
    if data[user]["ny"] != str(member.id):
        tat2= random.choice(tat1)
        embed= discord.Embed(
            title= f"{emoji_6} {ctx.author} slap {member.name}",
            color=0xFFC0CB
        )
        embed.set_image(url= tat2)
        await ctx.send(embed=embed)
        return
    if data[user]["ny"] == str(member.id):
        tat2= random.choice(tat1)
        tinhyeu= random.randint(1, 20)
        data[user]["love"] -= tinhyeu
        data[thanhvien]["love"] -= tinhyeu
        embed= discord.Embed(
            title= f"{ctx.author} đã tát người yêu của mình {member.name} 💔, tình yêu của 2 bạn đã bị giảm xuống {tinhyeu}%",
            color= 0x00000
        )
        embed.set_image(url= tat2)
        await ctx.send(embed=embed)
        save_data(data)
@slap.error
async def slap_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Chờ thêm **{int(error.retry_after)}s** nữa mới dùng lại được")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Tag thành viên đi baaaa")

@bot.command()
@commands.cooldown(1,86400,commands.BucketType.user)
async def dailylove(ctx, member: discord.Member):
    data= load_data()
    user= str(ctx.author.id)
    thanhvien= str(member.id)
    if user not in data:
        embed= discord.Embed(
            title= "Bạn chưa có người yêu",
            color= 0x000000
        )
        await ctx.send(embed=embed)
        return
    if thanhvien not in data:
        embed= discord.Embed(
            title= f"{member.name} chưa có người yêu",
            color= 0x000000
        )
        await ctx.send(embed=embed)
        return
    if member.id == user:
        embed=discord.Embed(
            title= "Bạn không thể yêu chính mình",
            color= 0x000000
        )
        await ctx.send(embed=embed)
        return
    if data[user]["ny"] != str(member.id):
        embed=discord.Embed(
            title= "Bạn định ngoại tình hả bạn ? 💔",
            color= 0x000000
        )
        await ctx.send(embed=embed)
        return
    if data[thanhvien]["ny"] != str(ctx.author.id):
        embed=discord.Embed(
            title= f" {member.name} có người yêu rồi, chia buôn với bạn 💔",
            color= 0x000000
        )
        await ctx.send(embed=embed)
        return
    khog_bt_dat_ten_bien_la_gi= random.choice(hon)
    love= random.randint(1,5)
    data[user]["love"] += love
    data[thanhvien]["love"] += love
    embed= discord.Embed(
        title= f" {emoji_3} Daily Love ❤️",
        description=(
            f"Tình yêu giữa **{ctx.author}** và **{member.name}** đã tăng thêm {love}%"
        ),
        color= 0xFFC0CB
    )
    embed.set_image(url= khog_bt_dat_ten_bien_la_gi)
    await ctx.send(embed=embed)
    save_data(data)
@dailylove.error
async def dailylove_error(ctx, error):
    gio= round((1/3600) * int(error.retry_after), 1)
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Chờ thêm **{gio}h** nữa mới dùng lại được")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Tag thành viên đi baaaa")

@bot.command()
@commands.cooldown(1,10,commands.BucketType.user)
async def search(ctx, *, topic):
    try:
        wikipedia.set_lang("vi")
        msg= f"Searching for {topic}"
        res= wikipedia.summary(topic, sentences=3)
        await ctx.send(
            f"Searching for **{topic}**:\n"
            f"{res}"
        )
    except PageError:
        try:
            wikipedia.set_lang("eng")
            res = wikipedia.summary(topic, sentences=3)
            await ctx.send(
                f"Không có bài tiếng Việt, mình gửi bản tiếng Anh:\n{res}"
            )
        except:
            await ctx.send(f"Không thể tìm kiếm cho **{topic}**")
@search.error
async def search_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Chờ thêm **{int(error.retry_after)}s** nữa mới dùng lại được")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Bạn tìm kiếm cái gì trên Wiki ?")

class LoveView(discord.ui.View):
    def __init__(self, ctx, member, data):
        super().__init__(timeout=60)  # 3 phút
        self.ctx = ctx
        self.member = member
        self.data = data
        self.message: Optional[discord.Message] = None

    async def on_timeout(self):
        if self.message is not None:
            await self.message.delete()

    @discord.ui.button(label="Chấp nhận", style=discord.ButtonStyle.success)
    async def accept(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id != self.member.id:
            await interaction.response.send_message("Không phải bạn.", ephemeral=True)
            return

        user = str(self.ctx.author.id)
        thanhvien = str(self.member.id)

        self.data[user] = {"love": 0, "ny": thanhvien}
        self.data[thanhvien] = {"love": 0, "ny": user}
        save_data(self.data)

        embed = discord.Embed(
            title=f"{self.ctx.author} Đã kết hôn với {self.member.name}",
            description=f"Xin chúc mừng hai bạn **{self.member.name} và {self.ctx.author}**",
            color=0x38EBE2
        )
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/1439931543710597201/1463161791075848297/Hug_Love_Gif_Hug_Gif_Love_Heart_Gif_Love_You_Gif_Cute_Cartoon_CC.gif?ex=6970d31b&is=696f819b&hm=2d0b62791f977357a27e4e22b0fe73da39fa6ab7406abb03334666fec3d24918"
        )

        await interaction.response.edit_message(embed=embed, view=None)
        self.stop()

    @discord.ui.button(label="Từ chối", style=discord.ButtonStyle.danger)
    async def decline(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id != self.member.id:
            await interaction.response.send_message("Không phải bạn.", ephemeral=True)
            return

        if interaction.message is not None:
            await interaction.message.delete()
        self.stop()


@bot.command()
@commands.cooldown(1,60, commands.BucketType.user)
async def setlove(ctx, member: discord.Member):
    data = load_data()
    user = str(ctx.author.id)
    thanhvien = str(member.id)

    if user in data:
        embed = discord.Embed(
            title="Bạn đã có người yêu rồi",
            color=0x38EBE2
        )
        await ctx.send(embed=embed)
        return

    if thanhvien in data:
        embed = discord.Embed(
            title=f" {member.name} đã có người yêu rồi",
            color=0x38EBE2
        )
        await ctx.send(embed=embed)
        return

    embed = discord.Embed(
        title=f"{ctx.author} sẽ kết hôn với {member.name}",
        description=f"{member.name} có đồng ý lời cầu hôn của {ctx.author} không ?",
        color=0x38EBE2
        )
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/1439931543710597201/1463161791075848297/Hug_Love_Gif_Hug_Gif_Love_Heart_Gif_Love_You_Gif_Cute_Cartoon_CC.gif?ex=6970d31b&is=696f819b&hm=2d0b62791f977357a27e4e22b0fe73da39fa6ab7406abb03334666fec3d24918"
    )
    view = LoveView(ctx, member, data)
    msg = await ctx.send(embed=embed, view=view)
    view.message = msg
@setlove.error
async def setlove_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Chờ thêm **{int(error.retry_after)}s** nữa mới dùng lại được")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Bạn định setlove với ai vậy ? 💔")
@bot.command()
@commands.cooldown(1,10, commands.BucketType.user)
async def checklove(ctx):
    data = load_data()
    guild = ctx.guild
    user = str(ctx.author.id)

    if user not in data:
        embed = discord.Embed(
            title="Bạn chưa có người yêu hoặc đã chia tay",
            color=0x000000
        )
        await ctx.send(embed=embed)
        return

    member =  await bot.fetch_user(int(data[user]["ny"]))

    embed = discord.Embed(
        title=f"{ctx.author} ❤️ {member.name}",
        description=(
            f"Trạng thái: **Người yêu**. {emoji_5}\n"
            f"Độ thân mật: **{data[user]['love']}%** {emoji_3}\n"
            f"Nơi check love: **{guild.name}**.\n"
            "\n"
            f"**Số định danh:**\n"
            f"**{ctx.author}**: {ctx.author.id}.\n"
            f"**{member.name}**: {member.id}"
        ),
        color=0xFFC0CB
    )
    embed.set_thumbnail(url= random.choice(cuoi))
    embed.set_image(url=random.choice(oms))
    await ctx.send(embed=embed)
@checklove.error
async def checklove_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Chờ thêm **{int(error.retry_after)}s** nữa mới dùng lại được")
class BreakupView(discord.ui.View):
    def __init__(self, ctx, lover_id, data):
        super().__init__(timeout=10)
        self.ctx = ctx
        self.lover_id = lover_id
        self.data = data
        self.message: Optional[discord.Message] = None

    async def on_timeout(self):
        if self.message is not None:
            await self.message.delete()

    @discord.ui.button(label="Xác nhận chia tay", style=discord.ButtonStyle.danger)
    async def accept(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id not in [self.ctx.author.id, int(self.lover_id)]:
            await interaction.response.send_message("Không phải bạn.", ephemeral=True)
            return

        user = str(self.ctx.author.id)
        lover = self.lover_id

        self.data.pop(user, None)
        self.data.pop(lover, None)
        save_data(self.data)

        if interaction.message is not None:
            await interaction.message.delete()
        self.stop()

    @discord.ui.button(label="Huỷ", style=discord.ButtonStyle.secondary)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id != self.ctx.author.id:
            await interaction.response.send_message("Không phải bạn.", ephemeral=True)
            return

        if interaction.message is not None:
            await interaction.message.delete()
        self.stop()
@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def chiatay(ctx):
    data = load_data()
    user = str(ctx.author.id)

    if user not in data:
        embed = discord.Embed(
            title="Bạn hiện không có người yêu",
            color=0x38EBE2
        )
        await ctx.send(embed=embed)
        return

    lover_id = data[user]["ny"]
    lover = ctx.guild.get_member(int(lover_id))

    embed = discord.Embed(
        title="Xác nhận chia tay",
        description=f"{ctx.author} và {lover.name} sẽ chia tay",
        color=0x38EBE2
    )

    view = BreakupView(ctx, lover_id, data)
    msg = await ctx.send(embed=embed, view=view)
    view.message = msg
@chiatay.error
async def chiatay_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Chờ thêm **{int(error.retry_after)}s** nữa mới dùng lại được")
def split_message(text, limit=2000):
    return [text[i:i+limit] for i in range(0, len(text), limit)]
@bot.command()
@commands.cooldown(1,10,commands.BucketType.user)
async def giaipt(ctx, a= float(), b= float(), c= float()):
    data= hocvan_data()
    user= str(ctx.author.id)
    if user not in data:
        data[user] = {}
    hocvan= data[user].get("hocvan", 0)
    delta= b**2-4*a*c
    if delta < 0:
        embed= discord.Embed(
            title= "Giải phương trình bậc 2 một ẩn ",
            description=(
                "Phương trình **vô nghiệm**.\n"
                "Bạn vừa giải 1 phương trình:)), bạn nhận được **01** trình độ học vấn"
            ),
            color= 0xFFC0CB
        )
        await ctx.send(embed=embed)
        data[user]["hocvan"] = hocvan + 1
        luu_dulieu(data)
    if delta > 0:
        x1= (-b+ math.sqrt(delta))/(2*a)
        x2= (-b - math.sqrt(delta))/(2*a)
        embed= discord.Embed(
            title= "Giải phương trình bậc 2 một ẩn ",
            description=(
                f"Phương trình có 2 nghiệm phân biệt x1,x2\n"
                f"x1= **{x1}**\n"
                f"x2= **{x2}**\n"
                "Bạn vừa giải 1 phương trình:)), bạn nhận được **01** trình độ học vấn"
            ),
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        data[user]["hocvan"] = hocvan + 1
        luu_dulieu(data)
    if delta == 0:
        x12= -b/(2*a)
        embed= discord.Embed(
            title= "Giải phương trình bậc 2 một ẩn",
            description=(
                f"Phương trình có 2 nghiệm kép x1=x2\n"
                f"x1=x2= **{x12}**\n"
                "Bạn vừa giải 1 phương trình:)), bạn nhận được **01** trình độ học vấn"
            ),
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        data[user]["hocvan"] = hocvan + 1
        luu_dulieu(data)
@giaipt.error
async def giaipt_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("Số nhập vào không hợp lệ")
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Chờ thêm **{int(error.retry_after)}s** nữa mới dùng lại được")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Thiếu số cần nhập vào")

MINECRAFT_FILE= "minecraft.json"
def mc_data():
    if not os.path.exists(MINECRAFT_FILE):
        try:
            with open(MINECRAFT_FILE, "w") as f:
                json.dump({}, f)
        except PermissionError:
            print(f"no write permission {MINECRAFT_FILE}")
            return {}
    try:
        with open(MINECRAFT_FILE, "r") as f:
            return json.load(f)
    except (PermissionError, json.JSONDecodeError) as e:
        print(f"❌ Lỗi đọc file {MINECRAFT_FILE}: {e}")
        return {}
def luu_data(data):
    try:
        with open(MINECRAFT_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except PermissionError:
        print(f"no write permission {MINECRAFT_FILE}")

HOCTAP_FILE= "trinhdohocvan.json"
def hocvan_data():
    if not os.path.exists(HOCTAP_FILE):
        try:
            with open(HOCTAP_FILE, "w") as f:
                json.dump({}, f)
        except PermissionError:
            print(f"khog co quyen viet file")
            return {}
    try:
        with open(HOCTAP_FILE, "r") as f:
            return json.load(f)
    except (PermissionError, json.JSONDecodeError) as e:
        print(f"❌ Lỗi đọc file {MINECRAFT_FILE}: {e}")
        return {}
def luu_dulieu(data):
    try:
        with open(HOCTAP_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except PermissionError:
        print(f"no write permission {MINECRAFT_FILE}")
@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def cash(ctx):
    data= mc_data()
    user= str(ctx.author.id)
    if user not in data:
        embed=discord.Embed(
            title= f"Hiện tại bạn có 0 {emoji_7}",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(
            title= f"**{ctx.author.name}** | Hiện tại bạn có {data[user].get("cash", 0)} {emoji_7}",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
@cash.error
async def cash_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Chờ thêm **{int(error.retry_after)}s** nữa mới dùng lại được")



@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def mine(ctx):
    data = mc_data()
    user = str(ctx.author.id)

    if user not in data:
        data[user] = {}

    data[user].setdefault("pack", {})

    so_luong = random.randint(1, 5)
    item = random.choices(khoangsan, weights=weights, k=1)[0]

    data[user]["pack"][item] = data[user]["pack"].get(item, 0) + so_luong

    luu_data(data)  

    embed = discord.Embed(
        title=f"{cupkcicon} Bạn đào được {so_luong} {item}",
        color=0x38EBE2
    )
    await ctx.send(embed=embed)
@mine.error
async def mine_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Chờ thêm **{int(error.retry_after)}s** nữa mới dùng lại được")
ma_so= ["#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9"]
@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def nung(ctx, code, amount: int):
    data= mc_data()
    user= str(ctx.author.id)
    pack= data[user]["pack"]
    if user not in data:
        embed= discord.Embed(
            title= "Bạn không có khoảng sản",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        return
    if code not in ma_so:
        embed=discord.Embed(
            title= "Khoáng sản không hợp lệ",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        return
    if amount <= 0:
        embed=discord.Embed(
            title= f"Bạn định nung khoáng sản [{code}] với số lượng bao nhiêu vậy ? 💔",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        return
    if pack.get(f"Than {thanicon} [#2]", 0) < amount//2:
        embed= discord.Embed(
            title= f"Bạn không đủ nguyên liệu than để nung khoáng sản",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        return
    if code == "#1":
        if pack.get(f"Đá Cuội {stoneicon} [#1]", 0) < amount:
            embed = discord.Embed(
                title= f"Bạn không đủ {amount} đá cuội",
                color=0x38EBE2
            )
            await ctx.send(embed=embed)
            return
        pack[f"Than {thanicon} [#2]"] -= amount//2
        pack[f"Đá Cuội {stoneicon} [#1]"] -= amount
        pack[f"Đá {dabthicon} [#10]"] = pack.get(f"Đá {dabthicon} [#10]", 0) + amount
        embed=discord.Embed(
            title= f"Đã nung {amount} đá cuội thành {amount} đá {dabthicon}",
            description= f"Bạn đã sử dụng **{amount//2}** số lượng than {thanicon} để nung",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        luu_data(data)
    if code == "#2":
        embed= discord.Embed(
            title= "Bạn không thể nung than đá (nó chỉ để bán)",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
    if code == "#3":
        if pack.get(f"Quặng Sắt {quangsaticon} [#3]", 0) < amount:
            embed= discord.Embed(
                title= f"Bạn không đủ {amount} quặng sắt để nung",
                color= 0x38EBE2
            )
            await ctx.send(embed=embed)
            return
        pack[f"Than {thanicon} [#2]"] -= amount//2
        pack[f"Quặng Sắt {quangsaticon} [#3]"] -= amount
        pack[f"Thỏi sắt {thoisaticon} [#11]"] = pack.get(f"Thỏi sắt {thoisaticon} [#11]", 0) + amount
        embed=discord.Embed(
            title= f"Đã nung {amount} quặng sắt thành {amount} thỏi sắt {thoisaticon}",
            description= f"Bạn đã sử dụng **{amount//2}** số lượng than {thanicon} để nung",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        luu_data(data)
    if code == "#4":
        if pack.get(f"Quặng Đồng {quangdongicon} [#4]", 0) < amount:
            embed=discord.Embed(
                title= f"Bạn không đủ {amount} quặng đồng",
                color= 0x38EBE2
            )
            await ctx.send(embed=embed)
            return
        pack[f"Than {thanicon} [#2]"] -= amount//2
        pack[f"Quặng Đồng {quangdongicon} [#4]"] -= amount
        pack[f"Đồng {dongbthicon} [#12]"] = pack.get(f"Đồng {dongbthicon} [#12]", 0) + amount
        embed=discord.Embed(
            title= F"Đã nung {amount} quặng đồng thành đồng {dongbthicon}",
            description= f"Bạn đã sử dụng **{amount//2}** số lượng than {thanicon} để nung",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        luu_data(data)
    if code == "#5":
        embed= discord.Embed(
            title= "Bạn không thể nung redstone(nó chỉ để bán)",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
    if code == "#6":
        if pack.get(f"Quặng Vàng {quangvang} [#6]", 0) < amount:
            embed= discord.Embed(
                title= f"Bạn không đủ {amount} quặng vàng để nung",
                color= 0x38EBE2
            )
            await ctx.send(embed=embed)
            return
        pack[f"Than {thanicon} [#2]"] -= amount//2
        pack[f"Quặng Vàng {quangvang} [#6]"] -= amount
        pack[f"Thỏi vàng {thoivangicon} [#13]"] = pack.get(f"Thỏi vàng {thoivangicon} [#13]", 0) + amount
        embed= discord.Embed(
            title= f"Đã nung {amount} quặng vàng thành {amount} thỏi vàng",
            description= f"Bạn đã sử dụng **{amount//2}** số lượng than {thanicon} để nung",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        luu_data(data)
    if code == "#7":
        embed= discord.Embed(
            title= "Bạn không thể nung Lapis Lazuli (nó chỉ để bán)",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
    if code == "#8":
        embed= discord.Embed(
            title= "Bạn không thể nung Kim Cương (nó chỉ để bán)",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
    if code == "#9":
        embed= discord.Embed(
            title= "Bạn không thể nung Ngọc Lục Bảo (nó chỉ để bán)",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
@nung.error
async def nung_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Chờ thêm **{int(error.retry_after)}s** nữa mới dùng lại được")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Lỗi cú pháp, cú pháp đúng: **eiunung <mã số khoáng sản> <số lượng khoáng sản cần nung>**")


def open_tui_mu():
    ben_trong_tui_mu1= random.choice(khoangsan)
    ben_trong_tui_mu2= random.randint(1, 50)

    ben_trong_tui_mu3= random.choice([ben_trong_tui_mu1, ben_trong_tui_mu2])

    return ben_trong_tui_mu3


class OpenTuiMu(discord.ui.View):
    def __init__(self, user, data):
        super().__init__(timeout=180)
        self.user = user
        self.data= data
    @discord.ui.button(label= "Mở Túi Mù ?", style= discord.ButtonStyle.green)
    async def dongy_tuimu(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user != self.user:
            await interaction.response.send_message("Có phải đồ của bạn đâu ? 💔", ephemeral= True)
            return
        user_key = str(self.user.id)
        user_data = self.data.setdefault(user_key, {})
        pack_data = user_data.setdefault("pack", {})
        pack_data.setdefault("Túi mù", 0)

        if pack_data.get("Túi mù", 0) == 0:
            embed= discord.Embed(
                title= "Bạn không có túi mù trong túi, làm ơn hãy vào shop mua đi 💔",
                color= 0x38EBE2
            )
            await interaction.response.edit_message(embed=embed, view= None)
            return
        bttm= open_tui_mu()
        if type(bttm) == int:
            user_data["cash"] = user_data.get("cash", 0) + bttm
            pack_data["Túi mù"] = max(0, pack_data.get("Túi mù", 0) - 1)
            embed= discord.Embed(
                title= "🎁 MỞ TÚI MÙ 🎁",
                description= f"✨ {self.user.name} đã mở túi mù...\n\n và bạn ấy đã nhận được **{bttm}** Hcoin",
                color= 0x38EBE2
            )
            await interaction.response.edit_message(embed= embed, view= None)
            luu_data(self.data)
        else:
            pack_data["Túi mù"] = max(0, pack_data.get("Túi mù", 0) - 1)
            pack_data[bttm] = pack_data.get(bttm, 0) + 5
            embed= discord.Embed(
                title= "🎁 MỞ TÚI MÙ 🎁",
                description= f"✨ {self.user.name} đã mở túi mù...\n\n và bạn ấy đã nhận được 5 **{bttm}**",
                color= 0x38EBE2
            )
            await interaction.response.edit_message(embed=embed, view= None)
            luu_data(self.data)
async def show_pack_inventory(ctx):
    """Hiển thị nội dung túi đồ (pack) của người dùng."""
    data = mc_data()
    user = str(ctx.author.id)

    if user not in data or not data[user].get("pack"):
        embed = discord.Embed(
            title="🎒 Túi đồ rỗng",
            description="Bạn chưa có đồ nào trong túi. Dùng `!mine` để đào khoáng sản.",
            color=0x38EBE2
        )
        await ctx.send(embed=embed)
        return

    pack = data[user].get("pack", {})
    embed = discord.Embed(
        title=f"🎒 Túi đồ của {ctx.author.display_name}",
        color=0x38EBE2
    )

    for item, qty in pack.items():
        embed.add_field(name=item, value=str(qty), inline=False)
    view= OpenTuiMu(ctx.author, data)
    await ctx.send(embed=embed, view= view)


ma_so_full= ma_so= ["#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9", "#10", "#11", "#12", "#13"]

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def sell(ctx, code, amount: int):
    data= mc_data()
    user= str(ctx.author.id)
    if user not in data:
        embed= discord.Embed(
            title= "Bạn không có khoáng sản",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        return
    if code not in ma_so_full:
        embed= discord.Embed(
            title= "Mã số khoáng sản không hợp lệ",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        return
    if amount <= 0:
        embed= discord.Embed(
            title= f"Bạn định bán khoáng sản có mã số [{code}] với số lượng bao nhiêu vậy ? 💔",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        return
    pack= data[user]["pack"]
    cash= data[user].get("cash", 0)
    if code == "#1":
        if pack.get(f"Đá Cuội {stoneicon} [#1]", 0) < amount:
            embed= discord.Embed(
                title= f"Bạn không đủ {amount} khoáng sản để bán",
                color= 0x38EBE2
            )
            await ctx.send(embed=embed)
            return
        pack[f"Đá Cuội {stoneicon} [#1]"] -= amount
        data[user]["cash"] = cash + amount*10
        embed= discord.Embed(
            title= f"Bạn đã bán đi {amount} đá cuội và nhận lại {amount} {emoji_7}",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        luu_data(data)
    if code == "#2":
        if pack.get(f"Than {thanicon} [#2]", 0):
            embed= discord.Embed(
                title= f"Bạn không đủ {amount} than để bán",
                color= 0x38EBE2
            )
            await ctx.send(embed=embed)
            return
        pack[f"Than {thanicon} [#2]"] -= amount
        data[user]["cash"] = cash + amount*20
        embed= discord.Embed(
            title= f"Bạn đã bán đi {amount} than và nhận lại {amount*2} {emoji_7}",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        luu_data(data)
    if code == "#3":
        if pack.get(f"Quặng Sắt {quangsaticon} [#3]", 0) < amount:
            embed=discord.Embed(
                title= f"Bạn không đủ {amount} quặng sắt để bán",
                color= 0x38EBE2
            )
            await ctx.send(embed=embed)
            return
        pack[f"Quặng Sắt {quangsaticon} [#3]"] -= amount
        data[user]["cash"] = cash + amount*20
        embed= discord.Embed(
            title= f"Bạn đã bán {amount} quặng sắt và nhận lại {amount*2} {emoji_7}",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        luu_data(data)
    if code == "#4":
        if pack.get(f"Quặng Đồng {quangdongicon} [#4]", 0) < amount:
            embed= discord.Embed(
                title= f"Bạn không đủ {amount} quặng đồng để bán",
                color= 0x38EBE2
            )
            await ctx.send(embed=embed)
            return
        pack[f"Quặng Đồng {quangdongicon} [#4]"] -= amount
        data[user]["cash"] = cash + amount*20
        embed= discord.Embed(
            title= f"Bạn đã bán {amount} quặng đồng và nhận lại {amount*2} {emoji_7}",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        luu_data(data)
    if code == "#5":
        if pack.get(f"Redstone {redstoneicon} [#5]", 0) < amount:
            embed= discord.Embed(
                title= f"Bạn không đủ {amount} redstone để bán",
                color= 0x38EBE2
            )
            await ctx.send(embed=embed)
            return
        pack[f"Redstone {redstoneicon} [#5]"] -= amount
        data[user]["cash"] = cash + amount*20
        embed= discord.Embed(
            title= f"Bạn đã bán {amount} redstone và nhận lại {amount*6} {emoji_7}",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        luu_data(data)
    if code == "#6":
        if pack.get(f"Quặng Vàng {quangvang} [#6]", 0) < amount:
            embed= discord.Embed(
                title= f"Bạn không đủ {amount} quặng vàng để bán",
                color= 0x38EBE2
            )
            await ctx.send(embed=embed)
            return
        pack[f"Quặng Vàng {quangvang} [#6]"] -= amount
        data[user]["cash"] = cash + amount * 30
        embed= discord.Embed(
            title= f"Bạn đã bán {amount} quặng vàng và nhận lại {amount*5} {emoji_7}",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        luu_data(data)
    if code == "#7":
        if pack.get(f"Lapis Lazuli {lapidicon} [#7]", 0) < amount:
            embed= discord.Embed(
                title= f"Bạn không đủ {amount} lapis lazuli để bán",
                color= 0x38EBE2
            )
            await ctx.send(embed=embed)
            return
        pack[f"Lapis Lazuli {lapidicon} [#7]"] -= amount
        data[user]["cash"] = cash + amount*50
        embed= discord.Embed(
            title= f"Bạn đã bán {amount} lapis lazuli và nhận lại {amount*7} {emoji_7}",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        luu_data(data)
    if code == "#8":
        if pack.get(f"Kim cương {kimcuongicon} [#8]", 0) < amount:
            embed= discord.Embed(
                title= f"Bạn không {amount} đủ kim cương để bán",
                color= 0x38EBE2
            )
            await ctx.send(embed=embed)
            return
        pack[f"Kim cương {kimcuongicon} [#8]"] -= amount
        data[user]["cash"] = cash + amount*200
        embed= discord.Embed(
            title= f"Bạn đã bán {amount} kim cương và nhận lại {amount*20} {emoji_7}",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        luu_data(data)
    if code == "#9":
        if pack.get(f"Ngọc lục bảo {ngoclucbaoicon} [#9]", 0) < amount:
            embed= discord.Embed(
                title= f"Bạn không đủ {amount} ngọc lục bảo để bán",
                color= 0x38EBE2
            )
            await ctx.send(embed=embed)
            return
        pack[f"Ngọc lục bảo {ngoclucbaoicon} [#9]"] -= amount
        data[user]["cash"] = cash + amount*150
        embed= discord.Embed(
            title= f"Bạn đã bán {amount} ngọc lục bảo và nhận lại {amount*17} {emoji_7}",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        luu_data(data)
    if code == "#10":
        if pack.get(f"Đá {dabthicon} [#10]", 0) < amount:
            embed= discord.Embed(
                title= f"Bạn không đủ {amount} đá để bán",
                color= 0x38EBE2
            )
            await ctx.send(embed=embed)
            return
        pack[f"Đá {dabthicon} [#10]"] -= amount
        data[user]["cash"] = cash + amount*15
        embed= discord.Embed(
            title= f"Bạn đã bán {amount} đá và nhận lại {amount+amount} {emoji_7}",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        luu_data(data)
    if code == "#11":
        if pack.get(f"Thỏi sắt {thoisaticon} [#11]", 0) < amount:
            embed= discord.Embed(
                title= f"Bạn không đủ {amount} thỏi sắt để bán",
                color= 0x38EBE2
            )
            await ctx.send(embed=embed)
            return
        pack[f"Thỏi sắt {thoisaticon} [#11]"] -= amount
        data[user]["cash"] = cash + amount*40
        embed= discord.Embed(
            title= f"Bạn đã bán {amount} thỏi sắt và nhận lại {amount*40} {emoji_7}",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        luu_data(data)
    if code == "#12":
        if pack.get(f"Đồng {dongbthicon} [#12]", 0) < amount:
            embed= discord.Embed(
                title= f"Bạn không đủ {amount} đồng để bán",
                color= 0x38EBE2
            )
            await ctx.send(embed=embed)
            return
        pack[f"Đồng {dongbthicon} [#12]"] -= amount
        data[user]["cash"] = cash + amount*35
        embed= discord.Embed(
            title= f"Bạn đã bán {amount} đồng và nhận lại {amount*4} {emoji_7}",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        luu_data(data)
    if code == "#13":
        a= random.randint(10, 50)
        if pack.get(f"Thỏi vàng {thoivangicon} [#13]", 0) < amount:
            embed= discord.Embed(
                title= f"Bạn không đủ {amount} thỏi vàng để bán",
                color= 0x38EBE2
            )
            await ctx.send(embed=embed)
            return
        pack[f"Thỏi vàng {thoivangicon} [#13]"] -= amount
        data[user]["cash"] = cash+ amount*a
        embed= discord.Embed(
            title= f"Bạn đã bán {amount} thỏi vàng và nhận lại {amount*a} {emoji_7}",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        luu_data(data)
@sell.error
async def sell_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Chờ thêm **{int(error.retry_after)}s** nữa mới dùng lại được")
    elif isinstance(error, commands.MissingRequiredArgument):
        embed= discord.Embed(
            title= f"Bảng giá thành các loại khoáng sản {cupkcicon}",
            description=(
                f"**Đá cuội {stoneicon} [#1]:** 10 Hcoin.\n"
                "\n"
                f"**Than {thanicon} [#2]:** 20 Hcoin.\n"
                "\n"
                f"**Quặng Sắt {quangsaticon} [#3]:** 20 Hcoin.\n"
                "\n"
                f"**Quặng Đồng {quangdongicon} [#4]:** 20 Hcoin.\n"
                "\n"
                f"**Redstone {redstoneicon} [#5]:** 20 Hcoin.\n"
                "\n"
                f"**Quặng Vàng {quangvang} [#6]:** 30 Hcoin.\n"
                "\n"
                f"**Lapis Lazuli {lapidicon} [#7]:** 50 Hcoin.\n"
                "\n"
                f"**Kim cương {kimcuongicon} [#8]:** 200 Hcoin.\n"
                "\n"
                f"**Ngọc lục bảo {ngoclucbaoicon} [#9]:** 150 Hcoin.\n"
                "\n"
                f"**Đá {dabthicon} [#10]:** 15 Hcoin.\n"
                "\n"
                f"**Thỏi Sắt {thoisaticon} [#11]:** 40 Hcoin.\n"
                "\n"
                f"**Đồng {dongbthicon} [#12]:** 35 Hcoin.\n"
                "\n"
                f"**Thỏi Vàng {thoivangicon} [#13]:** 10-50 Hcoin.\n"
            ),
            color= 0x38EBE2
        )
        await ctx.send(content="Command sell: **eiusell <mã số khoáng sản> <số lượng khoáng sản>**", embed=embed)





# Hàm phân tích công thức hoá học

def phan_tich_cong_thuc(cong_thuc):
    stack = [{}]
    i = 0

    while i < len(cong_thuc):
        ky_tu = cong_thuc[i]

        if ky_tu == "(":
            stack.append({})
            i += 1

        elif ky_tu == ")":
            i += 1
            so = ""
            while i < len(cong_thuc) and cong_thuc[i].isdigit():
                so += cong_thuc[i]
                i += 1
            he_so = int(so) if so else 1

            nhom = stack.pop()
            for nt in nhom:
                stack[-1][nt] = stack[-1].get(nt, 0) + nhom[nt] * he_so

        else:
            match = re.match(r"([A-Z][a-z]?)(\d*)", cong_thuc[i:])
            if match:
                nt = match.group(1)
                so = int(match.group(2)) if match.group(2) else 1
                stack[-1][nt] = stack[-1].get(nt, 0) + so
                i += len(match.group(0))
            else:
                i += 1

    return stack[0]
loi_giai= []

# Hàm cân bằng phương trình
def can_bang_va_giai(phuong_trinh):
    trai, phai = phuong_trinh.split("->")
    chat_trai = [c.strip() for c in trai.split("+")]
    chat_phai = [c.strip() for c in phai.split("+")]

    tat_ca = chat_trai + chat_phai
    bang_phan_tich = []
    tap_nguyen_to = set()

    for chat in tat_ca:
        pt = phan_tich_cong_thuc(chat)
        bang_phan_tich.append(pt)
        tap_nguyen_to.update(pt.keys())

    ds_nt = list(tap_nguyen_to)
    ma_tran = []

    for nt in ds_nt:
        hang = []
        for i, pt in enumerate(bang_phan_tich):
            sl = pt.get(nt, 0)
            if i >= len(chat_trai):
                sl *= -1
            hang.append(sl)
        ma_tran.append(hang)

    M = Matrix(ma_tran)
    nghiem = M.nullspace()[0]
    bcnn = lcm([x.q for x in nghiem])
    he_so = [abs(int(x * bcnn)) for x in nghiem]

    loi_giai = []
    loi_giai.append(f"**Nguyên tố tham gia:** `{', '.join(ds_nt)}`")
    loi_giai.append("**Bảng bảo toàn:**")

    for i, nt in enumerate(ds_nt):
        loi_giai.append(f"`{nt}: {ma_tran[i]}`")

    ket_trai = []
    ket_phai = []

    for i, c in enumerate(chat_trai):
        hs = he_so[i]
        ket_trai.append(f"`{hs if hs > 1 else ''}{c}`")

    for i, c in enumerate(chat_phai):
        hs = he_so[i + len(chat_trai)]
        ket_phai.append(f"`{hs if hs > 1 else ''}{c}`")

    ket_qua = " + ".join(ket_trai) + " -> " + " + ".join(ket_phai)
    return ket_qua, "\n".join(loi_giai)

@bot.command()
async def canbang(ctx, *, phuong_trinh):
    try:
        data= hocvan_data()
        user= str(ctx.author.id)
        trinh_la_gi_ma_la_trinh_ai_cham= random.randint(1, 10)
        if user not in data:
            data[user]= {}
        hocvan= data[user].get("hocvan", 0)
        ket_qua = can_bang_va_giai(phuong_trinh)
        data[user]["hocvan"] = hocvan + trinh_la_gi_ma_la_trinh_ai_cham
        await ctx.send("**Phương trình đã cân bằng:**")
        for i in range(0, len(ket_qua)):
            await ctx.send(
                f"{ket_qua[i]}.\n"
            )
        await ctx.send(f"Bạn vửa cân bằng 1 phương trình hoá học:)), bạn nhận được **{trinh_la_gi_ma_la_trinh_ai_cham}** trình độ học vấn")
        luu_dulieu(data)
    except:
        await ctx.send(
            "Lỗi cú pháp!\nVD đúng: `H2 + O2 -> H2O`"
        )



@bot.command()
async def tongquat(ctx, x:float, y:float, toadox:float, toadoy:float):
    data= hocvan_data()
    user= str(ctx.author.id)
    if user not in data:
        data[user]= {}
    hocvan= data[user].get("hocvan", 0)
    data[user]["hocvan"] = hocvan + 1
    embed= discord.Embed(
        title= f"Phương trình tổng quát của đường thẳng đi qua điểm ({toadox};{toadoy}) và có vectơ pháp tuyến ({x};{y}) là:",
        description= (
            f"**{x}x - {x*toadox} + {y}y - {toadoy*y} = 0**\n"
            "Bạn vừa viết 1 phương trình tổng quát:)), bạn nhận được **01** trình độ học vấn"
        ),
        color=0x38EBE2
    )
    await ctx.send(embed=embed)
    luu_dulieu(data)
@tongquat.error
async def tongquat_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("Số nhập vào không hợp lệ")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Cú pháp: **eiutongquat** `<toạ độ x của vectơ pháp tuyến>` `<toạ độ y của vectơ pháp tuyến>` *<toạ độ x của điểm mà đường thẳng đi qua>* *<toạ độ y của điểm mà đường thẳng đi qua>*")
        await ctx.send("VD: eiutongquat 4 -2 1 1 ")


@bot.command()
async def thamso(ctx, x:float, y:float, toadox:float, toadoy:float):
    data= hocvan_data()
    user= str(ctx.author.id)
    if user not in data:
        data[user]= {}
    hocvan= data[user].get("hocvan", 0)
    data[user]["hocvan"] = hocvan + 1
    embed=discord.Embed(
        title= f"Phương trình tham số của đường thẳng đi qua điểm ({toadox};{toadoy}) và có vectơ chỉ phương ({x};{y}) là:",
        description=(
            f"**x= {toadox} + {x}t**\n"
            f"**y= {toadoy} + {y}t**\n"
            "**(Với t thuộc số thực)**.\n"
            "Bạn vừa viết 1 phương trình tham số:)), bạn nhận được **01** trình độ học vấn"
        ),
        color= 0x38EBE2
    )
    await ctx.send(embed=embed)
    luu_dulieu(data)
@thamso.error
async def thamso_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("Số nhập vào không hợp lệ")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Cú pháp: **eiuthamso** `<toạ độ x của vectơ chỉ phương>` `<toạ độ y của vectơ chỉ phương>` *<toạ độ x của điểm mà đường thẳng đi qua>* *<toạ độ y của điểm mà đường thẳng đi qua>*")
        await ctx.send("VD: eiuthamso 2 -1 1 2")

@bot.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def daily(ctx):
    data= mc_data()
    user= str(ctx.author.id)
    if user not in data:
        data[user] = {}
    tien= random.randint(1, 10)
    idk= data[user].get("cash", 0)
    data[user]["cash"]= idk + tien
    embed= discord.Embed(
        title= f"Chúc mừng, ngày hôm nay bạn đã nhận được {tien} {emoji_7}",
        color= 0x38EBE2
    )
    await ctx.send(embed=embed)
    luu_data(data)
@daily.error
async def daily_error(ctx, error):
    gio= round((1/3600) * int(error.retry_after), 1)
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Chờ thêm **{gio}h** nữa mới dùng lại được")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def gay(ctx):
    do_gay_lo= random.randint(1, 100)
    embed= discord.Embed(
        title= f"Mức độ gay của bạn: {do_gay_lo}% 💔",
        color= 0x38EBE2
    )
    await ctx.send(embed=embed)
@gay.error
async def gay_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Chờ thêm **{int(error.retry_after)}s** nữa mới dùng lại được")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def moment(ctx, luc: float, canhtaydon: float):
    data= hocvan_data()
    user= str(ctx.author.id)
    if user not in data:
        data[user] = {}
    hocvan = data.get(user, {}).get("hocvan", 0)
    moment_luc= luc*canhtaydon
    embed= discord.Embed(
        title= f"Moment lực của lực **{luc}N** và cánh tay đòn **{canhtaydon}m** là:",
        description=(
            f"M= {moment_luc} N.m\n"
            f"Bạn đã nhận thêm được **01** trình độ học vấn"
        ),
        color= 0x38EBE2
    )
    await ctx.send(embed=embed)
    data[user]["hocvan"] = hocvan + 1
    luu_dulieu(data)
@moment.error
async def moment_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Chờ thêm **{int(error.retry_after)}s** nữa mới dùng lại được")
    if isinstance(error, commands.BadArgument):
        await ctx.send("Synxtax Error")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Thiếu số nhập vào")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def hocba(ctx):
    data= hocvan_data()
    user= str(ctx.author.id)
    if user not in data:
        embed= discord.Embed(
            title= "Bạn **không có** trình độ học vấn, làm ơn hãy học đi 💔",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        return
    hocvan= data[user].get("hocvan", 0)
    if hocvan < 100:
        embed= discord.Embed(
            title= f"📚 Học bạ của {ctx.author}",
            description=(
                "**Cấp bậc:** Mầm non 👶\n"
                f"**Trình độ học vấn:** {hocvan}.\n"
                f"**Giáo viên chủ nhiệm:** HanhDun love you ❤️ ౨ৎ"
            ),
            color= 0x38EBE2
        )
        embed.set_image(url= "https://cdn.discordapp.com/attachments/1439931543710597201/1472593168665936179/download.gif?ex=699322c2&is=6991d142&hm=57fd34321574cb9ab4475c2a88f116fe27f295c96e81afc0a67e9d581a567627")
        await ctx.send(embed=embed)
    elif hocvan >= 50:
        embed= discord.Embed(
            title= f"📚 Học bạ của {ctx.author}",
            description=(
                "**Cấp bậc:** Tiểu học 🧒\n"
                f"**Trình độ học vấn:** {hocvan}.\n"
                f"**Giáo viên chủ nhiệm:** HanhDun love you ❤️ ౨ৎ"
            ),
            color= 0x38EBE2
        )
        embed.set_image(url= "https://cdn.discordapp.com/attachments/1439931543710597201/1472593455703134341/download_1.gif?ex=69932307&is=6991d187&hm=74e58b9c86bf78d4bb972231970b0b8016fe6e1585cf67bac69332e920770759")
        await ctx.send(embed=embed)
    elif hocvan >= 100:
        embed= discord.Embed(
            title= f"📚 Học bạ của {ctx.author}",
            description=(
                "**Cấp bậc:** Trung học cơ sở 🥳\n"
                f"**Trình độ học vấn:** {hocvan}.\n"
                f"**Giáo viên chủ nhiệm:** HanhDun love you ❤️ ౨ৎ"
            ),
            color= 0x38EBE2
        )
        embed.set_image(url= "https://cdn.discordapp.com/attachments/1439931543710597201/1472594012882997379/anime_gif.gif?ex=6993238c&is=6991d20c&hm=b9730130672fcad431296b83d9346faf29403ea58778749f413babcba8647b4c")
        await ctx.send(embed=embed)
    elif hocvan >= 200:
        embed= discord.Embed(
            title= f"📚 Học bạ của {ctx.author}",
            description=(
                "**Cấp bậc:** Trung học phổ thông 🎓\n"
                f"**Trình độ học vấn:** {hocvan}.\n"
                f"**Giáo viên chủ nhiệm:** HanhDun love you ❤️ ౨ৎ"
            ),
            color= 0x38EBE2
        )
        embed.set_image(url= "https://cdn.discordapp.com/attachments/1439931543710597201/1472594387031556096/download_2.gif?ex=699323e5&is=6991d265&hm=fc2f337950fb7da516db5ac6541caf576853e6ea421717a9f824a5efdedbe41d")
        await ctx.send(embed=embed)
@hocba.error
async def hocba_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Chờ thêm **{int(error.retry_after)}s** nữa mới dùng lại được")

@bot.command()
async def join(ctx):
    if not ctx.author.voice:
        await ctx.send("Bạn chưa vào voice")
        return

    channel = ctx.author.voice.channel

    if ctx.voice_client:
        if ctx.voice_client.channel != channel:
            await ctx.voice_client.move_to(channel)
    else:
        await channel.connect(reconnect=True)

face= ["<:matngua:1472580866227179678>", "<:matsap:1472581401013387368>"]

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def cf(ctx, amount: str):
    data = mc_data()
    user = str(ctx.author.id)
    if user not in data:
        data[user] = {}

    cash = int(data[user].get("cash", 0) or 0)
    amount_str = str(amount).strip().lower()

    if amount_str == "all":
        bet = cash
        if bet <= 0:
            await ctx.send("Bạn không có Hcoin")
            return
    else:
        try:
            bet = int(amount_str)
        except Exception:
            await ctx.send("Số tiền cược chỉ có thể là số nguyên dương hoặc `all`")
            return

        if bet <= 0:
            await ctx.send("Số tiền cược phải lớn hơn 0")
            return

        if cash < bet:
            await ctx.send(f"Bạn không đủ {bet} {emoji_7}")
            return

    msg = await ctx.send("Bạn tung đồng xu ra mặt...")
    await asyncio.sleep(2)
    mat = random.choice(face)

    mat_ngua = face[0]
    win = (mat == mat_ngua)

    if win:
        new_cash = cash + bet
        data[user]["cash"] = new_cash
        luu_data(data)
        await msg.edit(content=f"**Mặt ngửa 🎉** bạn thắng **{bet}** {emoji_7} | Số dư: **{new_cash}**")
    else:
        new_cash = cash - bet
        data[user]["cash"] = new_cash
        luu_data(data)
        await msg.edit(content=f"**Mặt sấp 💔** bạn mất **{bet}** {emoji_7} | Số dư: **{new_cash}**")
    return
    
@cf.error
async def cf_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Bạn cược cho ván tung đồng xu này là bao nhiêu? 💔")
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Chờ thêm **{int(error.retry_after)}s** nữa mới dùng lại được")
STOCK_FILE = "stock.json"
CONFIG_FILE = "config.json"
def load_config():
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {"guilds": {}}

def save_config(data):
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f, indent=4)
def save_stock(data):
    with open(STOCK_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_stock():
    if not os.path.exists(STOCK_FILE):
        data = {"price": 50, "history": []}
        save_stock(data)
        return data

    try:
        with open(STOCK_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {"price": 50, "history": []}
@tasks.loop(seconds=60*3) 
async def update_stock_price():
    data = load_stock()
    old_price = data.get("price", 50)
    change = random.randint(-3, 3)
    new_price = max(1, old_price + change)

    candle = {
        "time": datetime.now().isoformat(),
        "open": old_price,
        "close": new_price,
        "high": max(old_price, new_price) + random.randint(0, 2),
        "low": min(old_price, new_price) - random.randint(0, 2)
    }
    if "history" not in data:
        data["history"] = []
    data["price"] = new_price
    data["history"].append(candle)
    data["history"] = data["history"][-31:]  
    save_stock(data)
def ve_bieu_do_realtime():
    data = load_stock()
    if not data["history"]:
        return None

    df = pd.DataFrame(data["history"])
    df["time"] = pd.to_datetime(df["time"])
    df.set_index("time", inplace=True)
    df= df.tail(35)

    fig, axlist = mpf.plot(
        df,
        type="candle",
        xrotation=0,
        style="charles",
        ylabel="Giá",

        # 🔥 kéo sát biểu đồ
        xlim=(df.index[0], df.index[-1]),
        figsize=(16, 9),
        datetime_format="%H:%M",

        returnfig=True,   # 🔥 BẮT BUỘC
    )

    ax = axlist[0]
    ax.set_title("Tình yêu của anh dành cho em <3", fontsize=20, pad=5)
    # 🔥 chỉnh title thủ công
    plt.xticks(rotation=30, fontsize=9)
    fig.savefig("chart.png", dpi=120, bbox_inches="tight")
    plt.close(fig)

    return "chart.png"

@tasks.loop(seconds=600)
async def send_stock_chart():
    config = load_config()
    guilds = config.get("guilds", {})

    for guild_id, guild_data in guilds.items():
        channel_id = guild_data.get("stock_channel_id")
        message_id = guild_data.get("stock_message_id")

        if not channel_id:
            continue

        channel = bot.get_channel(channel_id)
        if not isinstance(channel, discord.TextChannel):
            continue

        file_path = ve_bieu_do_realtime()
        if not file_path:
            continue

        file = discord.File(file_path, filename="chart.png")

        embed = discord.Embed(
            title="Trading cẩn thận không là xuống gầm cầu ngủ đó <:khoc:1474751118469894276>",
            color=0x38EBE2
        )
        embed.set_image(url="attachment://chart.png")

        if not message_id:
            msg = await channel.send(embed=embed, file=file)

            guild_data["stock_message_id"] = msg.id
            save_config(config)

        else:
            try:
                msg = await channel.fetch_message(message_id)
                await msg.edit(embed=embed, attachments=[file])
            except:
                msg = await channel.send(embed=embed, file=file)
                guild_data["stock_message_id"] = msg.id
                save_config(config)
@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
@commands.has_permissions(administrator=True)
async def setupchannel(ctx, channel: discord.TextChannel):
    config = load_config()

    if "guilds" not in config:
        config["guilds"] = {}

    guild_id = str(ctx.guild.id)

    if guild_id not in config["guilds"]:
        config["guilds"][guild_id] = {}

    config["guilds"][guild_id]["stock_channel_id"] = channel.id

    save_config(config)

    embed = discord.Embed(
        title=f"Đã setup kênh **{channel.mention}** cho game đầu tư",
        color=0xFFC0CB
    )
    embed.set_footer(text="Lưu ý: Thị trường sẽ được cập nhật bằng cách edit ảnh, vui lòng setup channel riêng tránh làm trôi tin nhắn")
    await ctx.send(embed=embed)


@setupchannel.error
async def setupchannel_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Chờ thêm **{int(error.retry_after)}s** nữa mới dùng lại được")
    if isinstance(error, commands.BadArgument):
        await ctx.send("**ID channel** không hợp lệ")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Lỗi cú pháp: **Thiếu id channel**")

def get_current_price():
    data = load_stock()
    if not data["history"]:
        return data.get("price", 0)
    return data["history"][-1]["close"]

@bot.command()
@commands.cooldown(1,20,commands.BucketType.user)
async def buy(ctx, amount: int):
    if amount < 0:
        embed=discord.Embed(
            title= "Bạn mua cổ phiếu cho người âm phủ hả bạn? 💔",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        return
    if amount == 0:
        embed=discord.Embed(
            title= "Mua 0 cổ phiếu thì mua làm gì? 💔",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        return
    price= get_current_price()
    cost= price * amount
    data = mc_data()
    user = str(ctx.author.id)
    if user not in data:
        data[user] = {}
    if data[user]["cash"] < cost:
        embed= discord.Embed(
            title= f"Bạn không đủ {cost} {emoji_7}",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        return
    else:
        data[user]["cash"] = data[user].get("cash",0) - cost
        data[user].setdefault("stocks", {})
        data[user]["stocks"]["HDPE"] = data[user]["stocks"].get("HDPE", 0) + amount

        luu_data(data)
        embed= discord.Embed(
            title= f"{ctx.author} đã mua cổ phiếu với giá {cost} {emoji_7}",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
@buy.error
async def buy_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Chờ thêm **{int(error.retry_after)}s** nữa mới dùng lại được")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("**Lỗi cú pháp, cú pháp đúng:** `eiubuy <số cổ phiếu>`")
    if isinstance(error, commands.BadArgument):
        await ctx.send("Số cổ phiếu bạn muốn mua chỉ có thể là số nguyên")
@bot.command()
@commands.cooldown(1,10, commands.BucketType.user)
async def cophieu(ctx):
    data= mc_data()
    user= str(ctx.author.id)
    if user not in data:
        embed= discord.Embed(
            title= "Bạn chưa mua cổ phiếu",
            color= 0xFFC0CB
        )
        await ctx.send(embed=embed)
        return
    so_co_phieu= data[user]["stocks"].get("HDPE", 0)
    if so_co_phieu == 0:
        embed=discord.Embed(
            title= "Bạn chưa mua cổ phiếu",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        return
    else:
        embed= discord.Embed(
            title= f"Bạn đang có {so_co_phieu} cổ phiếu",
            color= 0x38EBE2
        )
        embed.set_image(url= "https://cdn.discordapp.com/attachments/1439931543710597201/1474689758352638094/download.gif?ex=699ac35c&is=699971dc&hm=c94fd186a7ec1c155ef6f49eedffd531244e471287f16fd048377f548f149589")
        await ctx.send(embed=embed)
@cophieu.error
async def cophieu_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Chờ thêm **{int(error.retry_after)}s** nữa mới dùng lại được")


@bot.command()
@commands.cooldown(1,20,commands.BucketType.user)
async def sellstock(ctx, amount:int):
    if amount < 0:
        embed=discord.Embed(
            title= "Bạn bán cổ phiếu cho người âm phủ hả bạn? 💔",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        return
    if amount == 0:
        embed=discord.Embed(
            title= "Bán 0 cổ phiếu thì bán làm gì? 💔",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        return
    price= get_current_price()
    data= mc_data()
    user= str(ctx.author.id)
    if user not in data:
        data[user] = {}
    if "stocks" not in data[user]:
        embed= discord.Embed(
            title= "Bạn chưa mua cổ phiếu",
            color= 0xFFC0CB
        )
        await ctx.send(embed=embed)
        return
    if data[user]["stocks"].get("HDPE", 0) < amount:
        embed= discord.Embed(
            title= f"Bạn không đủ {amount} cổ phiếu để bán",
            color= 0xFFC0CB
        )
        await ctx.send(embed=embed)
        return
    data[user]["stocks"]["HDPE"] -= amount
    data[user]["cash"] = data[user].get("cash",0)  + price * amount
    embed= discord.Embed(
            title= f"{ctx.author} đã bán {amount} cổ phiếu với giá {price*amount} {emoji_7}",
            color= 0x38EBE2
    )
    await ctx.send(embed=embed)
    luu_data(data)
@sellstock.error
async def sellstock_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Chờ thêm **{int(error.retry_after)}s** nữa mới dùng lại được")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("**Lỗi cú pháp, cú pháp đúng:** `eiusell <số cổ phiếu>`")
    if isinstance(error, commands.BadArgument):
        await ctx.send("Số cổ phiếu bạn muốn bán chỉ có thể là số nguyên")

class ConfirmGive(discord.ui.View):
    def __init__(self, sender, receiver, amount, data):
        super().__init__(timeout=60)
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.data = data

    @discord.ui.button(label="Tôi chắc chắn", style=discord.ButtonStyle.danger)
    async def confirm_button(self, interaction: discord.Interaction, button: discord.ui.Button):

        if interaction.user != self.sender:
            await interaction.response.send_message(
                "Có ai hỏi bạn đâu ? 💔",
                ephemeral=True
            )
            return

        self.data[str(self.sender.id)]["cash"] -= self.amount
        self.data[str(self.receiver.id)]["cash"] += self.amount
        embed= discord.Embed(
            title= f"Bạn đã tặng **{self.amount}** Hcoin cho **{self.receiver.name}** <:ngau:1474753850312491169>",
            color= 0x38EBE2
        )
        embed.set_image(url= "https://cdn.discordapp.com/attachments/1439931543710597201/1474689758352638094/download.gif?ex=699ac35c&is=699971dc&hm=c94fd186a7ec1c155ef6f49eedffd531244e471287f16fd048377f548f149589")
        await interaction.response.edit_message(
            embed=embed,
            view=None
        )
        luu_data(self.data)
    @discord.ui.button(label= "Tôi từ chối", style= discord.ButtonStyle.secondary)
    async def tuchoi_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user != self.sender:
            await interaction.response.send_message("Có ai hỏi bạn đâu ? 💔", ephemeral=True)
            return
        await interaction.response.edit_message(content= f"Bạn đã từ chối tặng **{self.amount}** Hcoin cho **{self.receiver.name}**", view= None)
@bot.command()
async def give(ctx, member: discord.Member, amount: int):

    data = mc_data()

    sender_id = str(ctx.author.id)
    receiver_id = str(member.id)
    if ctx.author.id == member.id:
        embed= discord.Embed(
            title= "Bạn không thể tự tặng chính mình",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        return
    if amount < 0:
        embed= discord.Embed(
            title= f"Bạn định tặng {member.name} bao nhiêu Hcoin vậy trời ? 💔",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
        return
    if amount == 0:
        embed= discord.Embed(
            title= "Bạn tặng 0 Hcoin thì tặng làm gì ? 💔",
            color= 0x38EBE2
        )
        await ctx.send(embed=embed)
    if sender_id not in data:
        data[sender_id] = {"cash": 0}

    if receiver_id not in data:
        data[receiver_id] = {"cash": 0}

    if data[sender_id]["cash"] < amount:
        embed= discord.Embed(
            title= f"Bạn không có đủ {amount} Hcoin để tặng {member.name}",
            color= 0x38EBE2
        )
        return

    embed = discord.Embed(
        title="Khoan, hãy nhìn kỹ lại thông tin trước khi tặng Hcoin <a:SirenStickerSirenDescobrireCompa:1474748570648313856>",
        description=(
            f"**Người gửi:** {ctx.author} | **Số định danh:** `{sender_id}`.\n\n"
            f"**Người nhận:** {member.name} | **Số định danh:** `{receiver_id}`.\n\n"
            f"**Số Hcoin:** {amount} Hcoin {emoji_7}.\n\n"
            "`Cái loại không làm mà đòi có ăn thì...` <:anduahau:1474751936388661258>"
        ),
        color=0x38EBE2
    )

    view = ConfirmGive(ctx.author, member, amount, data)
    embed.set_image(url= "https://cdn.discordapp.com/attachments/1439931543710597201/1474747898880200755/download.gif?ex=699af982&is=6999a802&hm=121c1f03df8af9b39bb01eda077d125c48fb1af2f17f7b77ff423b6a0cfa70ff")
    await ctx.send(embed=embed, view=view)

@give.error
async def give_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("**Syntax error**")
    if isinstance(error, commands.BadArgument):
        await ctx.send("**Thành viên không hợp lệ** hoặc số Hcoin **không phải số nguyên**")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def tut(ctx):
    embed = discord.Embed(
        title="<:trading:1474758273558122543> HƯỚNG DẪN ĐẦU TƯ CHỨNG KHOÁN",
        description="Chào mừng bạn đến với hệ thống đầu tư cổ phiếu ảo 💎\nTheo dõi biểu đồ và giao dịch thông minh để kiếm lời!",
        color=0x38EBE2
    )

    embed.add_field(
        name="<:wifi:1463532432459432018> 1. Setup kênh",
        value="`eiusetupchannel <id_channel>`\nThiết lập kênh gửi biểu đồ & thông báo giao dịch (Admin only).",
        inline=False
    )

    embed.add_field(
        name=f"{emoji_7} 2. Xem thông tin cổ phiếu",
        value="`eiucophieu`\nXem giá hiện tại, số dư, số cổ phiếu đang giữ và tổng tài sản.",
        inline=False
    )

    embed.add_field(
        name="<a:thankyou:1456562416497328138> 3. Mua cổ phiếu",
        value="`eiubuy <số_lượng>`\nMua cổ phiếu theo giá hiện tại.\nKhông đủ tiền sẽ không giao dịch được.",
        inline=False
    )

    embed.add_field(
        name="<a:Newkitten:1456562014372626464> 4. Bán cổ phiếu",
        value="`eiusell <số_lượng>`\nBán số cổ phiếu đang giữ.\nKhông thể bán quá số lượng bạn có.",
        inline=False
    )

    embed.add_field(
        name="💡 Mẹo chơi",
        value="• Mua khi giá giảm 📉\n"
              "• Bán khi giá tăng 📈\n"
              "• Theo dõi biểu đồ bot gửi mỗi 3 phút\n"
              "• Đừng all-in khi giá đang pump mạnh <a:SirenStickerSirenDescobrireCompa:1474748570648313856>",
        inline=False
    )

    embed.set_footer(text="💎 Đầu tư thông minh - Không FOMO - Không Cay Cú")
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/3135/3135706.png")

    await ctx.send(embed=embed)
@tut.error
async def tut_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Chờ thêm **{int(error.retry_after)}s** nữa mới dùng lại được")




YDL_OPTIONS: Dict[str, Any] = {
    "format": "bestaudio[abr>=160]/bestaudio/best",
    "quiet": True,
    "noplaylist": True,            
    "default_search": "scsearch",  
    "extractor_retries": 3,
    "no_warnings": True,
    "source_address": "0.0.0.0",
    "cookiefile": None,
    "http_headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Referer": "https://soundcloud.com"
    }
}

FFMPEG_OPTIONS: Dict[str, str] = {
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
    "options": "-vn -ar 48000 -ac 2 -b:a 192k -loglevel panic"
}

async def get_voice_client(ctx):
    """Kết nối voice an toàn, tránh lỗi 4017"""
    channel = ctx.author.voice.channel
    vc = ctx.voice_client

    if vc:
        if vc.is_playing():
            vc.stop()
        
        if vc.channel == channel and vc.is_connected():
            return vc
        
        try:
            await vc.disconnect(force=True)
        except Exception:
            pass
        
        ctx.guild.voice_client._connected.clear()
        await asyncio.sleep(1.5)

    for attempt in range(3):
        try:
            vc = await channel.connect(reconnect=False, timeout=10)
            return vc
        except Exception as e:
            print(f"Lần thử {attempt + 1} thất bại: {e}")
            await asyncio.sleep(2)
    
    return None


@bot.command()
async def play(ctx, url):
    if not ctx.author.voice:
        await ctx.send("Bạn chưa vào voice.")
        return

    vc = await get_voice_client(ctx)
    
    if not vc:
        await ctx.send("Không thể kết nối voice sau 3 lần thử")
        return

    try:
        with yt_dlp.YoutubeDL(cast(Any, YDL_OPTIONS)) as ydl:
            info = cast(Dict[str, Any], ydl.extract_info(url, download=False))

            if "entries" in info:
                entries = info.get("entries") or []
                first_entry = next((entry for entry in entries if isinstance(entry, dict)), None)
                if first_entry is None:
                    raise ValueError("Không tìm thấy bài phù hợp")
                info = first_entry

            url2 = info.get("url")
            title = info.get("title", "Không rõ tiêu đề")

        if not isinstance(url2, str) or not url2:
            raise ValueError("Không lấy được đường dẫn phát nhạc")
        if not isinstance(title, str):
            title = "Không rõ tiêu đề"

        source = discord.FFmpegPCMAudio(
            url2,
            before_options=FFMPEG_OPTIONS["before_options"],
            options=FFMPEG_OPTIONS["options"]
        )
        vc.play(source)

        await ctx.send(f"<a:BUNNIES_GIF_CUTE_STICKER_livtorr:1478021520554066042> Đang phát: **{title}**")

    except Exception as e:
        await ctx.send(f"Lỗi: {e}")


@bot.command()
async def roidi(ctx):
    if not ctx.voice_client:
        await ctx.send("Bot chưa vào voice.")
        return

    if not ctx.author.voice or ctx.author.voice.channel != ctx.voice_client.channel:
        await ctx.send("Bạn phải ở cùng voice với bot")
        return

    await ctx.voice_client.disconnect()
    await ctx.send("Đã rời voice.")



@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def tinhcong(ctx, luc:float, quangduong:float, alpha:float):
    data= hocvan_data()
    user= str(ctx.author.id)
    if user not in data:
        data[user] = {}
    
    trinh= data[user].get("hocvan", 0)
    w= luc * quangduong * math.cos(alpha)
    data[user]["hocvan"] = trinh + 1
    embed= discord.Embed(
        title= f"Tính Công, lực F= {luc}, quãng đường S= {quangduong}, góc alpha= {alpha}",
        description=(
            f"W= {w} (J)"
        ),
        color= 0x38EBE2
    )
    embed.set_footer(text= "Công thức tính: W = F * S * Cos(alpha)")
    await ctx.send(content= "Bạn vừa tính được Công:))), bạn nhận được **01** trình độ học vấn", embed=embed)
    luu_dulieu(data)
@tinhcong.error
async def tinhcong_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Chờ thêm **{int(error.retry_after)}s** nữa mới dùng lại được")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Thiếu số nhập vào")
    if isinstance(error, commands.BadArgument):
        await ctx.send("Lỗi có pháp.\n cú pháp đúng: `eiutinhcong <lực F> <quãng đường> <góc alpha>`")
@bot.command()
@commands.has_permissions(moderate_members=True)
async def mute(ctx, member: discord.Member, minutes: int = 10, *, reason="Không có lý do"):
    if member.top_role >= ctx.author.top_role:
        return await ctx.send("Bạn không thể mute người có role cao hơn hoặc bằng bạn!")

    from datetime import timedelta
    duration = timedelta(minutes=minutes)
    await member.timeout(duration, reason=reason)

    embed = discord.Embed(
        title= "Thành viên bị Mute",
        color= 0x38EBE2,
        timestamp=datetime.utcnow()
    )
    embed.add_field(name="Thành viên", value=member.mention, inline=True)
    embed.add_field(name="Thời gian", value=f"{minutes} phút", inline=True)
    embed.add_field(name="Lý do", value=reason, inline=False)
    embed.add_field(name="Thực hiện bởi", value=ctx.author.mention, inline=False)
    await ctx.send(embed=embed)



chiakhoa= "36d087a453d348c6a2707b6404423525"
NEWS_API_URL = "https://newsapi.org/v2/everything"
TOP_HEADLINES_URL = "https://newsapi.org/v2/top-headlines"

async def fetch_news(url: str, params: dict) -> list:
    """Gọi NewsAPI và trả về danh sách bài báo."""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params, timeout=aiohttp.ClientTimeout(total=10)) as resp:
                if resp.status != 200:
                    return []
                data = await resp.json()
                articles = data.get("articles", [])
                return [a for a in articles if a.get("title") and "[Removed]" not in a["title"]]
    except Exception as e:
        print(f"[Lỗi fetch_news] {e}")
        return []

def build_news_embed(articles: list, title: str, color: int) -> discord.Embed:
    """Tạo Discord Embed đẹp từ danh sách bài báo."""
    embed = discord.Embed(title=title, color=color, timestamp=datetime.utcnow())
    for i, article in enumerate(articles[:5], start=1):
        headline = article.get("title", "Không có tiêu đề")
        url = article.get("url", "")
        source = article.get("source", {}).get("name", "Không rõ nguồn")
        description = article.get("description") or ""
        published = article.get("publishedAt", "")[:10]
        if len(description) > 120:
            description = description[:120] + "..."
        value = f"📌 *{description}*\n🏢 `{source}` · 📅 `{published}`\n🔗 [Đọc thêm]({url})"
        embed.add_field(name=f"{i}. {headline}", value=value, inline=False)
    embed.set_footer(text="Tin nóng hổi vừa thổi vừa ăn")
    return embed

@bot.command()
async def news(ctx, * , word: str):
    params = {
        "q": word,
        "language": "vi",         
        "sortBy": "publishedAt",
        "pageSize": 5,
        "apiKey": chiakhoa
    }

    articles = await fetch_news(NEWS_API_URL, params)

    if not articles:
        params["language"] = "en"
        articles = await fetch_news(NEWS_API_URL, params)
    if not articles:
        await ctx.send(f"Không tìm thấy tin tức về **{word}**")
        return

    embed = build_news_embed(articles, title=f"📰 Tin tức: {word}", color=0x38EBE2)
    await ctx.send(embed=embed)

@news.error
async def news_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Bạn muốn xem tin tức về vấn đề gì ?")







SHOP_DATA = {
    "10A": {
        "title": "🍵 Trà Quán 10A",
        "description": "Chào mừng bạn đến với Trà Quán 10A!\nThư giãn và thưởng thức những ly trà thơm ngon nhất hội trợ hè!",
        "color": 0x38EBE2,
        "items": [
            {"name": "🧋 Trà Sữa Trân Châu",       "desc": "Béo ngậy, thơm lừng",                  "price": 60},
            {"name": "🍵 Trà Xanh Matcha",           "desc": "Thanh mát, nhẹ nhàng",                 "price": 50},
            {"name": "🥤 Trà Đào Cam Sả",            "desc": "Chua ngọt, giải nhiệt",                "price": 40},
            {"name": "🧊 Trà Sữa Kem Cheese",        "desc": "Béo thơm, hot nhất quán",              "price": 65},
            {"name": "🫖 Trà Ô Long Sữa Tươi",       "desc": "Thanh dịu, thơm hậu vị",              "price": 55},
            {"name": "🍓 Trà Dâu Kem Tươi",          "desc": "Đỏ tươi, ngọt chua, sống ảo max",     "price": 70},
            {"name": "🍋 Trà Chanh Sả Gừng",         "desc": "Ấm bụng, cay nhẹ, tỉnh người",        "price": 38},
            {"name": "🌸 Trà Hoa Đậu Biếc",          "desc": "Đổi màu huyền ảo, uống là mê",        "price": 60},
            {"name": "🧉 Trà Sencha Nhật",            "desc": "Thanh tao, hậu ngọt, sang xịn",       "price": 80},
            {"name": "🍯 Trà Mật Ong Chanh Leo",      "desc": "Ngọt thơm, vitamin C dồi dào",        "price": 48},
            {"name": "🫐 Trà Việt Quất Lạnh",         "desc": "Tím đẹp, chua dịu, chill max",        "price": 58},
        ]
    },
    "10B": {
        "title": "🍽️ Gian Hàng 10B",
        "description": "Chào mừng bạn đến với Gian Hàng 10B!\nĐủ món ngon, đủ vị — một chuyến ghé là không muốn về!",
        "color": 0xF4A261,
        "items": [
            {"name": "🥪 Bánh Mì Que Phô Mai",       "desc": "Giòn rụm, kéo sợi cực đã",            "price": 40},
            {"name": "🍟 Khoai Tây Chiên",            "desc": "Vàng ươm, chấm tương ớt",             "price": 35},
            {"name": "🧆 Chả Giò Chiên",              "desc": "Giòn tan, nhân thập cẩm",             "price": 45},
            {"name": "🥤 Nước Chanh Muối",            "desc": "Mát lạnh, đã khát",                   "price": 30},
            {"name": "🌮 Bánh Tráng Cuộn Bò",         "desc": "Cuộn tay, thịt bò tươi, chấm mắm",   "price": 55},
            {"name": "🍗 Cánh Gà Chiên Mắm Tỏi",     "desc": "Ngọt đậm, ăn hoài không ngán",        "price": 65},
            {"name": "🥚 Trứng Cuộn Nhân Phô Mai",    "desc": "Mềm thơm, kéo sợi, ăn là ghiền",     "price": 50},
            {"name": "🌭 Xúc Xích Chiên Bơ",          "desc": "Giòn bên ngoài, mọng bên trong",      "price": 42},
            {"name": "🧅 Hành Chiên Giòn Mix",        "desc": "Giòn rụm, chấm sốt mayo",             "price": 38},
            {"name": "🍱 Cơm Cuộn Nhân Cá",           "desc": "Nhỏ gọn, ngon miệng, no căng",        "price": 60},
            {"name": "🥜 Đậu Phộng Rang Muối Ớt",     "desc": "Cay nhẹ, giòn tan, nhâm nhi cực đã", "price": 32},
        ]
    },
    "10C": {
        "title": "🍢 Xiên Bẩn 10C",
        "description": "Chào mừng bạn đến với Xiên Bẩn 10C!\nĂn là ghiền, ghiền là quay lại — xiên bẩn đỉnh nhất hội trợ!",
        "color": 0xE63946,
        "items": [
            {"name": "🍢 Xiên Bẩn Sốt Đặc Biệt",    "desc": "Cay xé lưỡi, nghiện không lối thoát", "price": 40},
            {"name": "🌭 Xúc Xích Nướng Than",        "desc": "Thơm lừng, ăn hoài không chán",       "price": 35},
            {"name": "🧅 Bánh Tráng Nướng Topping",   "desc": "Giòn rụm, topping đầy ắp",            "price": 48},
            {"name": "🌶️ Bò Viên Xiên Que",           "desc": "Dai dai, cay cay, đậm đà",            "price": 42},
            {"name": "🦑 Mực Viên Sốt Chua Ngọt",     "desc": "Thơm biển, sốt đỏ au, đỉnh vị",      "price": 55},
            {"name": "🐟 Cá Viên Chiên Sa Tế",        "desc": "Vàng giòn, cay thơm, ăn là no",      "price": 45},
            {"name": "🧀 Phô Mai Que Bột Chiên",       "desc": "Kéo sợi cực đã, béo thơm không cưỡng","price": 50},
            {"name": "🌽 Bắp Nướng Bơ Muối",          "desc": "Ngọt tự nhiên, thơm béo, đỉnh cao",  "price": 38},
            {"name": "🥔 Khoai Lang Xiên Nướng",       "desc": "Ngọt bùi, thơm dẻo, healthy vibe",   "price": 35},
            {"name": "🍄 Nấm Đùi Gà Nướng Tỏi",       "desc": "Thơm ngậy, dai giòn, ăn là ghiền",   "price": 45},
            {"name": "🌶️ Sốt Chấm Đặc Biệt 10C",      "desc": "Bí quyết riêng, cay ngọt đậm đà",    "price": 30},
        ]
    },
    "10D": {
        "title": "🏙️ Land Mark 10D",
        "description": "Chào mừng bạn đến với Land Mark 10D!\nCao sang, đẳng cấp — trải nghiệm hội trợ theo một cách khác biệt!",
        "color": 0x6A4C93,
        "items": [
            {"name": "🍰 Bánh Crepe Nhân Kem",        "desc": "Mỏng mịn, ngọt ngào như mùa hè",      "price": 60},
            {"name": "☕ Cà Phê Dalgona",              "desc": "Trendy, đắng nhẹ, thơm lừng",         "price": 55},
            {"name": "🧁 Cupcake Trang Trí",           "desc": "Xinh xắn, ngọt ngào, sống ảo đỉnh",  "price": 75},
            {"name": "🥛 Sữa Tươi Trân Châu",          "desc": "Thanh mát, beo béo",                  "price": 48},
            {"name": "🍮 Panna Cotta Vani",            "desc": "Mịn như lụa, ngọt thanh, sang xịn",  "price": 80},
            {"name": "🫧 Soda Kem Cao Cấp",            "desc": "Bọt mịn, kem tan chậm, đẳng cấp",    "price": 65},
            {"name": "🍩 Donut Glazed Socola",         "desc": "Tròn đều, phủ socola bóng mịn",       "price": 55},
            {"name": "🥐 Croissant Bơ Pháp",           "desc": "Lớp vỏ giòn, nhân bơ tan chảy",      "price": 70},
            {"name": "🍓 Tart Dâu Kem Tươi",           "desc": "Đế giòn, kem mịn, dâu đỏ tươi",      "price": 90},
            {"name": "🍵 Matcha Latte Artwork",         "desc": "Latte art đỉnh, vừa đẹp vừa ngon",   "price": 85},
            {"name": "🎁 Gift Box Combo Land Mark",    "desc": "Hộp quà đặc biệt từ 10D",             "price": 150},
        ]
    },
    "10E": {
        "title": "🎭 Sân Khấu 10E",
        "description": "Chào mừng bạn đến với Sân Khấu 10E!\nKhông chỉ xem — bạn còn được ăn uống thả ga ngay tại đây!",
        "color": 0xFFB703,
        "items": [
            {"name": "🍿 Bắp Rang Bơ Caramel",        "desc": "Xem show mà thiếu bắp là thiếu vibe", "price": 35},
            {"name": "🧃 Nước Ép Trái Cây Mix",        "desc": "Tươi mát, đủ loại trái cây mùa hè",  "price": 42},
            {"name": "🍭 Kẹo Bông Gòn Màu",           "desc": "Ngọt như những tràng vỗ tay",         "price": 30},
            {"name": "🥨 Bánh Snack Mix Hộp",          "desc": "Nhâm nhi xem show, đỉnh của chóp",   "price": 38},
            {"name": "🌮 Nachos Sốt Cheese",           "desc": "Giòn rụm, sốt phô mai béo ngậy",     "price": 55},
            {"name": "🍔 Mini Burger Sân Khấu",        "desc": "Nhỏ gọn, đủ nhân, ăn không rơi",     "price": 70},
            {"name": "🧋 Trà Sữa Xem Show",            "desc": "Kích thước lớn, uống suốt cả show",  "price": 60},
            {"name": "🍕 Pizza Cắt Miếng",             "desc": "Giòn đế, đầy topping, kéo sợi đã",   "price": 65},
            {"name": "🎪 Combo Xem Show VIP",          "desc": "Bắp + Trà sữa + Snack, ngồi VIP",    "price": 130},
            {"name": "🍦 Kem Que Biểu Diễn",           "desc": "Ăn kem xem show — định nghĩa mùa hè","price": 45},
            {"name": "🥤 Slushie Màu Sắc",             "desc": "Lạnh ngọt, màu đẹp, sống ảo đỉnh",  "price": 50},
        ]
    },
    "10G": {
        "title": "🎨 Góc Nghệ 10G",
        "description": "Chào mừng bạn đến với Góc Nghệ 10G!\nSáng tạo, nghệ thuật và... cực kỳ ngon miệng!",
        "color": 0xE9C46A,
        "items": [
            {"name": "🎂 Bánh Vẽ Trang Trí",          "desc": "Vừa đẹp vừa ngon, sống ảo ngay",      "price": 100},
            {"name": "🍡 Chè Thái Sắc Màu",            "desc": "Nhiều màu, nhiều topping, nhiều vui", "price": 55},
            {"name": "🖌️ Trà Hoa Đậu Biếc",            "desc": "Đổi màu huyền ảo, uống là mê",        "price": 58},
            {"name": "🍩 Donut Phủ Socola Nghệ Thuật", "desc": "Trang trí độc đáo, đẹp không nỡ ăn", "price": 65},
            {"name": "🧁 Cupcake Vẽ Tay",              "desc": "Từng chiếc là một tác phẩm",          "price": 80},
            {"name": "🌈 Rainbow Cake Slice",           "desc": "7 màu cầu vồng, ngọt như ước mơ",    "price": 90},
            {"name": "🫧 Drink Galaxy Swirl",           "desc": "Xoáy màu thiên hà, uống là ảo",      "price": 70},
            {"name": "🍰 Tiramisu Cốc",                 "desc": "Đắng nhẹ cà phê, ngọt kem, sang xịn","price": 75},
            {"name": "🖼️ Cookie Hình In",               "desc": "In hình theo yêu cầu, độc nhất",     "price": 120},
            {"name": "🎨 Combo Nghệ Sĩ",               "desc": "Bánh + Trà + Cookie hình — full art",  "price": 180},
            {"name": "✏️ Bookmark Handmade",            "desc": "Tặng kèm mỗi đơn — kỷ niệm đẹp",    "price": 30},
        ]
    },
    "10H": {
        "title": "😎 Chill Zone 10H",
        "description": "Chào mừng bạn đến với Chill Zone 10H!\nCứ thư giãn đi — ở đây lo hết từ đồ ăn đến vibe!",
        "color": 0x48CAE4,
        "items": [
            {"name": "🥤 Sinh Tố Bơ",                 "desc": "Béo mịn, chill không kém gì 10H",     "price": 55},
            {"name": "🧊 Đá Xay Chanh Leo",            "desc": "Chua ngọt, mát lạnh, giải nhiệt max", "price": 45},
            {"name": "🍦 Kem Cuộn Thái",               "desc": "Mát lạnh, toppings chất, sống ảo",    "price": 65},
            {"name": "🫧 Soda Kem Muối",               "desc": "Lạ miệng, hợp trend, uống là ghiền",  "price": 48},
            {"name": "🧴 Smoothie Bowl",               "desc": "Healthy, đẹp mắt, topping đầy",       "price": 80},
            {"name": "🎵 Chill Playlist + Nước",       "desc": "Nước uống + mã playlist chill 10H",   "price": 70},
            {"name": "🍧 Đá Bào Nhật Kakigori",        "desc": "Mịn như tuyết, đủ vị, mát cực đỉnh", "price": 60},
            {"name": "🥭 Mango Slushy",                "desc": "Xoài chín, ngọt thơm, mát cả người",  "price": 50},
            {"name": "🫐 Acai Bowl Mini",              "desc": "Trendy, healthy, ăn là thấy sang",    "price": 85},
            {"name": "😎 Chill Combo",                 "desc": "Sinh tố + Kem cuộn + Snack nhẹ",      "price": 140},
            {"name": "🌊 Blue Ocean Soda",             "desc": "Xanh như biển, mát như gió hè",       "price": 52},
        ]
    },
    "11A": {
        "title": "🍱 Buffet Hè 11A",
        "description": "Chào mừng bạn đến với Buffet Hè 11A!\nNo căng, vui hết nấc — một mình đi cũng không thấy cô đơn!",
        "color": 0x2DC653,
        "items": [
            {"name": "🍱 Cơm Hộp Thập Cẩm",           "desc": "Đủ món, no lâu, xứng đáng đồng Hcoin", "price": 80},
            {"name": "🥗 Salad Trộn Sốt Mè",          "desc": "Thanh nhẹ, healthy, ăn không lo béo", "price": 55},
            {"name": "🍜 Mì Trộn Hàn Quốc",           "desc": "Dai, cay, đậm đà, ăn hoài không ngán","price": 65},
            {"name": "🧋 Trà Sữa Tặng Kèm",           "desc": "FREE khi mua combo — 11A chơi lớn!",  "price": 0},  # free
            {"name": "🍣 Cơm Cuộn Cá Hồi",            "desc": "Tươi ngon, cuộn đều, sang như nhà hàng","price": 90},
            {"name": "🥘 Súp Bí Đỏ Kem",              "desc": "Béo ngậy, ấm bụng, ủi mà ngon",      "price": 50},
            {"name": "🥙 Wrap Gà Nướng",               "desc": "Bánh mì cuộn, gà thơm, rau tươi",    "price": 70},
            {"name": "🍛 Cơm Chiên Kimchi",            "desc": "Cay thơm, đậm đà, no căng",          "price": 72},
            {"name": "🍝 Mì Ý Sốt Cà",                "desc": "Sốt đặc, thơm lừng, no dài",         "price": 75},
            {"name": "🧆 Falafel Chấm Hummus",         "desc": "Lạ miệng, healthy, trendy vibe",      "price": 65},
            {"name": "👑 Buffet Combo VIP",             "desc": "Cơm + Salad + Mì + Trà sữa full set","price": 200},
        ]
    },
    "11B": {
        "title": "🍺 Quán Nhậu 11B",
        "description": "Chào mừng bạn đến với Quán Nhậu 11B!\nDzô dzô — mùa hè không say không về (say vui thôi nha 😂)!",
        "color": 0xFB8500,
        "items": [
            {"name": "🍗 Gà Rán Cay Hàn",             "desc": "Cay giòn, ăn kèm bia bắp cực đỉnh",  "price": 75},
            {"name": "🌽 Bắp Nướng Phô Mai",           "desc": "Béo thơm, ngọt tự nhiên",            "price": 42},
            {"name": "🥜 Đậu Phộng Rang Muối",         "desc": "Nhâm nhi, tâm sự, quên cả về nhà",   "price": 32},
            {"name": "🥤 Bia Bắp Homemade",            "desc": "Giải khát số 1 — không cồn thả ga",  "price": 45},
            {"name": "🦐 Tôm Nướng Muối Ớt",          "desc": "Lột vỏ ăn ngay, cay thơm, tươi ngon","price": 90},
            {"name": "🥩 Sườn Nướng BBQ",              "desc": "Thịt mềm, sốt ngấm, gặm hoài không chán","price": 110},
            {"name": "🍖 Chân Gà Nướng Sả",           "desc": "Da giòn, thịt dai, thơm lừng sả ớt", "price": 55},
            {"name": "🌮 Bánh Tráng Thịt Nướng",       "desc": "Cuộn rau, chấm mắm, ngon hết sảy",   "price": 60},
            {"name": "🧅 Hành Tây Chiên Giòn",         "desc": "Vàng giòn, chấm sốt, nhâm nhi đỉnh", "price": 38},
            {"name": "🍻 Party Combo 11B",             "desc": "Gà + Tôm + Sườn + 2 Bia bắp",        "price": 200},
            {"name": "🥗 Gỏi Xoài Tôm",               "desc": "Chua cay ngọt, ăn kèm nhậu cực hợp", "price": 65},
        ]
    },
    "11C": {
        "title": "☕ Café Sân Vườn 11C",
        "description": "Chào mừng bạn đến với Café Sân Vườn 11C!\nNgồi lai rai, tám chuyện, tận hưởng mùa hè thật thư thái!",
        "color": 0x6B4226,
        "items": [
            {"name": "☕ Cà Phê Sữa Đá",              "desc": "Đắng nhẹ, béo thơm, tỉnh ngủ nhanh",  "price": 42},
            {"name": "🌿 Bạc Hà Chanh Đá",            "desc": "Mát lạnh, thanh mát như gió sân vườn","price": 38},
            {"name": "🧇 Bánh Waffle Mật Ong",         "desc": "Giòn ngoài mềm trong, ăn kèm cà phê", "price": 60},
            {"name": "🫖 Trà Hoa Cúc Mật Ong",         "desc": "Ngọt dịu, thơm nhẹ, bình yên",        "price": 48},
            {"name": "🍰 Bánh Cheesecake Cốc",         "desc": "Mịn béo, ngọt nhẹ, tan trên đầu lưỡi","price": 70},
            {"name": "🥐 Croissant Mứt Dâu",           "desc": "Giòn bơ pháp, mứt chua ngọt",        "price": 58},
            {"name": "🧋 Cold Brew Sữa Yến Mạch",      "desc": "Healthy trend, đắng dịu, sang xịn",  "price": 72},
            {"name": "🍮 Bánh Flan Caramel",           "desc": "Mềm mịn, caramel đắng nhẹ, đỉnh",    "price": 50},
            {"name": "🌸 Latte Hoa Hồng",              "desc": "Thơm hoa hồng, đẹp như tranh vẽ",    "price": 68},
            {"name": "🎋 Matcha Honey Latte",          "desc": "Matcha đắng, mật ngọt, cân bằng hoàn hảo","price": 75},
            {"name": "☕ Café Combo Đôi",              "desc": "2 ly cà phê + 2 bánh — hẹn hò chill", "price": 160},
        ]
    },
    "11D": {
        "title": "🚚 Food Truck 11D",
        "description": "Chào mừng bạn đến với Food Truck 11D!\nBánh mì, nước uống, full combo — đỉnh của hội trợ!",
        "color": 0xFF6B35,
        "items": [
            {"name": "🥖 Bánh Mì Pate Đặc Biệt",      "desc": "Nhân đầy ắp, giòn rụm, ăn là no",    "price": 48},
            {"name": "🌮 Bánh Tráng Cuộn Thịt",        "desc": "Cuộn tay, chấm mắm, ngon hết sảy",   "price": 55},
            {"name": "🥤 Nước Mía Ép Tươi",            "desc": "Ngọt thanh, mát lạnh, giải nhiệt",    "price": 35},
            {"name": "🍡 Chả Cá Chiên Giòn",           "desc": "Giòn ngoài, dai trong, chấm tương",  "price": 42},
            {"name": "🥙 Bánh Mì Gà Nướng",            "desc": "Gà thơm, rau tươi, sốt đặc biệt",    "price": 58},
            {"name": "🌯 Bánh Mì Xúc Xích Bơ",        "desc": "Giòn bơ, xúc xích chiên vàng",       "price": 52},
            {"name": "🍟 Khoai Tây Chiên Đặc Biệt",   "desc": "Giòn lâu, sốt Food Truck riêng",      "price": 45},
            {"name": "🧆 Há Cảo Chiên Giòn",           "desc": "Vỏ giòn, nhân tươi, chấm sốt chua",  "price": 50},
            {"name": "🥜 Bánh Mì Phô Mai Bơ Tỏi",     "desc": "Nướng thơm, bơ tỏi ngấm vào từng thớ","price": 45},
            {"name": "🚚 Street Food Combo",           "desc": "Bánh mì + Khoai tây + Nước mía",      "price": 120},
            {"name": "🌶️ Bánh Tráng Nướng Đầy Topping","desc": "Topping đến đâu hết đến đó",          "price": 60},
        ]
    },
    "11E": {
        "title": "🌙 Phố Đêm 11E",
        "description": "Chào mừng bạn đến với Phố Đêm 11E!\nKhông khí chợ đêm sôi động — ăn đã, chơi đã, vui đã!",
        "color": 0x1B1B2F,
        "items": [
            {"name": "🦑 Mực Nướng Sa Tế",            "desc": "Thơm lừng, cay nồng, không dừng được","price": 75},
            {"name": "🍢 Tteokbokki Sốt Đỏ",          "desc": "Dai mềm, cay ngọt, hot trend",        "price": 60},
            {"name": "🌯 Bánh Tráng Nướng Pate",       "desc": "Giòn rụm, thơm mùi than nướng",       "price": 45},
            {"name": "🧃 Nước Chanh Sả Gừng",         "desc": "Cay nhẹ, ấm bụng, uống là tỉnh",      "price": 38},
            {"name": "🍖 Chân Gà Sốt Tắc",            "desc": "Da dai, sốt chua ngọt cay, ghiền",    "price": 55},
            {"name": "🔮 Takoyaki Bạch Tuộc",          "desc": "Tròn giòn, nhân bạch tuộc, sốt Nhật", "price": 68},
            {"name": "🌮 Bánh Mì Nướng Than Hoa",     "desc": "Than hoa thơm ngào ngạt, giòn tan",   "price": 50},
            {"name": "🍜 Bún Bò Cay Mini",             "desc": "Cay thơm, nước dùng đậm đà",          "price": 65},
            {"name": "🥟 Há Cảo Hấp Sốt Gừng",        "desc": "Mỏng mịn, nhân tươi, chấm gừng",     "price": 55},
            {"name": "🌙 Night Market Combo",          "desc": "Mực + Tteokbokki + Nước — đêm phố",  "price": 160},
            {"name": "🔥 Phô Mai Que Nướng Than",      "desc": "Kéo sợi ngay trên lửa, nóng hổi",    "price": 52},
        ]
    },
    "11G": {
        "title": "🌶️ Mì Cay 11G",
        "description": "Chào mừng bạn đến với Mì Cay 11G!\nThách thức vị giác — bạn dám thử không? 🔥",
        "color": 0xD62828,
        "items": [
            {"name": "🍜 Mì Cay Cấp 1",               "desc": "Cay nhẹ, ai cũng ăn được",            "price": 50},
            {"name": "🍜 Mì Cay Cấp 3",               "desc": "Cay vừa, bắt đầu chảy nước mắt",      "price": 62},
            {"name": "🍜 Mì Cay Cấp 5",               "desc": "Cay xé lưỡi — không phải ai cũng dám","price": 75},
            {"name": "🥛 Sữa Tươi Giải Cay",           "desc": "Cứu tinh số 1 sau mì cay",            "price": 35},
            {"name": "🍜 Mì Cay Hải Sản",              "desc": "Tôm mực tươi + cay = đỉnh nóc",      "price": 90},
            {"name": "🍜 Mì Cay Phô Mai",              "desc": "Cay rồi lại béo — combo điên rồ",     "price": 80},
            {"name": "🌶️ Nước Sốt Cay Special",       "desc": "Mang về dùng — bí quyết của 11G",     "price": 45},
            {"name": "🥚 Trứng Onsen Thêm Vào",        "desc": "Lòng đào béo ngậy, giảm cay tuyệt",  "price": 30},
            {"name": "🍜 Mì Cay Cấp 7 (Extreme)",     "desc": "⚠️ Cảnh báo: cực cay — ký tên trước", "price": 100},
            {"name": "🏆 Challenge Combo Cấp 5+",      "desc": "Mì cay cấp 5 + Sữa + Khăn lạnh",     "price": 130},
            {"name": "🌶️ Ớt Trái Thêm Phần",          "desc": "Thêm cay cho những ai chưa đủ",       "price": 30},
        ]
    },
    "11H": {
        "title": "🏮 Hội Quán 11H",
        "description": "Chào mừng bạn đến với Hội Quán 11H!\nTụ tập, vui chơi, ăn uống thả ga — ghé một lần là muốn ở lại mãi!",
        "color": 0xC77DFF,
        "items": [
            {"name": "🍲 Lẩu Mini 2 Người",            "desc": "Nóng hổi, đủ topping, ăn cùng bạn bè","price": 140},
            {"name": "🥟 Há Cảo Hấp",                  "desc": "Mỏng mịn, nhân tươi, chấm tương",    "price": 55},
            {"name": "🍮 Bánh Flan Caramel",           "desc": "Mềm mịn, ngọt nhẹ, ăn xong muốn thêm","price": 45},
            {"name": "🫖 Trà Ô Long Sữa",              "desc": "Thơm dịu, béo nhẹ, nhâm nhi hoài",   "price": 52},
            {"name": "🥘 Dim Sum Thập Cẩm",            "desc": "5 loại dim sum, đủ vị, sang như khách sạn","price": 120},
            {"name": "🍜 Mì Vịt Tiềm",                 "desc": "Nước dùng ngọt thanh, vịt mềm",      "price": 85},
            {"name": "🧆 Chả Hành Chiên",              "desc": "Giòn thơm, nhân hành béo ngậy",       "price": 48},
            {"name": "🫕 Cháo Sườn Hoa Tiêu",          "desc": "Nóng ấm, thơm tiêu, ăn là no",       "price": 60},
            {"name": "🎎 Hội Quán Combo",              "desc": "Lẩu mini + Dim sum + Trà ô long",     "price": 200},
            {"name": "🥐 Bánh Bao Nhân Thịt",          "desc": "Mềm bông, nhân đầy, ăn là ấm lòng",  "price": 42},
            {"name": "🍡 Chè Ba Màu",                  "desc": "Ngọt mát, đủ topping, giải nhiệt",    "price": 40},
        ]
    },
    "12A": {
        "title": "🌅 Hoàng Hôn 12A",
        "description": "Chào mừng bạn đến với Hoàng Hôn 12A!\nMùa hè cuối cấp — hãy để 12A giúp bạn lưu trọn khoảnh khắc đẹp nhất!",
        "color": 0xFF9F1C,
        "items": [
            {"name": "📸 Góc Chụp Ảnh Kỷ Niệm",       "desc": "Lưu lại mùa hè cuối cấp đáng nhớ",   "price": 60},
            {"name": "🍹 Mocktail Hoàng Hôn",          "desc": "Đỏ rực, đẹp mắt, cảm xúc dâng trào", "price": 65},
            {"name": "🧁 Bánh Tart Trứng",              "desc": "Vàng ươm, thơm bơ, ngọt ngào",       "price": 52},
            {"name": "🫐 Sinh Tố Việt Quất",            "desc": "Tím đẹp như hoàng hôn, ngon như ký ức","price": 58},
            {"name": "🌅 Sunset Ombre Drink",           "desc": "Gradient màu hoàng hôn, uống đẹp lắm","price": 72},
            {"name": "🍰 Bánh Mousse Chanh Leo",        "desc": "Chua nhẹ, mịn như tơ, ngọt hậu",    "price": 80},
            {"name": "📷 Polaroid + Đồ Uống",           "desc": "In ảnh kỷ niệm kèm ly mocktail",     "price": 110},
            {"name": "🌸 Nước Hoa Quả Tươi Ép",        "desc": "Tươi ngon, đủ vitamin, healthy",      "price": 48},
            {"name": "🎑 Combo Hoàng Hôn Đôi",         "desc": "2 mocktail + 2 tart + 2 polaroid",    "price": 180},
            {"name": "🫶 Ly Đôi Kỷ Niệm",              "desc": "In tên lên ly — lưu giữ mãi mãi",    "price": 90},
            {"name": "🌻 Trà Hoa Nhài Lạnh",           "desc": "Thơm thanh, dịu nhẹ, nhẹ như gió hè","price": 45},
        ]
    },
    "12B": {
        "title": "📔 Ký Ức Hè 12B",
        "description": "Chào mừng bạn đến với Ký Ức Hè 12B!\nGhé đây để lưu lại những kỷ niệm đẹp nhất trước khi chia tay!",
        "color": 0xF72585,
        "items": [
            {"name": "🎞️ Ảnh Polaroid In Liền",        "desc": "In ngay kỷ niệm hội trợ, mang về",   "price": 80},
            {"name": "🍰 Bánh Bông Lan Cuộn",           "desc": "Mềm mịn, ngọt thanh, kỷ niệm đẹp",  "price": 58},
            {"name": "🧋 Trà Sữa Kẻ Sọc",              "desc": "Hai màu, hai vị, một kỷ niệm",        "price": 62},
            {"name": "🍬 Kẹo Ký Ức",                   "desc": "Đủ loại kẹo tuổi thơ — nhớ ngay hồi bé","price": 35},
            {"name": "📓 Sổ Tay Kỷ Niệm",              "desc": "Ghi lại những điều đáng nhớ",         "price": 90},
            {"name": "🎁 Hộp Quà Lưu Niệm",            "desc": "Đầy ắp kỷ niệm từ 12B",              "price": 150},
            {"name": "🍩 Donut Phủ Kem Tươi",           "desc": "Tròn đều, ngọt ngào, đẹp như kỷ niệm","price": 65},
            {"name": "🫖 Trà Hoa Đặc Biệt 12B",        "desc": "Blend riêng, thơm lừng, nhớ mãi",    "price": 55},
            {"name": "📸 Combo Lưu Ký Ức",             "desc": "Polaroid + Sổ tay + Trà + Bánh",      "price": 200},
            {"name": "✉️ Bưu Thiếp Viết Tay",           "desc": "Gửi lời yêu thương đến bạn bè",      "price": 40},
            {"name": "🎀 Vòng Tay Kết Đôi",            "desc": "Tặng bạn thân — kết nối mãi mãi",    "price": 70},
        ]
    },
    "12C": {
        "title": "🔥 Sunset BBQ 12C",
        "description": "Chào mừng bạn đến với Sunset BBQ 12C!\nNướng cùng 12C, cháy hết mình trước ngày xa trường!",
        "color": 0xE63946,
        "items": [
            {"name": "🥩 Thịt Bò Nướng Lá Lốt",       "desc": "Thơm lừng, cuốn bánh tráng, đỉnh!",  "price": 85},
            {"name": "🍗 Cánh Gà Nướng BBQ",           "desc": "Vàng ươm, sốt đậm, gặm hoài không chán","price": 75},
            {"name": "🌽 Bắp Nướng Bơ Tỏi",           "desc": "Thơm béo, ngọt tự nhiên",             "price": 42},
            {"name": "🥤 Soda Chanh Dây",              "desc": "Chua ngọt, mát lạnh, giải ngán BBQ",  "price": 42},
            {"name": "🦐 Tôm Nướng Muối Ớt",          "desc": "Tươi ngon, bóc vỏ ăn ngay, thơm",    "price": 95},
            {"name": "🍖 Sườn Non Nướng Mật Ong",      "desc": "Mật ong ngấm sâu, thịt mềm, đỉnh",  "price": 120},
            {"name": "🧀 Bánh Mì Bơ Tỏi Phô Mai",     "desc": "Nướng than, kéo sợi, thơm khói",     "price": 55},
            {"name": "🥗 Gỏi Cuốn Bò Nướng",          "desc": "Thanh mát, ăn kèm BBQ cân bằng",     "price": 65},
            {"name": "🍹 BBQ Mocktail Combo",           "desc": "2 Soda + 1 Sườn + 1 Gà — BBQ perfect","price": 175},
            {"name": "🏕️ Sunset Feast Combo",           "desc": "Bò + Tôm + Sườn + Rau nướng + Nước", "price": 200},
            {"name": "🥬 Rau Nướng Hỗn Hợp",          "desc": "Nấm, ớt chuông, zucchini nướng than", "price": 48},
        ]
    },
    "12D": {
        "title": "🛤️ Quán Cuối Đường 12D",
        "description": "Chào mừng bạn đến với Quán Cuối Đường 12D!\nChặng cuối của hành trình — dừng chân ở đây trước khi lên đường nhé!",
        "color": 0x8D99AE,
        "items": [
            {"name": "🍜 Phở Bò Đặc Biệt",            "desc": "Nước dùng ngọt thanh, thịt bò tươi",  "price": 90},
            {"name": "🥐 Bánh Sừng Bò Bơ",            "desc": "Giòn lớp ngoài, mềm bên trong",       "price": 48},
            {"name": "☕ Cà Phê Đen Đá",               "desc": "Đắng đậm, một ngụm tỉnh cả người",   "price": 40},
            {"name": "🍮 Chè Đậu Đỏ Bánh Lọt",        "desc": "Ngọt thanh, mát lạnh, nhớ mãi",       "price": 52},
            {"name": "🍲 Bún Bò Huế Mini",             "desc": "Cay thơm, nước dùng đỏ au, đậm đà",  "price": 80},
            {"name": "🥞 Bánh Pancake Mật Ong",         "desc": "Mềm xốp, thơm bơ, mật ngọt",         "price": 65},
            {"name": "🧋 Cà Phê Trứng",                "desc": "Béo ngậy, thơm trứng, Hà Nội cổ",    "price": 58},
            {"name": "🫕 Súp Lươn Đặc Biệt",           "desc": "Đậm đà, ngọt thịt, ấm bụng",         "price": 75},
            {"name": "🛤️ Combo Lên Đường",             "desc": "Phở + Cà phê + Bánh — sẵn sàng đi xa","price": 160},
            {"name": "🍱 Cơm Tấm Sườn Bì Chả",        "desc": "Đủ bộ, ngon đúng điệu miền Nam",      "price": 85},
            {"name": "🌸 Chè Thái Coconut",             "desc": "Nước cốt dừa béo, topping đầy",       "price": 55},
        ]
    },
    "12E": {
        "title": "💃 Last Dance 12E",
        "description": "Chào mừng bạn đến với Last Dance 12E!\nMột lần nữa thôi — nhảy, ăn, vui hết mình trước khi tốt nghiệp!",
        "color": 0xFF006E,
        "items": [
            {"name": "🧃 Nước Ép Mix Detox",           "desc": "Thanh lọc cơ thể, sẵn sàng bùng cháy","price": 52},
            {"name": "🍓 Bánh Crepe Dâu Tây",          "desc": "Đỏ tươi, chua ngọt, đẹp như 12E",     "price": 65},
            {"name": "🍭 Lollipop Đủ Màu",             "desc": "Ngọt ngào như kỷ niệm sắp qua",       "price": 30},
            {"name": "🥤 Smoothie Xoài Dứa",           "desc": "Nhiệt đới, bùng nổ vị giác",          "price": 58},
            {"name": "💃 Energy Drink Hội Trợ",        "desc": "Tăng lực nhảy — không cồn, đừng lo",  "price": 48},
            {"name": "🎂 Bánh Tiramisu Tốt Nghiệp",    "desc": "Đắng cà phê, ngọt kem, như hành trình","price": 85},
            {"name": "🍩 Donut Rainbow",               "desc": "Màu sắc như tuổi 18, ngọt như ước mơ","price": 68},
            {"name": "🫧 Sparkling Mocktail",          "desc": "Bong bóng lấp lánh, chúc mừng tương lai","price": 62},
            {"name": "💃 Graduation Combo",            "desc": "Smoothie + Crepe + Tiramisu — chia tay", "price": 180},
            {"name": "🎤 Mic Drop Cookie",             "desc": "Cookie hình mic — cho ai cuối cùng",   "price": 55},
            {"name": "🏅 Huy Chương Chocolate",        "desc": "Chocolate hình huy chương tốt nghiệp", "price": 45},
        ]
    },
    "12G": {
        "title": "📖 Chương Cuối 12G",
        "description": "Chào mừng bạn đến với Chương Cuối 12G!\nTrang cuối của cuốn sách học trò — hãy viết tiếp thật đẹp cùng 12G!",
        "color": 0x4A4E69,
        "items": [
            {"name": "📚 Combo Sách + Trà",            "desc": "Ngồi đọc sách, nhâm nhi trà — chill",  "price": 75},
            {"name": "🫖 Trà Thảo Mộc Đặc Biệt",      "desc": "Blend riêng của 12G, nhớ mãi",        "price": 58},
            {"name": "🍪 Bánh Quy Handmade",           "desc": "Tự tay 12G làm — tâm huyết",          "price": 45},
            {"name": "🎁 Bookmark Kỷ Niệm",            "desc": "Lưu lại trang đẹp nhất tuổi học trò", "price": 30},
            {"name": "📖 Truyện Ngắn 12G Tự Viết",    "desc": "Tập truyện do chính 12G sáng tác",     "price": 90},
            {"name": "🖊️ Bút Ký Tên Kỷ Niệm",         "desc": "Ký tên lưu niệm — kết nối mãi mãi",  "price": 50},
            {"name": "🧋 Trà Sữa Chương Cuối",         "desc": "Vị ngọt ngào của trang cuối đẹp nhất","price": 62},
            {"name": "🎨 Postcard Thủ Công",           "desc": "Tự tay 12G vẽ — mỗi tấm là duy nhất", "price": 70},
            {"name": "📔 Nhật Ký Bìa Cứng",            "desc": "Bắt đầu chương mới với cuốn nhật ký", "price": 120},
            {"name": "📖 The Last Chapter Combo",      "desc": "Sách + Trà + Bánh quy + Bookmark",    "price": 180},
            {"name": "🌟 Gói Lưu Niệm Tốt Nghiệp",    "desc": "Hộp kỷ niệm full: sách, bút, bưu thiếp","price": 200},
        ]
    },
    "12H": {
        "title": "🎉 Bữa Tiệc Cuối 12H",
        "description": "Chào mừng bạn đến với Bữa Tiệc Cuối 12H!\nTiệc chia tay đỉnh nhất mùa hè — cùng 12H kết thúc thật rực rỡ!",
        "color": 0xF9C74F,
        "items": [
            {"name": "🎂 Bánh Sinh Nhật Mini",          "desc": "Thổi nến, ước nguyện, ngọt như tuổi 18","price": 100},
            {"name": "🥂 Sparkling Soda Lễ Hội",        "desc": "Bong bóng lấp lánh, chúc mừng tương lai","price": 52},
            {"name": "🍣 Sushi Cuộn Handmade",          "desc": "Cuộn tay, topping đầy, đẹp ngon",    "price": 85},
            {"name": "🎊 Túi Quà Kỷ Niệm",             "desc": "FREE khi mua combo — lưu kỷ niệm",   "price": 0},  # free
            {"name": "🍾 Party Popper Set",             "desc": "Bắn confetti mừng tốt nghiệp",        "price": 60},
            {"name": "🍰 Bánh Cheesecake Tiệc",         "desc": "Slice to share — ngon ngất ngây",     "price": 75},
            {"name": "🎈 Balloon Confetti Cup",         "desc": "Ly bong bóng confetti, sống ảo cực",  "price": 68},
            {"name": "🦞 Tôm Hùm Mini Nướng",          "desc": "Xa hoa, đỉnh nhất hội trợ, 1 lần",    "price": 180},
            {"name": "🍱 Party Bento Box",              "desc": "Hộp cơm tiệc đủ vị, đẹp như tranh",  "price": 90},
            {"name": "🎉 Grand Finale Combo",           "desc": "Bánh sinh nhật + Sushi + Sparkling",  "price": 200},
            {"name": "🌟 VIP Seat + Ưu Tiên Order",    "desc": "Ngồi đầu bàn + order trước mọi người","price": 150},
        ]
    },
}

EVENT_PRICE_MULTIPLIER = 2


def event_effective_price(item: dict) -> int:
    base = int(item.get("price", 0) or 0)
    if base <= 0:
        return 0
    return int(base * EVENT_PRICE_MULTIPLIER)




INVENTORY_FILE = "inventory.json"

FREE_EVENT_CLAIMS_FILE = "event_free_claims.json"

def load_inventory() -> dict:
    """Đọc toàn bộ inventory từ file JSON. Trả về dict rỗng nếu chưa có file."""
    if not os.path.exists(INVENTORY_FILE):
        return {}
    with open(INVENTORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_inventory(data: dict) -> None:
    """Ghi toàn bộ inventory xuống file JSON."""
    with open(INVENTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_item_to_inventory(user_id: int, item_name: str, price: int, class_value: str) -> None:
    """
    Thêm 1 món vào inventory của user.
    Nếu món đã tồn tại thì cộng dồn quantity lên 1.
    """
    inv = load_inventory()
    uid = str(user_id)

    if uid not in inv:
        inv[uid] = {}

    if item_name in inv[uid]:
        inv[uid][item_name]["quantity"] += 1
    else:
        inv[uid][item_name] = {
            "quantity": 1,
            "price":    price,
            "class":    class_value,
        }

    save_inventory(inv)

def get_user_inventory(user_id: int) -> dict:
    """Lấy inventory của 1 user theo user_id. Trả về dict rỗng nếu chưa có gì."""
    inv = load_inventory()
    return inv.get(str(user_id), {})


def load_free_event_claims() -> dict:
    """Đọc dữ liệu đã nhận FREE của Hội Trợ Hè. Schema: {uid: [claim_key, ...]}"""
    if not os.path.exists(FREE_EVENT_CLAIMS_FILE):
        return {}
    try:
        with open(FREE_EVENT_CLAIMS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def save_free_event_claims(data: dict) -> None:
    with open(FREE_EVENT_CLAIMS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def _free_claim_key(class_value: str, item_name: str) -> str:
    return f"{class_value}::{item_name}"


def has_claimed_free_event_item(user_id: int, class_value: str, item_name: str) -> bool:
    claims = load_free_event_claims()
    uid = str(user_id)
    key = _free_claim_key(class_value, item_name)
    user_claims = claims.get(uid, [])
    return key in user_claims


def mark_claimed_free_event_item(user_id: int, class_value: str, item_name: str) -> None:
    claims = load_free_event_claims()
    uid = str(user_id)
    key = _free_claim_key(class_value, item_name)
    if uid not in claims or not isinstance(claims.get(uid), list):
        claims[uid] = []
    if key not in claims[uid]:
        claims[uid].append(key)
    save_free_event_claims(claims)



class PurchaseSelect(discord.ui.Select):
    """Dropdown chọn món để mua trong từng gian hàng."""
    def __init__(self, class_value: str):
        self.class_value = class_value
        shop = SHOP_DATA[class_value]
        options = []
        for idx, item in enumerate(shop["items"]):
            eff_price = event_effective_price(item)
            price_label = "FREE" if eff_price == 0 else f"{eff_price} xu"
            options.append(
                discord.SelectOption(
                    label=item["name"][:100],
                    description=f"{item['desc'][:50]} | 💰 {price_label}",
                    value=str(idx),
                )
            )
        super().__init__(
            placeholder="🛒 Chọn món bạn muốn mua...",
            options=options,
            min_values=1,
            max_values=1,
        )

    async def callback(self, interaction: discord.Interaction):
        shop = SHOP_DATA[self.class_value]
        idx  = int(self.values[0])
        item = shop["items"][idx]

        eff_price = event_effective_price(item)

        if eff_price == 0:
            if has_claimed_free_event_item(interaction.user.id, self.class_value, item["name"]):
                embed = discord.Embed(
                    title="🎁 Món FREE đã nhận rồi",
                    description=(
                        f"Bạn đã nhận **{item['name']}** miễn phí từ **{shop['title']}** trước đó rồi.\n"
                        "Mỗi user chỉ được nhận mỗi món FREE **1 lần duy nhất**."
                    ),
                    color=discord.Color.red(),
                )
                embed.set_footer(text="🌊 Hội Trợ Hè")
                await interaction.response.send_message(embed=embed, ephemeral=True)
                return

            add_item_to_inventory(
                user_id     = interaction.user.id,
                item_name   = item["name"],
                price       = 0,
                class_value = self.class_value,
            )
            mark_claimed_free_event_item(interaction.user.id, self.class_value, item["name"])
            embed = discord.Embed(
                title="🎁 Nhận Miễn Phí!",
                description=(
                    f"Bạn đã nhận **{item['name']}** miễn phí từ **{shop['title']}**!\n"
                    f"*{item['desc']}*\n\n"
                    f"*Dùng `eiupack` để xem toàn bộ túi đồ*"
                ),
                color=discord.Color.green()
            )
            embed.set_footer(text="🌊 Hội Trợ Hè | Chúc bạn ngon miệng!")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return

   

        mc = mc_data()
        nguoidung = interaction.user.id
        uid_str   = str(nguoidung)

        if uid_str not in mc:
            mc[uid_str] = {}

        if mc[uid_str].get("cash", 0) < eff_price:
            purchase_success = False
        else:
            mc[uid_str]["cash"] = mc[uid_str].get("cash", 0) - int(eff_price)
            luu_data(mc)
            purchase_success = True

        remaining_Hcoins = mc[uid_str].get("cash", 0)


        if purchase_success:
            # BUG FIX 5: Lưu inventory CHỈ khi mua thành công
            add_item_to_inventory(
                user_id     = interaction.user.id,
                item_name   = item["name"],
                price       = eff_price,
                class_value = self.class_value,
            )

            user_inv    = get_user_inventory(interaction.user.id)
            current_qty = user_inv.get(item["name"], {}).get("quantity", 1)

            embed = discord.Embed(
                title="Mua Hàng Thành Công",
                description=(
                    f"**{interaction.user.display_name}** đã mua:\n"
                    f"🛍️ **{item['name']}**\n"
                    f"*{item['desc']}*\n\n"
                    f"💸 Đã trừ: **{eff_price} xu**\n"
                    f"💰 Số dư còn lại: **{remaining_Hcoins} xu**\n\n"
                    f"🎒 Túi đồ: **{item['name']}** x{current_qty}\n"
                    f"*Dùng `eiupack` để xem toàn bộ túi đồ*"
                ),
                color=discord.Color.green()
            )
            embed.set_footer(text=f"🌊 Hội Trợ Hè | {shop['title']}")
        else:
            embed = discord.Embed(
                title="Không Đủ Coin",
                description=(
                    f"Bạn cần **{eff_price} xu** để mua **{item['name']}**\n"
                    f"nhưng số dư hiện tại không đủ 😢\n\n"
                    f"Hãy kiếm thêm Hcoin rồi quay lại nhé"
                ),
                color=discord.Color.red()
            )
            embed.set_footer(text="🌊 Hội Trợ Hè | Cố lên!")

        await interaction.response.send_message(embed=embed, ephemeral=True)


class ShopView(discord.ui.View):
    """View chứa dropdown mua hàng của từng gian hàng."""
    def __init__(self, class_value: str, author_id: int):
        super().__init__(timeout=120)
        self.author_id = author_id
        self.add_item(PurchaseSelect(class_value))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.author_id:
            await interaction.response.send_message(
                "Bạn không thể dùng menu này!", ephemeral=True
            )
            return False
        return True



class eventSec(discord.ui.Select):
    def __init__(self):
        options = []
        grade_emoji = {
            "10": "<:class10:1480550771891241093>",
            "11": "<:class11:1480550771891241093>",
            "12": "<:class12:1480550771891241093>",
        }
        for key, val in SHOP_DATA.items():
            grade = key[:2]
            options.append(
                discord.SelectOption(
                    label=val["title"],
                    description=val["description"].split("\n")[1][:50],
                    emoji=grade_emoji.get(grade, "🏫"),
                    value=key,
                )
            )
        super().__init__(
            placeholder="Nhớ đi tham quan các gian hàng của trường chúng mình nhé",
            options=options,
        )

    async def callback(self, interaction: discord.Interaction):
        value = self.values[0]
        if value not in SHOP_DATA:
            await interaction.response.send_message("Gian hàng không tồn tại!", ephemeral=True)
            return

        data = SHOP_DATA[value]
        embed = discord.Embed(
            title=data["title"],
            description=data["description"],
            color=data["color"]
        )

        for item in data["items"]:
            eff_price = event_effective_price(item)
            price_str = "🎁 FREE" if eff_price == 0 else f"💰 {eff_price} {emoji_7}"
            embed.add_field(
                name=f"{item['name']} — {price_str}",
                value=item["desc"],
                inline=False,
            )

        embed.set_footer(text="🌊 Hội Trợ Hè | Nhấn nút bên dưới để mua!")

        view = ShopView(class_value=value, author_id=interaction.user.id)
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)



class eventview(discord.ui.View):
    def __init__(self, author_id: int):
        super().__init__(timeout=None)
        self.author_id = author_id
        self.add_item(eventSec())

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.author_id:
            await interaction.response.send_message(
                "Bạn không thể dùng menu này", ephemeral=True
            )
            return False
        return True



@bot.command(name="event")
async def event(ctx):
    embed = discord.Embed(
        description=(
            "## <:ngau:1474753850312491169> TRƯỜNG THPT KẺ SẶT\n"
            "*Một mùa hè rực rỡ đang chờ bạn khám phá*\n"
            "*Ở đây chúng tớ có các gian hàng, thưởng thức món ngon*\n"
            "*Bạn đã mất công tới đây rồi thì hãy lưu lại những kỷ niệm đẹp nhất nhé*\n\n"
            "**<a:cute:1472213417883336764> Hướng dẫn**\n"
            "*Chọn lớp bên dưới để xem menu gian hàng*\n\u200b"
        ),
        color=0x38EBE2
    )
    embed.add_field(
        name="🏫 Khối 10",
        value=(
            "> 🍵 Trà Quán 10A\n"
            "> 🍽️ Gian Hàng 10B\n"
            "> 🍢 Xiên Bẩn 10C\n"
            "> 🏙️ Land Mark 10D\n"
            "> 🎭 Sân Khấu 10E\n"
            "> 🎨 Góc Nghệ 10G\n"
            "> 😎 Chill Zone 10H"
        ),
        inline=True
    )
    embed.add_field(
        name="🏫 Khối 11",
        value=(
            "> 🍱 Buffet Hè 11A\n"
            "> 🍺 Quán Nhậu 11B\n"
            "> ☕ Café Sân Vườn 11C\n"
            "> 🚚 Food Truck 11D\n"
            "> 🌙 Phố Đêm 11E\n"
            "> 🌶️ Mì Cay 11G\n"
            "> 🏮 Hội Quán 11H"
        ),
        inline=True
    )
    embed.add_field(
        name="🏫 Khối 12",
        value=(
            "> 🌅 Hoàng Hôn 12A\n"
            "> 📔 Ký Ức Hè 12B\n"
            "> 🔥 Sunset BBQ 12C\n"
            "> 🛤️ Quán Cuối Đường 12D\n"
            "> 💃 Last Dance 12E\n"
            "> 📖 Chương Cuối 12G\n"
            "> 🎉 Bữa Tiệc Cuối 12H"
        ),
        inline=True
    )
    embed.set_footer(text="THPT Kẻ Sặt | Chọn gian hàng bên dưới để xem menu")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/1439931543710597201/1480566524690563103/Gemini_Generated_Image_nv9c4onv9c4onv9c-Photoroom.png?ex=69b02487&is=69aed307&hm=b6d8179ef053be06ed17ae0486841fa1174c7e960daaf44e28bb0f6560c04cba"
    )
    view = eventview(author_id=ctx.author.id)
    await ctx.send(embed=embed, view=view)


@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def pack(ctx, member: Optional[discord.Member] = None):
    target = member or ctx.author
    data   = mc_data()
    user   = str(target.id)

    pack_data = data.get(user, {}).get("pack", {})

    mo_ta = ""
    if pack_data:
        for item, so_luong in pack_data.items():
            if so_luong != 0:
                mo_ta += f"• **{item}** × {so_luong}\n\n"

    user_inv = get_user_inventory(target.id)

    if not mo_ta and not user_inv:
        embed = discord.Embed(
            title="Túi đồ của bạn hiện không có gì",
            color=0x38EBE2
        )
        await ctx.send(embed=embed)
        return

    embed = discord.Embed(
        title="Túi đồ của bạn:",
        color=0x38EBE2
    )

    if mo_ta:
        embed.add_field(
            name="🎒 Đồ vật",
            value=mo_ta,
            inline=False
        )

    if user_inv:
        grouped: dict[str, list] = {}
        total_spent = 0
        total_items = 0

        for item_name, info in user_inv.items():
            cls   = info.get("class", "?")
            qty   = info.get("quantity", 1)
            price = info.get("price", 0)
            total_spent += price * qty
            total_items += qty

            if cls not in grouped:
                grouped[cls] = []
            grouped[cls].append((item_name, qty, price))

        embed.add_field(
            name=f"🌊 Hội Trợ Hè — {total_items} món • 💸 Tổng chi: {total_spent} xu",
            value="\u200b",
            inline=False
        )

        for cls in sorted(grouped.keys()):
            class_title = SHOP_DATA.get(cls, {}).get("title", f"Lớp {cls}")
            lines = []
            for item_name, qty, price in grouped[cls]:
                price_str = "FREE" if price == 0 else f"{price} xu"
                qty_str   = f" x{qty}" if qty > 1 else ""
                lines.append(f"> {item_name}{qty_str} — {price_str}")
            embed.add_field(
                name=class_title,
                value="\n".join(lines),
                inline=False,
            )

    embed.set_thumbnail(url=target.display_avatar.url)
    embed.set_footer(text="🌊 Hội Trợ Hè THPT Kẻ Sặt | eiuevent để mua thêm")
    view = OpenTuiMu(target, data)
    await ctx.send(embed=embed, view=view)

@pack.error
async def pack_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Chờ thêm **{int(error.retry_after)}s** nữa mới dùng lại được")






def get_fb_public_info(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    res = requests.get(url, headers=headers)
    
    if res.status_code != 200:
        return "Link lỗi hoặc bị chặn"

    soup = BeautifulSoup(res.text, "html.parser")

    def get_meta(prop):
        tag = soup.find("meta", property=prop)
        return tag.get("content") if tag else None

    title_tag = soup.find("title")
    name = title_tag.text if title_tag else "Không rõ"

    data = {
        "name": name,
        "avatar": get_meta("og:image"),
        "description": get_meta("og:description"),
        "url": get_meta("og:url"),
        "type": get_meta("og:type"),
        "site_name": get_meta("og:site_name")
    }

    return data


@bot.command()
async def fb(ctx, link):
    data = get_fb_public_info(link)

    if isinstance(data, str):
        await ctx.send(data)
        return

    embed = discord.Embed(
        title=data["name"],
        description=data["description"] or "Không có mô tả",
        color=0x38EBE2
    )

    if data["avatar"]:
        embed.set_thumbnail(url=data["avatar"])

    embed.add_field(name="**Link**", value=data["url"] or link, inline=False)
    embed.add_field(name="**Loại**", value=data["type"] or "Không rõ")

    embed.set_footer(text=f"Nguồn: {data['site_name'] or 'Facebook'}")

    await ctx.send(embed=embed)




def get_tiktok_info(username):
    import requests

    url = f"https://www.tikwm.com/api/user/info?unique_id={username}"
    res = requests.get(url)
    data = res.json()

    if data.get("code") != 0:
        return "Không tìm thấy user"

    user = data.get("data", {}).get("user", {})
    stats = data.get("data", {}).get("stats", {})

    avatar = (
        user.get("avatar")
        or user.get("avatar_thumb")
        or user.get("avatarLarger")
        or "https://via.placeholder.com/150"
    )

    return {
        "username": user.get("unique_id") or user.get("uniqueId"),
        "nickname": user.get("nickname"),
        "avatar": avatar,
        "bio": user.get("signature"),

        "followers": stats.get("followerCount") or stats.get("follower_count", 0),
        "following": stats.get("followingCount") or stats.get("following_count", 0),
        "likes": stats.get("heartCount") or stats.get("total_favorited", 0)
    }
MESSAGE_ID = 1483814141733900309
ROLE_RED = 1483780067741143060
ROLE_BLUE = 1483782793409331220
@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id != MESSAGE_ID:
        return
    guild = bot.get_guild(payload.guild_id)
    if guild is None:
        return
    member = guild.get_member(payload.user_id)
    if member is None or member.bot:
        return
    if str(payload.emoji) == "☀️":
        role = guild.get_role(ROLE_RED)
        if role is not None:
            await member.add_roles(role)

    elif str(payload.emoji) == "🤯":
        role = guild.get_role(ROLE_BLUE)
        if role is not None:
            await member.add_roles(role)
@bot.event
async def on_raw_reaction_remove(payload):
    if payload.message_id != MESSAGE_ID:
        return
    guild = bot.get_guild(payload.guild_id)
    if guild is None:
        return
    member = guild.get_member(payload.user_id)
    if member is None:
        return
    if str(payload.emoji) == "☀️":
        role = guild.get_role(ROLE_RED)
        if role is not None:
            await member.remove_roles(role)
    elif str(payload.emoji) == "🤯":
        role = guild.get_role(ROLE_BLUE)
        if role is not None:
            await member.remove_roles(role)


cu_pet= ["Cow :cow2:", "Sheep :sheep:", "Bee :bee:", "Cat :cat:", "Dog :dog:", "Buffalo :water_buffalo:", "Elephant :elephant:"]

class shopseclect(discord.ui.Select):
    def __init__(self):
        luachon= [
            discord.SelectOption(
                label= "Than",
                description= "Bạn có thể mua combo 5 cục than tại đây",
                emoji= "<:than:1464971302778572860>",
                value= "than"
            ),
            discord.SelectOption(
                label= "Túi mù 20 Hcoin",
                description= "Thứ này có thể sẽ giúp bạn thử vận may",
                emoji= "<:tuimu:1484534499592372436>",
                value= "tuimu"
            ),
            discord.SelectOption(
                label= "Copper Pet",
                description= "Bạn có thể mua pet hạng đồng với 100 Hcoin",
                emoji= "🐮",
                value= "cupet"
            )
        ]
        super().__init__(
            placeholder= "Chọn vật phẩm bạn muốn mua",
            options= luachon
        )
    async def callback(self, interaction: discord.Interaction):
        data = mc_data()
        user = str(interaction.user.id)

        if user not in data:
            embed = discord.Embed(
                title="Bạn chưa có Hcoin",
                color=0x38EBE2
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return

        data[user].setdefault("pack", {})
        pack = data[user]["pack"]
        pack.setdefault("Túi mù", 0)
        pack.setdefault(f"Than {thanicon} [#2]", 0)
        value = self.values[0]
        embed = discord.Embed(
            title="Vật phẩm không hợp lệ",
            color=0x38EBE2
        )

        if value == "than":
            cash= data[user].get("cash", 0)
            if cash < 100:
                embed= discord.Embed(
                    title= f"Bạn không đủ **100** Hcoin để có thể mua combo 5 than {thanicon}",
                    color= 0x38EBE2
                )
            else:
                data[user]["cash"] = cash - 100
                pack[f"Than {thanicon} [#2]"] = pack.get(f"Than {thanicon} [#2]", 0) + 5
                embed= discord.Embed(
                    title= "Bạn đã mua combo 5 than với **100** Hcoin từ HanhDun Shop 🔥",
                    color=0x38EBE2
                )
                luu_data(data)
        elif value == "tuimu":
            cash= data[user].get("cash",0)
            
            if cash < 20:
                embed= discord.Embed(
                    title= "Bạn không đủ **20** Hcoin để có thể mua túi mù",
                    color= 0x38EBE2
                )
            else:
                data[user]["cash"] = cash - 20
                pack["Túi mù"] = pack.get("Túi mù", 0) + 1
                embed= discord.Embed(
                    title= "Bạn đã mua túi mù với **20** Hcoin từ HanhDun Shop <:tuimu:1484534499592372436>",
                    color= 0x38EBE2
                )
                luu_data(data)
        elif value == "cupet":
            cash =data[user].get("cash", 0)
            if cash < 100:
                embed= discord.Embed(
                    title= "Bạn không đủ **100** Hcoin để có thể mua pet hạng đồng",
                    color= 0x38EBE2
                )
            else:
                pet= random.choice(cu_pet)
                data[user]["cash"] = cash - 100
                pack[pet] = pack.get(pet, 0) + 1
                embed= discord.Embed(
                    title= "Cảm ơn bạn đã mua pet của cúng tôi :heart_hands:",
                    description= f"**:confetti_ball: Chúc mừng** bạn đã mua được bé **{pet}**",
                    color= 0x38EBE2
                )
                luu_data(data)
        
        if interaction.response.is_done():
            await interaction.edit_original_response(embed=embed, view=self.view)
        else:
            await interaction.response.edit_message(embed=embed, view=self.view)

class shopView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout= 180)
        self.add_item(shopseclect())

@bot.command()
@commands.cooldown(1,10, commands.BucketType.user)
async def shop(ctx):
    embed= discord.Embed(
        title= "Chào mừng đến với HanhDun Shop ",
        description=(
            f"Xin chào **{ctx.author}**.\n"
            "Đây chính là cửa hàng của tôi HanhDun <:ngau:1474753850312491169>\n"
            "Hãy vui vẻ tận huởng hành trình của riêng bạn nhé.\n\n"
            "Bạn vui lòng chọn sản phẩm bên dưới để có thể mua ❤️‍🔥"
        ),
        color= 0x38EBE2
    )
    await ctx.send(embed= embed, view= shopView())
@shop.error
async def shop_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Chờ thêm **{int(error.retry_after)}s** nữa mới dùng lại được")
        return

    original_error = getattr(error, "original", error)
    traceback.print_exception(type(original_error), original_error, original_error.__traceback__)
    await ctx.send("Lệnh shop đang lỗi nội bộ. Mình đã hiện log ở console để kiểm tra.")


HERO_FILE= "hero.json"
def hero_data():
    if not os.path.exists(HERO_FILE):
        try:
            with open(HERO_FILE, "w") as f:
                json.dump({}, f)
        except PermissionError:
            print("khog co quyen")
            return {}
    try:
        with open(HERO_FILE, "r") as f:
            return json.load(f)
    except (PermissionError, json.JSONDecodeError) as e:
        print("loi doc file")
        return {}
def luu_hero(data):
    try:
        with open(HERO_FILE, "w") as f:
            json.dump(data, f, indent= 4)
    except PermissionError:
        print("loi ghi file")
        return


MAX_HERO_LEVEL = 20


def _hero_progress_values(entry: dict) -> Tuple[int, int]:
    if not isinstance(entry, dict):
        return 1, 0
    level = max(1, int(entry.get("level", 1) or 1))
    exp = max(0, int(entry.get("exp", 0) or 0))
    return level, exp


def _hero_entry_has_progress(entry: dict) -> bool:
    level, exp = _hero_progress_values(entry)
    return level > 1 or exp > 0


def sync_current_hero_legacy_progress(data: dict, user_id_str: str) -> None:
    profile = data[user_id_str]
    current_hero = int(profile.get("hero", 0) or 0)
    if current_hero not in HERO_KIT:
        profile["level"] = 1
        profile["exp"] = 0
        return

    level, exp = _hero_progress_values(profile["heroes"].get(str(current_hero), {}))
    profile["level"] = level
    profile["exp"] = exp


def ensure_hero_profile(data: dict, user_id_str: str) -> None:
    """Đảm bảo user có đủ field trong hero.json."""
    if user_id_str not in data:
        data[user_id_str] = {}
    profile = data[user_id_str]
    profile.setdefault("hero", 0)
    profile.setdefault("heroes", {})
    profile.setdefault("hero_progress_migrated", False)

    heroes = profile["heroes"]
    if not isinstance(heroes, dict):
        heroes = {}
        profile["heroes"] = heroes

    for hero_id in HERO_KIT.keys():
        key = str(hero_id)
        if key not in heroes or not isinstance(heroes.get(key), dict):
            heroes[key] = {"level": 1, "exp": 0}
        else:
            heroes[key].setdefault("level", 1)
            heroes[key].setdefault("exp", 0)

    old_level = int(profile.get("level", 1) or 1)
    old_exp = int(profile.get("exp", 0) or 0)
    current_hero = int(profile.get("hero", 0) or 0)
    has_saved_hero_progress = any(_hero_entry_has_progress(entry) for entry in heroes.values())

    if has_saved_hero_progress:
        profile["hero_progress_migrated"] = True

    if (
        current_hero in HERO_KIT
        and not bool(profile.get("hero_progress_migrated", False))
        and not has_saved_hero_progress
        and (old_level != 1 or old_exp != 0)
    ):
        heroes[str(current_hero)] = {"level": max(1, old_level), "exp": max(0, old_exp)}
        profile["hero_progress_migrated"] = True

    if current_hero in HERO_KIT:
        sync_current_hero_legacy_progress(data, user_id_str)
    else:
        profile.setdefault("level", 1)
        profile.setdefault("exp", 0)


def hero_next_level_cost(level: int) -> int:
    level = max(1, int(level))
    return 5 + (level - 1) * 3


def hero_effective_max_hp(hero_id: int, level: int) -> int:
    base = _max_hp(hero_id)
    level = max(1, int(level))
    multiplier = 1.0 + 0.05 * (level - 1)
    return int(round(base * multiplier))


def get_hero_progress(hero_db: dict, user_id_str: str, hero_id: int) -> Tuple[int, int]:
    ensure_hero_profile(hero_db, user_id_str)
    if hero_id not in HERO_KIT:
        return 1, 0
    entry = hero_db[user_id_str]["heroes"].get(str(hero_id), {})
    level = int(entry.get("level", 1) or 1)
    exp = int(entry.get("exp", 0) or 0)
    return max(1, level), max(0, exp)


def set_hero_progress(hero_db: dict, user_id_str: str, hero_id: int, level: int, exp: int) -> None:
    ensure_hero_profile(hero_db, user_id_str)
    if hero_id not in HERO_KIT:
        return
    level = max(1, int(level))
    exp = max(0, int(exp))
    hero_db[user_id_str]["heroes"][str(hero_id)] = {"level": level, "exp": exp}
    hero_db[user_id_str]["hero_progress_migrated"] = True
    sync_current_hero_legacy_progress(hero_db, user_id_str)


def hero_damage_multiplier(hero_id: int, level: int) -> float:
    level = max(1, int(level))
    if hero_id == 1:
        return 1.0 + 0.025 * (level - 1)
    if hero_id == 2:
        return 1.0 + 0.035 * (level - 1)
    if hero_id == 3:
        return 1.0 + 0.03 * (level - 1)
    return 1.0


def hero_damage_reduction(hero_id: int, level: int) -> float:
    level = max(1, int(level))
    if hero_id == 1:
        return min(0.30, 0.02 * (level - 1))
    if hero_id == 2:
        return min(0.18, 0.012 * (level - 1))
    if hero_id == 3:
        return min(0.22, 0.015 * (level - 1))
    return 0.0


def build_hero_pick_description(hero_id: int, user_id: int) -> str:
    kit = HERO_KIT.get(hero_id)
    if not kit:
        return "Không rõ tướng."

    db = hero_data()
    uid = str(user_id)
    level, exp = get_hero_progress(db, uid, hero_id)
    need = hero_next_level_cost(level)

    mult = hero_damage_multiplier(hero_id, level)
    reduction = hero_damage_reduction(hero_id, level)
    hp = hero_effective_max_hp(hero_id, level)

    basic = kit.get("basic", {})
    basic_dmg = int(round(int(basic.get("damage", 0) or 0) * mult))

    s1 = kit.get("s1", {})
    s1_dmg = int(round(int(s1.get("damage", 0) or 0) * mult)) if "damage" in s1 else 0

    s2 = kit.get("s2", {})
    s3 = kit.get("s3", {})

    lines: list[str] = []
    lines.append(f"Bạn đã chọn tướng: **{kit['name']}** ({kit['emoji']}).")
    lines.append(f"Cấp: **{level}** (EXP: **{exp}/{need}**) — Mỗi tướng có level riêng")
    lines.append(f"HP (khi fight): **{hp}**")
    lines.append(f"Tăng sát thương theo cấp: **x{mult:.3g}**")
    lines.append(f"Phòng thủ theo cấp: giảm sát thương nhận **{int(round(reduction*100))}%**")
    lines.append("")

    lines.append(f"**Đánh thường**: **{basic_dmg}** sát thương")

    if s1:
        cd = s1.get("cd_s")
        cd_txt = f" (CD {cd}s)" if cd is not None else ""
        if "damage" in s1:
            lines.append(f"**Chiêu 1 – {s1.get('name','')}**: **{s1_dmg}** sát thương{cd_txt}")
        else:
            lines.append(f"**Chiêu 1 – {s1.get('name','')}**{cd_txt}")

        if hero_id == 2:
            true_bonus = int(s1.get("true_bonus", 0) or 0)
            if true_bonus > 0:
                true_scaled = int(round(true_bonus * mult))
                threshold = float(s1.get("execute_true_if_target_below", 0) or 0)
                if threshold > 0:
                    lines.append(f"- +**{true_scaled}** sát thương chuẩn nếu mục tiêu < **{int(threshold*100)}%** HP")

    if s2:
        cd = s2.get("cd_s")
        cd_txt = f" (CD {cd}s)" if cd is not None else ""
        if hero_id == 1:
            shield_base = int(s2.get("shield", 0) or 0)
            shield = int(round(shield_base * (1.0 + 0.03 * (level - 1))))
            lines.append(f"**Chiêu 2 – {s2.get('name','')}**: khiên **{shield}**{cd_txt}")
        elif hero_id == 2:
            empower = int(s2.get("empower_bonus", 0) or 0)
            empower_scaled = int(round(empower * mult))
            lines.append(f"**Chiêu 2 – {s2.get('name','')}**: đòn kế +**{empower_scaled}** sát thương{cd_txt}")
        elif hero_id == 3:
            dmg = int(round(int(s2.get("damage", 0) or 0) * mult))
            freeze = int(s2.get("freeze_turns", 0) or 0)
            lines.append(f"**Chiêu 2 – {s2.get('name','')}**: **{dmg}** sát thương, đóng băng **{freeze}** lượt{cd_txt}")

    if s3:
        cd = s3.get("cd_s")
        cd_txt = f" (CD {cd}s)" if cd is not None else ""
        if hero_id == 1:
            rage_turns = int(s3.get("rage_turns", 0) or 0)
            bonus = int(s3.get("bonus_damage", 0) or 0)
            bonus_scaled = int(round(bonus * mult))
            ls = float(s3.get("lifesteal", 0) or 0)
            lines.append(f"**Chiêu 3 – {s3.get('name','')}**: cuồng nộ **{rage_turns}** lượt, mỗi đòn +**{bonus_scaled}** sát thương, hút máu **{int(ls*100)}%**{cd_txt}")
        elif hero_id == 2:
            dmg = int(round(int(s3.get("damage", 0) or 0) * mult))
            threshold = float(s3.get("execute_kill_if_target_below", 0) or 0)
            if threshold > 0:
                lines.append(f"**Chiêu 3 – {s3.get('name','')}**: **{dmg}** sát thương, kết liễu nếu mục tiêu < **{int(threshold*100)}%** HP{cd_txt}")
            else:
                lines.append(f"**Chiêu 3 – {s3.get('name','')}**: **{dmg}** sát thương{cd_txt}")
        elif hero_id == 3:
            dmg = int(round(int(s3.get("damage", 0) or 0) * mult))
            lines.append(f"**Chiêu 3 – {s3.get('name','')}**: **{dmg}** sát thương{cd_txt}")

    return "\n".join(lines)


def set_current_hero(data: dict, user_id_str: str, hero_id: int) -> None:
    ensure_hero_profile(data, user_id_str)
    if hero_id not in HERO_KIT:
        return
    profile = data[user_id_str]
    old_level = int(profile.get("level", 1) or 1)
    old_exp = int(profile.get("exp", 0) or 0)
    has_saved_hero_progress = any(_hero_entry_has_progress(entry) for entry in profile["heroes"].values())

    profile["hero"] = hero_id
    if (
        not bool(profile.get("hero_progress_migrated", False))
        and not has_saved_hero_progress
        and (old_level != 1 or old_exp != 0)
    ):
        profile["heroes"][str(hero_id)] = {"level": max(1, old_level), "exp": max(0, old_exp)}
        profile["hero_progress_migrated"] = True

    sync_current_hero_legacy_progress(data, user_id_str)


HERO_EMBED_COLOR = 0x38EBE2

DAU_SI_EMBED_DESC = (
    "Bạn đã chọn tướng: **Đấu Sĩ** (⚔️).\n"
    "HP: **2500**\n\n"
    "**Chiêu 1 – Chém Xung Kích**\n"
    "- Damage: **180** sát thương vật lý\n"
    "- Làm chậm: **30%** trong **1.5s**\n"
    "- ⏱️ Hồi chiêu: **5s**\n\n"
    "**Chiêu 2 – Khiên Bất Diệt**\n"
    "- Khiên: **500** sát thương trong **3s**\n"
    "- ⏱️ Hồi chiêu: **10s**\n\n"
    "**Chiêu 3 – Cuồng Nộ Chiến Thần (Ultimate)**\n"
    "- **6s**: mỗi đòn đánh gây thêm **220** sát thương (AOE)\n"
    "- Hút máu: **25%** sát thương gây ra\n"
    "- ⏱️ Hồi chiêu: **25s**"
)

SAT_THU_EMBED_DESC = (
    "Bạn đã chọn tướng: **Sát Thủ** (🗡️).\n"
    "HP: **1500**\n\n"
    "**Chiêu 1 – Phi Tiêu Bóng Tối**\n"
    "- Damage: **300** sát thương vật lý\n"
    "- +**200** sát thương chuẩn nếu mục tiêu < **50%** máu\n"
    "- ⏱️ Hồi chiêu: **4s**\n\n"
    "**Chiêu 2 – Tàng Hình**\n"
    "- Ẩn thân **2.5s**\n"
    "- Đòn sau: +**280** sát thương\n"
    "- ⏱️ Hồi chiêu: **12s**\n\n"
    "**Chiêu 3 – Ám Sát Tuyệt Đối (Ultimate)**\n"
    "- Damage: **600** sát thương vật lý\n"
    "- Kết liễu nếu mục tiêu < **30%** máu\n"
    "- ⏱️ Hồi chiêu: **20s**"
)

PHAP_SU_EMBED_DESC = (
    "Bạn đã chọn tướng: **Pháp Sư** (🪄).\n"
    "HP: **1800**\n\n"
    "**Chiêu 1 – Cầu Lửa**\n"
    "- Damage: **250** sát thương phép\n"
    "- Lan: **125** sát thương\n"
    "- ⏱️ Hồi chiêu: **6s**\n\n"
    "**Chiêu 2 – Băng Trói**\n"
    "- Damage: **150/s** trong **2s** (tổng **300**)\n"
    "- Đóng băng **1.5s**\n"
    "- ⏱️ Hồi chiêu: **12s**\n\n"
    "**Chiêu 3 – Đại Hủy Diệt (Ultimate)**\n"
    "- **3** lần thiên thạch, mỗi lần **300** sát thương\n"
    "- Tổng: **900** sát thương diện rộng\n"
    "- ⏱️ Hồi chiêu: **30s**"
)


def _cooldown_turns_from_seconds(seconds: float) -> int:
    # Turn-based conversion: every 5s ~= 1 turn.
    return max(1, math.ceil(seconds / 5))


HERO_KIT = {
    1: {
        "key": "dausi",
        "name": "Đấu Sĩ",
        "emoji": "⚔️",
        "max_hp": 2500,
        "basic": {"name": "Đánh thường", "damage": 50, "type": "physical"},
        "s1": {"name": "Chém Xung Kích", "damage": 180, "type": "physical", "cd_s": 5},
        "s2": {"name": "Khiên Bất Diệt", "shield": 500, "shield_turns": 1, "cd_s": 10},
        "s3": {"name": "Cuồng Nộ Chiến Thần", "rage_turns": 2, "bonus_damage": 220, "lifesteal": 0.25, "cd_s": 25},
    },
    2: {
        "key": "satthu",
        "name": "Sát Thủ",
        "emoji": "🗡️",
        "max_hp": 1500,
        "basic": {"name": "Đánh thường", "damage": 50, "type": "physical"},
        "s1": {"name": "Phi Tiêu Bóng Tối", "damage": 300, "type": "physical", "cd_s": 4, "execute_true_if_target_below": 0.50, "true_bonus": 200},
        "s2": {"name": "Tàng Hình", "empower_bonus": 280, "cd_s": 12},
        "s3": {"name": "Ám Sát Tuyệt Đối", "damage": 600, "type": "physical", "cd_s": 20, "execute_kill_if_target_below": 0.30},
    },
    3: {
        "key": "phapsu",
        "name": "Pháp Sư",
        "emoji": "🪄",
        "max_hp": 1800,
        "basic": {"name": "Đánh thường", "damage": 50, "type": "magic"},
        "s1": {"name": "Cầu Lửa", "damage": 250, "type": "magic", "cd_s": 6},
        "s2": {"name": "Băng Trói", "damage": 300, "type": "magic", "cd_s": 12, "freeze_turns": 1},
        "s3": {"name": "Đại Hủy Diệt", "damage": 900, "type": "magic", "cd_s": 30},
    },
}


@dataclass
class FighterState:
    user_id: int
    hero_id: int
    hp: int
    level: int = 1
    shield: int = 0
    shield_turns_left: int = 0
    skip_turns: int = 0
    empower_next_damage: int = 0
    rage_turns_left: int = 0
    # cooldown turns left
    cd_basic: int = 0
    cd_s1: int = 0
    cd_s2: int = 0
    cd_s3: int = 0


def _apply_shield(target: FighterState, incoming_damage: int) -> Tuple[int, int]:
    """Returns (damage_to_hp, absorbed_by_shield)."""
    if incoming_damage <= 0:
        return 0, 0
    if target.shield <= 0:
        return incoming_damage, 0
    absorbed = min(target.shield, incoming_damage)
    target.shield -= absorbed
    return incoming_damage - absorbed, absorbed


def _hero_name(hero_id: int) -> str:
    kit = HERO_KIT.get(hero_id)
    if not kit:
        return "Không rõ"
    return f"{kit['emoji']} {kit['name']}"


def _max_hp(hero_id: int) -> int:
    kit = HERO_KIT.get(hero_id)
    return int(kit["max_hp"]) if kit else 1000


def _format_cd(turns: int) -> str:
    return "0" if turns <= 0 else str(turns)


def _fight_embed(
    ctx: commands.Context,
    p1: FighterState,
    p2: FighterState,
    turn_user_id: int,
    log_lines: List[str],
) -> discord.Embed:
    guild = ctx.guild
    u1 = guild.get_member(p1.user_id) if guild else None
    u2 = guild.get_member(p2.user_id) if guild else None
    name1 = u1.display_name if u1 else str(p1.user_id)
    name2 = u2.display_name if u2 else str(p2.user_id)

    def status_line(p: FighterState) -> str:
        parts = []
        if p.shield > 0:
            parts.append(f"Khiên: **{p.shield}**")
        if p.empower_next_damage > 0:
            parts.append(f"Cường hoá: **+{p.empower_next_damage}**")
        if p.rage_turns_left > 0:
            parts.append(f"Cuồng nộ: **{p.rage_turns_left}** lượt")
        if p.skip_turns > 0:
            parts.append(f"Choáng: **mất {p.skip_turns}** lượt")
        return " | ".join(parts) if parts else "Không"

    embed = discord.Embed(
        title="⚔️ Fight 1v1",
        description=(
            f"**Tới lượt:** <@{turn_user_id}>\n\n"
            f"**{name1}** — {_hero_name(p1.hero_id)}\n"
            f"Cấp: **{p1.level}** | HP: **{p1.hp}/{hero_effective_max_hp(p1.hero_id, p1.level)}**\n"
            f"Trạng thái: {status_line(p1)}\n"
            f"CD: S1 **{_format_cd(p1.cd_s1)}** | S2 **{_format_cd(p1.cd_s2)}** | S3 **{_format_cd(p1.cd_s3)}**\n\n"
            f"**{name2}** — {_hero_name(p2.hero_id)}\n"
            f"Cấp: **{p2.level}** | HP: **{p2.hp}/{hero_effective_max_hp(p2.hero_id, p2.level)}**\n"
            f"Trạng thái: {status_line(p2)}\n"
            f"CD: S1 **{_format_cd(p2.cd_s1)}** | S2 **{_format_cd(p2.cd_s2)}** | S3 **{_format_cd(p2.cd_s3)}**\n\n"
            f"**Diễn biến:**\n" + ("\n".join(log_lines[-6:]) if log_lines else "Chưa có hành động")
        ),
        color=0xFFC0CB,
    )
    return embed


ACTIVE_FIGHT_USERS: set[int] = set()


class FightView(discord.ui.View):
    def __init__(
        self,
        ctx: commands.Context,
        p1: FighterState,
        p2: FighterState,
    ):
        super().__init__(timeout=180)
        self.ctx = ctx
        self.p1 = p1
        self.p2 = p2
        self.turn = random.choice([0, 1])  
        self.log_lines: List[str] = []
        self.message: Optional[discord.Message] = None
        self._start_turn()

    def _current(self) -> FighterState:
        return self.p1 if self.turn == 0 else self.p2

    def _other(self) -> FighterState:
        return self.p2 if self.turn == 0 else self.p1

    def _start_turn(self) -> None:
        p = self._current()
        p.cd_s1 = max(0, p.cd_s1 - 1)
        p.cd_s2 = max(0, p.cd_s2 - 1)
        p.cd_s3 = max(0, p.cd_s3 - 1)

        if p.shield_turns_left > 0:
            p.shield_turns_left -= 1
            if p.shield_turns_left <= 0:
                p.shield = 0
        if p.rage_turns_left > 0:
            p.rage_turns_left -= 1

    def _end_turn(self) -> None:
        self.turn = 1 - self.turn
        next_p = self._current()
        if next_p.skip_turns > 0:
            next_p.skip_turns -= 1
            self.log_lines.append(f"<@{next_p.user_id}> bị đóng băng và mất lượt!")
            self.turn = 1 - self.turn
        self._start_turn()

    def _winner_id(self) -> Optional[int]:
        if self.p1.hp <= 0 and self.p2.hp <= 0:
            return 0
        if self.p1.hp <= 0:
            return self.p2.user_id
        if self.p2.hp <= 0:
            return self.p1.user_id
        return None

    def _make_embed(self) -> discord.Embed:
        return _fight_embed(
            self.ctx,
            self.p1,
            self.p2,
            self._current().user_id,
            self.log_lines,
        )

    def _update_button_state(self) -> None:
        cur = self._current()
        self.s1_btn.disabled = cur.cd_s1 > 0
        self.s2_btn.disabled = cur.cd_s2 > 0
        self.s3_btn.disabled = cur.cd_s3 > 0

    async def _refresh(self) -> None:
        self._update_button_state()
        if self.message:
            await self.message.edit(embed=self._make_embed(), view=self)

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id not in (self.p1.user_id, self.p2.user_id):
            await interaction.response.send_message("Bạn không phải người trong trận này.", ephemeral=True)
            return False
        if interaction.user.id != self._current().user_id:
            await interaction.response.send_message("Chưa tới lượt bạn.", ephemeral=True)
            return False
        return True

    async def on_timeout(self) -> None:
        for child in self.children:
            if isinstance(child, discord.ui.Button):
                child.disabled = True
        try:
            if self.message:
                await self.message.edit(content="⏳ Trận đấu đã hết thời gian.", view=self)
        finally:
            ACTIVE_FIGHT_USERS.discard(self.p1.user_id)
            ACTIVE_FIGHT_USERS.discard(self.p2.user_id)

    def _deal_damage(
        self,
        attacker: FighterState,
        defender: FighterState,
        base_damage: int,
        damage_type: str,
        true_damage: int = 0,
    ) -> Tuple[int, int, int]:
        """Returns (hp_damage, shield_absorbed, true_damage_applied)."""
        raw_damage = int(base_damage)
        if attacker.empower_next_damage > 0 and raw_damage > 0:
            raw_damage += attacker.empower_next_damage
            attacker.empower_next_damage = 0

        rage_lifesteal = 0.0
        if attacker.hero_id == 1:
            kit = HERO_KIT[1]["s3"]
            if attacker.rage_turns_left > 0 and raw_damage > 0:
                raw_damage += int(kit["bonus_damage"])
                rage_lifesteal = float(kit["lifesteal"])

        damage = max(0, int(raw_damage))
        if damage > 0:
            mult = float(hero_damage_multiplier(attacker.hero_id, attacker.level))
            damage = int(round(damage * mult))

            reduction = float(hero_damage_reduction(defender.hero_id, defender.level))
            damage = int(round(damage * (1.0 - reduction)))
            if damage <= 0:
                damage = 1

        true_damage_scaled = 0
        if true_damage and true_damage > 0:
            mult = float(hero_damage_multiplier(attacker.hero_id, attacker.level))
            true_damage_scaled = max(1, int(round(int(true_damage) * mult)))

        hp_damage, absorbed = _apply_shield(defender, damage)
        defender.hp = max(0, defender.hp - hp_damage)

        true_applied = 0
        if true_damage_scaled > 0 and defender.hp > 0:
            true_applied = min(defender.hp, int(true_damage_scaled))
            defender.hp = max(0, defender.hp - true_applied)

        total_hp_damage = hp_damage + true_applied
        if rage_lifesteal > 0 and total_hp_damage > 0:
            heal = int(total_hp_damage * rage_lifesteal)
            attacker.hp = min(hero_effective_max_hp(attacker.hero_id, attacker.level), attacker.hp + heal)
        return hp_damage, absorbed, true_applied

    def _set_cooldown(self, attacker: FighterState, skill_key: str) -> None:
        kit = HERO_KIT[attacker.hero_id]
        if skill_key == "s1":
            attacker.cd_s1 = _cooldown_turns_from_seconds(kit["s1"]["cd_s"])
        elif skill_key == "s2":
            attacker.cd_s2 = _cooldown_turns_from_seconds(kit["s2"]["cd_s"])
        elif skill_key == "s3":
            attacker.cd_s3 = _cooldown_turns_from_seconds(kit["s3"]["cd_s"])

    async def _after_action(self, interaction: discord.Interaction) -> None:
        winner = self._winner_id()
        if winner is not None:
            for child in self.children:
                if isinstance(child, discord.ui.Button):
                    child.disabled = True
            if winner == 0:
                content = "🤝 Kết quả: Hoà!"
            else:
                content = f"🏆 Người thắng: <@{winner}>"
            await interaction.response.edit_message(content=content, embed=self._make_embed(), view=self)
            ACTIVE_FIGHT_USERS.discard(self.p1.user_id)
            ACTIVE_FIGHT_USERS.discard(self.p2.user_id)
            self.stop()
            return

        self._end_turn()
        await interaction.response.edit_message(embed=self._make_embed(), view=self)
        await self._refresh()

    @discord.ui.button(label="⚔️ Chiêu 1", style=discord.ButtonStyle.primary)
    async def s1_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        attacker = self._current()
        defender = self._other()
        kit = HERO_KIT[attacker.hero_id]
        s1 = kit["s1"]

        true_damage = 0
        if attacker.hero_id == 2:
            threshold = float(s1.get("execute_true_if_target_below", 0))
            if threshold > 0:
                if defender.hp <= int(hero_effective_max_hp(defender.hero_id, defender.level) * threshold):
                    true_damage = int(s1.get("true_bonus", 0))

        hp_dmg, absorbed, true_applied = self._deal_damage(
            attacker,
            defender,
            base_damage=int(s1.get("damage", 0)),
            damage_type=str(s1.get("type", "physical")),
            true_damage=true_damage,
        )
        extra = []
        if absorbed > 0:
            extra.append(f"hấp thụ {absorbed}")
        if true_applied > 0:
            extra.append(f"chuẩn {true_applied}")
        extra_text = f" ({', '.join(extra)})" if extra else ""
        self.log_lines.append(
            f"<@{attacker.user_id}> dùng **{s1['name']}** gây **{hp_dmg}** sát thương{extra_text} lên <@{defender.user_id}>."
        )
        self._set_cooldown(attacker, "s1")
        await self._after_action(interaction)

    @discord.ui.button(label="❄️ Chiêu 2", style=discord.ButtonStyle.secondary)
    async def s2_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        attacker = self._current()
        defender = self._other()
        kit = HERO_KIT[attacker.hero_id]
        s2 = kit["s2"]

        if attacker.hero_id == 1:
            shield_base = int(s2.get("shield", 0))
            attacker.shield = int(round(shield_base * (1.0 + 0.03 * (max(1, attacker.level) - 1))))
            attacker.shield_turns_left = int(s2.get("shield_turns", 1))
            self.log_lines.append(
                f"<@{attacker.user_id}> dùng **{s2['name']}** tạo khiên **{attacker.shield}**."
            )
        elif attacker.hero_id == 2:
            attacker.empower_next_damage = int(s2.get("empower_bonus", 0))
            self.log_lines.append(
                f"<@{attacker.user_id}> dùng **{s2['name']}**: đòn đánh kế tiếp +**{attacker.empower_next_damage}** sát thương."
            )
        elif attacker.hero_id == 3:
            hp_dmg, absorbed, true_applied = self._deal_damage(
                attacker,
                defender,
                base_damage=int(s2.get("damage", 0)),
                damage_type=str(s2.get("type", "magic")),
            )
            freeze_turns = int(s2.get("freeze_turns", 0))
            if freeze_turns > 0 and defender.hp > 0:
                defender.skip_turns += freeze_turns
            extra_text = ""
            if absorbed > 0:
                extra_text = f" (hấp thụ {absorbed})"
            self.log_lines.append(
                f"<@{attacker.user_id}> dùng **{s2['name']}** gây **{hp_dmg}** sát thương{extra_text} lên <@{defender.user_id}> và đóng băng **{freeze_turns}** lượt."
            )

        self._set_cooldown(attacker, "s2")
        await self._after_action(interaction)

    @discord.ui.button(label="🔥 Chiêu 3", style=discord.ButtonStyle.danger)
    async def s3_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        attacker = self._current()
        defender = self._other()
        kit = HERO_KIT[attacker.hero_id]
        s3 = kit["s3"]

        if attacker.hero_id == 1:
            attacker.rage_turns_left = int(s3.get("rage_turns", 2))
            self.log_lines.append(
                f"<@{attacker.user_id}> kích hoạt **{s3['name']}** trong **{attacker.rage_turns_left}** lượt."
            )
        elif attacker.hero_id == 2:
            # execute
            threshold = float(s3.get("execute_kill_if_target_below", 0))
            if threshold > 0 and defender.hp <= int(hero_effective_max_hp(defender.hero_id, defender.level) * threshold):
                defender.hp = 0
                self.log_lines.append(
                    f"<@{attacker.user_id}> dùng **{s3['name']}** và **kết liễu** <@{defender.user_id}>!"
                )
            else:
                hp_dmg, absorbed, true_applied = self._deal_damage(
                    attacker,
                    defender,
                    base_damage=int(s3.get("damage", 0)),
                    damage_type=str(s3.get("type", "physical")),
                )
                extra_text = f" (hấp thụ {absorbed})" if absorbed > 0 else ""
                self.log_lines.append(
                    f"<@{attacker.user_id}> dùng **{s3['name']}** gây **{hp_dmg}** sát thương{extra_text} lên <@{defender.user_id}>."
                )
        elif attacker.hero_id == 3:
            hp_dmg, absorbed, true_applied = self._deal_damage(
                attacker,
                defender,
                base_damage=int(s3.get("damage", 0)),
                damage_type=str(s3.get("type", "magic")),
            )
            extra_text = f" (hấp thụ {absorbed})" if absorbed > 0 else ""
            self.log_lines.append(
                f"<@{attacker.user_id}> gọi **{s3['name']}** gây tổng **{hp_dmg}** sát thương{extra_text} lên <@{defender.user_id}>."
            )

        self._set_cooldown(attacker, "s3")
        await self._after_action(interaction)

    @discord.ui.button(label="⏳ Bỏ lượt", style=discord.ButtonStyle.success)
    async def skip_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        attacker = self._current()
        self.log_lines.append(f"<@{attacker.user_id}> bỏ lượt.")
        await self._after_action(interaction)


@bot.command()
async def fight(ctx, opponent: discord.Member):
    """Đấu 1v1 theo lượt với nút bấm dùng chiêu."""
    if opponent.bot:
        await ctx.send("Không thể fight với bot.")
        return
    if opponent.id == ctx.author.id:
        await ctx.send("Không thể fight với chính mình.")
        return

    if ctx.author.id in ACTIVE_FIGHT_USERS or opponent.id in ACTIVE_FIGHT_USERS:
        await ctx.send("Một trong hai người đang ở trong trận khác rồi.")
        return

    data = hero_data()
    a = str(ctx.author.id)
    b = str(opponent.id)
    ensure_hero_profile(data, a)
    ensure_hero_profile(data, b)
    hero_a = int(data.get(a, {}).get("hero", 0) or 0)
    hero_b = int(data.get(b, {}).get("hero", 0) or 0)
    level_a, _exp_a = get_hero_progress(data, a, hero_a)
    level_b, _exp_b = get_hero_progress(data, b, hero_b)

    if hero_a not in HERO_KIT:
        await ctx.send(f"{ctx.author.mention} chưa chọn tướng. Dùng lệnh `eiupick` trước nhé.")
        return
    if hero_b not in HERO_KIT:
        await ctx.send(f"{opponent.mention} chưa chọn tướng. Dùng lệnh `eiupick` trước nhé.")
        return

    p1 = FighterState(user_id=ctx.author.id, hero_id=hero_a, level=level_a, hp=hero_effective_max_hp(hero_a, level_a))
    p2 = FighterState(user_id=opponent.id, hero_id=hero_b, level=level_b, hp=hero_effective_max_hp(hero_b, level_b))
    view = FightView(ctx, p1, p2)
    view._update_button_state()

    ACTIVE_FIGHT_USERS.add(ctx.author.id)
    ACTIVE_FIGHT_USERS.add(opponent.id)

    embed = view._make_embed()
    msg = await ctx.send(
        content=f"🎮 Trận đấu bắt đầu: {ctx.author.mention} vs {opponent.mention}",
        embed=embed,
        view=view,
    )
    view.message = msg




class pick_hero(discord.ui.Select):
    def __init__(self):
        luachon= [
            discord.SelectOption(
                label= "Đấu Sĩ",
                description= "Bạn sẽ là chiến binh với sức công thủ toàn diện",
                emoji= "⚔️",
                value= "dausi"
            ),
            discord.SelectOption(
                label= "Sát Thủ",
                description= "Bạn sẽ là một sát thủ thầm lặng",
                emoji= "🗡️",
                value= "satthu"
            ),
            discord.SelectOption(
                label= "Pháp Sư",
                description= "Bạn sẽ là một pháp sư tài ba",
                emoji= "🪄",
                value= "phapsu"
            )
        ]
        super().__init__(
            placeholder= "Hãy chọn một tướng để khi chiến đầu",
            options= luachon
        )
    async def callback(self, interaction: discord.Interaction):
        async def _respond(updated_embed: discord.Embed):
            try:
                await interaction.response.edit_message(embed=updated_embed, view=self.view)
            except discord.errors.InteractionResponded:
                await interaction.edit_original_response(embed=updated_embed, view=self.view)

        data= hero_data()
        user= str(interaction.user.id)
        ensure_hero_profile(data, user)
        hero_by_value = {
            "dausi": 1,
            "satthu": 2,
            "phapsu": 3,
        }
        hero_id = hero_by_value.get(self.values[0])
        if hero_id is None:
            await interaction.response.send_message("Không tìm thấy tướng hợp lệ.", ephemeral=True)
            return

        set_current_hero(data, user, hero_id)
        luu_hero(data)

        embed= discord.Embed(
            title= "🎉 Chọn Tướng Thành Công",
            description= build_hero_pick_description(hero_id, interaction.user.id),
            color= HERO_EMBED_COLOR
        )
        await _respond(embed)
class pick_hero_view(discord.ui.View):
    def __init__(self):
        super().__init__(timeout= 180)
        self.add_item(pick_hero())
@bot.command()
async def pick(ctx):
    db = hero_data()
    uid = str(ctx.author.id)
    ensure_hero_profile(db, uid)
    lv1, _ = get_hero_progress(db, uid, 1)
    lv2, _ = get_hero_progress(db, uid, 2)
    lv3, _ = get_hero_progress(db, uid, 3)
    embed= discord.Embed(
        title= "Wao Xin Chào Đại Sư Huynh, Huynh muốn chọn tướng nào vậy ?",
        description= (
            "**Hiện tại chốn này đang sở hữu các đại tướng:**\n"
            f"`1.` **Sát Thủ** (cấp **{lv2}**) - sát thủ thầm lặng, damage scale nhanh.\n"
            f"`2`. **Đấu Sĩ** (cấp **{lv1}**) - công thủ toàn diện, phòng thủ scale tốt.\n"
            f"`3`. **Pháp Sư** (cấp **{lv3}**) - sát thương phép + khống chế.\n\n"
            "*Dạ xin mời đại sư huynh chọn tướng ạ =))*"
        ),
        color= 0xFFC0CB
    )
    await ctx.send(embed=embed, view= pick_hero_view())


def remove_item_from_inventory(user_id: int, item_name: str, quantity: int = 1) -> bool:
    inv = load_inventory()
    uid = str(user_id)
    if quantity <= 0:
        return False
    if uid not in inv:
        return False
    if item_name not in inv[uid]:
        return False

    current_qty = int(inv[uid][item_name].get("quantity", 0) or 0)
    if current_qty < quantity:
        return False

    inv[uid][item_name]["quantity"] = current_qty - quantity
    if inv[uid][item_name]["quantity"] <= 0:
        del inv[uid][item_name]
    if not inv[uid]:
        del inv[uid]
    save_inventory(inv)
    return True


def event_item_exp_value(item_info: dict) -> int:
    price = int(item_info.get("price", 0) or 0)
    return max(1, math.ceil(price / 50))


class UpgradeItemSelect(discord.ui.Select):
    def __init__(self, user_id: int):
        self.user_id = user_id
        user_inv = get_user_inventory(user_id)
        options: list[discord.SelectOption] = []
        for item_name, info in list(user_inv.items())[:25]:
            qty = int(info.get("quantity", 1) or 1)
            exp_gain = event_item_exp_value(info)
            options.append(
                discord.SelectOption(
                    label=item_name[:100],
                    description=f"x{qty} | +{exp_gain} EXP",
                    value=item_name,
                )
            )

        if not options:
            options.append(
                discord.SelectOption(
                    label="(Không có vật phẩm)",
                    description="Hãy vào hội trợ để mua vật phẩm",
                    value="__no_items__",
                )
            )

        placeholder = "Chọn vật phẩm để nâng cấp..." if user_inv else "Bạn chưa có vật phẩm nào"
        super().__init__(
            placeholder=placeholder,
            options=options,
            min_values=1,
            max_values=1,
            disabled=(len(user_inv) == 0),
        )

    async def callback(self, interaction: discord.Interaction):
        view = self.view  # type: ignore
        view.selected_item_name = self.values[0]  # type: ignore
        await view.refresh(interaction)  # type: ignore


class UpgradeHeroView(discord.ui.View):
    def __init__(self, author_id: int):
        super().__init__(timeout=180)
        self.author_id = author_id
        self.selected_item_name: Optional[str] = None
        self.add_item(UpgradeItemSelect(author_id))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.author_id:
            await interaction.response.send_message("Bạn không thể dùng menu này!", ephemeral=True)
            return False
        return True

    def build_embed(self, user_id: int) -> discord.Embed:
        hero_db = hero_data()
        uid = str(user_id)
        ensure_hero_profile(hero_db, uid)
        hero_id = int(hero_db[uid].get("hero", 0) or 0)
        level, exp = get_hero_progress(hero_db, uid, hero_id)
        cost = hero_next_level_cost(level)

        inv = get_user_inventory(user_id)
        total_items = sum(int(info.get("quantity", 1) or 1) for info in inv.values())

        desc = (
            "*Tại đây sư huynh có thể nâng cấp tướng mà sư huynh đã chọn*.\n"
            f"Tướng hiện tại: **{_hero_name(hero_id)}**\n"
            f"Cấp: **{level}** (EXP: **{exp}/{cost}**)\n"
            f"HP tối đa (khi fight): **{hero_effective_max_hp(hero_id, level)}**\n\n"
            f"Vật phẩm Hội Trợ Hè trong túi: **{total_items}**\n"
            f"Chọn 1 vật phẩm rồi nhấn **Nâng cấp** để dùng."
        )

        if self.selected_item_name:
            info = inv.get(self.selected_item_name)
            if info:
                exp_gain = event_item_exp_value(info)
                qty = int(info.get("quantity", 1) or 1)
                desc += (
                    f"\n\nĐã chọn: **{self.selected_item_name}** (còn **x{qty}**)"
                    f"\nDự kiến nhận: **+{exp_gain} EXP**"
                )
            else:
                desc += "\n\nĐã chọn: (vật phẩm không còn trong túi)"

        embed = discord.Embed(
            title="Chào mừng đại sư huynh đến sảnh nâng cấp tướng",
            description=desc,
            color=0x38EBE2,
        )
        embed.set_footer(text="Dùng vật phẩm đã mua trong hội trợ")
        return embed

    async def refresh(self, interaction: discord.Interaction) -> None:
        embed = self.build_embed(interaction.user.id)
        self.upgrade_btn.disabled = not bool(self.selected_item_name)
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="Nâng cấp", style=discord.ButtonStyle.success, disabled=True)
    async def upgrade_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        user_id = interaction.user.id
        uid = str(user_id)

        hero_db = hero_data()
        ensure_hero_profile(hero_db, uid)
        hero_id = int(hero_db[uid].get("hero", 0) or 0)
        if hero_id not in HERO_KIT:
            await interaction.response.send_message("Bạn chưa chọn tướng. Dùng `eiupick` trước nhé.", ephemeral=True)
            return

        level, exp = get_hero_progress(hero_db, uid, hero_id)

        if level >= MAX_HERO_LEVEL:
            await interaction.response.send_message(f"Tướng của bạn đã đạt cấp tối đa (**{MAX_HERO_LEVEL}**).", ephemeral=True)
            return

        if not self.selected_item_name:
            await interaction.response.send_message("Bạn chưa chọn vật phẩm.", ephemeral=True)
            return

        inv = get_user_inventory(user_id)
        info = inv.get(self.selected_item_name)
        if not info or int(info.get("quantity", 0) or 0) <= 0:
            await interaction.response.send_message("Vật phẩm này không còn trong túi.", ephemeral=True)
            return

        exp_gain = event_item_exp_value(info)

        if not remove_item_from_inventory(user_id, self.selected_item_name, quantity=1):
            await interaction.response.send_message("Không thể trừ vật phẩm (có thể bạn vừa dùng ở nơi khác).", ephemeral=True)
            return

        exp += exp_gain
        leveled_up = 0
        while level < MAX_HERO_LEVEL:
            need = hero_next_level_cost(level)
            if exp < need:
                break
            exp -= need
            level += 1
            leveled_up += 1

        set_hero_progress(hero_db, uid, hero_id, level, exp)
        luu_hero(hero_db)

        result = discord.Embed(
            title="🔥 Nâng cấp thành công",
            description=(
                f"Bạn đã dùng **{self.selected_item_name}** và nhận **+{exp_gain} EXP**.\n"
                + (f"🎉 Lên **{leveled_up}** cấp!\n" if leveled_up > 0 else "")
                + f"Tướng: **{_hero_name(hero_id)}**\n"
                + f"Cấp hiện tại: **{level}** (EXP: **{exp}/{hero_next_level_cost(level)}**)\n"
                + f"HP tối đa (khi fight): **{hero_effective_max_hp(hero_id, level)}**"
            ),
            color=discord.Color.green(),
        )
        result.set_footer(text="Cảm ơn sư huynh đã tin tưởng dịch vụ nâng cấp tướng của muội=))")

        self.selected_item_name = None
        for child in list(self.children):
            if isinstance(child, UpgradeItemSelect):
                self.remove_item(child)
        self.add_item(UpgradeItemSelect(self.author_id))
        self.upgrade_btn.disabled = True

        await interaction.response.edit_message(embed=result, view=self)


@bot.command(name="up", aliases=["nangcaptuong"])
@commands.cooldown(1, 10, commands.BucketType.user)
async def up(ctx):
    hero_db = hero_data()
    uid = str(ctx.author.id)
    ensure_hero_profile(hero_db, uid)
    hero_id = int(hero_db[uid].get("hero", 0) or 0)
    if hero_id not in HERO_KIT:
        await ctx.send(f"{ctx.author.mention} chưa chọn tướng. Dùng `eiupick` trước nhé.")
        return

    inv = get_user_inventory(ctx.author.id)
    if not inv:
        await ctx.send("Bạn chưa có vật phẩm nào để nâng cấp. Hãy vào hội trợ (`eiuevent`) để mua trước nhé.")
        return

    view = UpgradeHeroView(author_id=ctx.author.id)
    embed = view.build_embed(ctx.author.id)
    await ctx.send(embed=embed, view=view)


@up.error
async def nangcap_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Chờ thêm **{int(error.retry_after)}s** nữa mới dùng lại được")

mon_hoc= ["Toán", "Vật lý", "Ngữ văn", "Hóa học", "Sinh học", "Tin học", "Tiếng anh", "Lịch sử", "Địa lí", "Kinh tế pháp luật", "Quốc phòng an ninh", "Công nghệ"]

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def dailystudy(ctx):
    hom_nay_hoc_gi= random.choice(mon_hoc)
    await ctx.send(f"Yes sir, hôm nay bạn sẽ phải học môn {hom_nay_hoc_gi}:)))")
@dailystudy.error
async def dailystudy_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Chờ thêm **{int(error.retry_after)}s** nữa mới dùng lại được")


@bot.tree.command(name= "makeqr", description= "Tạo mã QR từ link")
@app_commands.describe(url="Đường link cần tạo QR")
async def makeqr(interaction: discord.Interaction, url:str):
    buffer = io.BytesIO()

    img = qrcode.make(url)
    img.save(buffer, format="PNG")
    buffer.seek(0)

    file = discord.File(buffer, filename="qrcode.png")

    embed = discord.Embed(
        title="QR của bạn đây",
        description= f"**Link:** {url}",
        color=0x38EBE2
    )
    embed.set_image(url="attachment://qrcode.png")
    await interaction.response.send_message(embed=embed, file=file)



@bot.tree.command(name= "weather", description= "Xem thời tiết tại một thành phố")
@app_commands.describe(city="Nhập tên thành phố (vd: Hà Nội, Tokyo)")
async def weather(interaction: discord.Interaction, city: str):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric&lang=vi"
    )

    res = requests.get(url)
    data = res.json()

    if data.get("cod") != 200:
        await interaction.response.send_message("Không tìm thấy thành phố")
        return

    temp = data["main"]["temp"]
    feels = data["main"]["feels_like"]
    desc = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    embed = discord.Embed(
        title=f"🌤 Thời tiết tại {city}",
        color= 0x38EBE2
    )
    embed.add_field(name="🌡 Nhiệt độ", value=f"{temp}°C")
    embed.add_field(name="🤔 Cảm giác như", value=f"{feels}°C")
    embed.add_field(name="💧 Độ ẩm", value=f"{humidity}%")
    embed.add_field(name="📄 Trạng thái", value=desc.capitalize())
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name= "avatar", description= "Xem avatar của người bạn muốn xem")
@app_commands.describe(member= "Người bạn muốn xem avatar")
async def avatar(interaction:discord.Interaction, member: discord.Member):
    avatar= member.avatar
    embed= discord.Embed(
        title= f"{member.name} avatar",
        color= 0x38EBE2
    )
    embed.set_image(url= avatar)
    await interaction.response.send_message(embed=embed)



@bot.tree.command(name= "lookup_tiktok", description= "Xem info tài khoản TikTok của bạn")
@app_commands.describe(username= "Bạn muốn xem kênh TikTok nào ?")
async def tiktok(interaction: discord.Interaction, username: str):
    data= get_tiktok_info(username)
    if isinstance(data, str):
        await interaction.response.send_message(data)
        return
    embed = discord.Embed(title=data["nickname"], color= 0x38EBE2)
    embed.set_image(url= data["avatar"])

    embed.add_field(name="Followers", value=data["followers"])
    embed.add_field(name="Following", value=data["following"])
    embed.add_field(name="Likes", value=data["likes"])
    embed.add_field(name="Bio", value=data["bio"], inline=False)
    await interaction.response.send_message(embed=embed)
bot.run("Bot token")