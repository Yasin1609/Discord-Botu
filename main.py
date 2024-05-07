                      import discord
from discord.ext import commands
import os, random
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

rastgele_numara = random.randint(1, 999)  # Rastgele sayıyı burada tanımlayalım

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def merhaba(ctx):
    await ctx.send("Selam ben bir botum!")

@bot.command()
async def bye(ctx):
    await ctx.send("🖐️")

@bot.command()
async def rastgele_sayı(ctx):
    global rastgele_numara  # Rastgele sayıyı global olarak kullanabilmek için
    rastgele_numara = random.randint(1, 999)  # Yeni bir rastgele sayı oluşturalım
    await ctx.send(f"Tabii ki!, İşte: {rastgele_numara}")

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)

@bot.command()
async def tahmin(ctx):
    sayi = random.randint(1, 100)
    await ctx.send("1 ile 100 arasında bir sayı tahmin et!")
    
    def kontrol(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content.isdigit()

    tahmin = await bot.wait_for('message', check=kontrol)

    tahmin = int(tahmin.content)
    if tahmin == sayi:
        await ctx.send("Tebrikler, doğru tahmin ettiniz!")
    else:
        await ctx.send(f"Üzgünüm, doğru cevap {sayi} idi.")
    
@bot.command()
async def tarih(ctx):
    simdiki_zaman = datetime.now()
    tarih = simdiki_zaman.strftime("%d/%m/%Y")
    await ctx.send(f"Bugünün tarihi: {tarih}")

@bot.command()
async def saat(ctx):
    simdiki_zaman = datetime.now()
    saat = simdiki_zaman.strftime("%H:%M:%S")
    await ctx.send(f"Şu an saat: {saat}")

@bot.command()
async def kuresel_bilgi(ctx):
    bilgi_mesajı = (
        "Küresel ısınma, dünya genelindeki atmosferdeki ve okyanuslardaki sıcaklık artışını ifade eder. "
        "Bu artışın nedenleri arasında fosil yakıtların yanması, ormansızlaşma ve endüstriyel faaliyetler yer alır. "
        "Küresel ısınmanın etkileri arasında buzulların erimesi, deniz seviyelerinin yükselmesi, "
        "ekosistemlerde değişiklikler ve daha sık ve şiddetli doğal afetler bulunur. "
        "Küresel ısınmayı önlemek için ise yenilenebilir enerji kullanımı teşvik edilmeli, "
        "ormansızlaşma engellenmeli ve enerji verimliliği artırılmalıdır."
    )
    await ctx.send(bilgi_mesajı)

@bot.command()
async def ipuclari(ctx):
    ipuclari_mesajı = (
        "Küresel ısınmayı önlemek için yapabileceğiniz bazı ipuçları şunlardır:\n"
        "- Evlerinizi ve iş yerlerinizi enerji verimli hale getirin.\n"
        "- Fosil yakıtların kullanımını azaltın ve yenilenebilir enerji kaynaklarını tercih edin.\n"
        "- Sürdürülebilir ulaşım yöntemlerini tercih edin (yürüyüş, bisiklet, toplu taşıma).\n"
        "- Atıkları azaltın, geri dönüşüm yapın ve çevreye zararlı kimyasallardan kaçının.\n"
        "- Daha az et tüketin ve yerel ve organik gıdaları tercih edin."
    )
    await ctx.send(ipuclari_mesajı)

@bot.command()
async def etkinlikler(ctx):
    etkinlikler_mesajı = (
        "Çevre dostu etkinlikler yaparak küresel ısınmayı önlemeye katkıda bulunabilirsiniz:\n"
        "- Orman temizliği ve fidan dikme etkinliklerine katılın.\n"
        "- Çevre temizliği etkinliklerine katılın ve çöpleri toplayın.\n"
        "- Çevre konulu seminerlere ve atölyelere katılın ve bilgi edinin.\n"
        "- Topluluk bahçelerine katılın ve organik tarımı destekleyin."
    )
    await ctx.send(etkinlikler_mesajı)
@bot.command()
async def tesekkurler(ctx):
    await ctx.send("rica ederim :)")

@bot.command()
async def hakkinda(ctx):
    botun_ozellikleri = (
        "**Komutlar:**\n"
        "`$rastgele_sayı`: 1 ile 100 arasında rastgele bir sayı seçer.\n"
        "`$mem`: Bir meme resmi gönderir.\n"
        "`$tahmin`: 1 ile 100 arasında bir sayı tahmin etmece oyunu.\n"
        "`$tarih`: Bugünün tarihini söyler.\n"
        "`$saat`: Şu anki saati söyler.\n"
        "`$kuresel_bilgi`: Küresel ısınma hakkında bilgi verir.\n"
        "`$ipucu`: Küresel ısınmayı önlemek için neler yapılabileceğini söyler.\n"
        "`$etkinlikler`: Küresel ısınmayı önlemek için yapılabilecek etkinlikler hakkında bilgi verir.\n"
    )
    await ctx.send(botun_ozellikleri)



bot.run("Token")     
