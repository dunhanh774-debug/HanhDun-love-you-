import discord
from discord.ext import commands
import qrcode
import io
class MakeQR(commands.Cog):
    def __init__(self,bot):
        self.bot= bot
    @commands.command()
    async def makeqr(ctx, url: str):
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
        await ctx.send(embed=embed, file=file)
async def setup(bot):
    await bot.add_cog(MakeQR(bot))