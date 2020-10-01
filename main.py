from telethon.sync import TelegramClient
from telethon import events
import asyncio
from telethon.sessions import StringSession
from telethon import events
from constants import CMD_PREFIX
from constants import API_HASH, API_ID, SESSION_KEY
import time

poke_list = ['Zygarde', 'Cosmog', 'Cosmoem', 'Solgaleo', 'Lunala', 'Necrozma', 'Magearna', 'Marshadow'
, 'Greninja', 'Sylveon', 'Xerneas', 'Yveltal', 'Talonflame', 'Moltres', 'Charizard', 'Dragonite'
, 'Alakazam', 'Ninjask', 'Shedinja', 'Snorlax', 'Mawile', 'Aerodactyl', 'Hoopa',  'Tyranitar', 'Hydreigon', 'Kangaskhan'
]

#Thanks Anil Vro
with TelegramClient(StringSession(SESSION_KEY), API_ID, API_HASH,) as client:


    @client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "hexamatch (.*) (\w+)"))
    async def hexamatch(event):
        bid = 572621020
        msg = "/hunt"
        times_hunt = event.pattern_match.group(1)
        set_sec = event.pattern_match.group(2)
        eta = int((int(times_hunt) * int(set_sec))/60)
        if not times_hunt.isnumeric():
            text = "`Onii-sama nHunts and nSex both must be integers :)`"
            await event.edit(text)
        else:
            await event.edit("`Aye aye Captain... `"
                            "\n`Started hunting right away on yer command 🤠`"
                            f"\n\n`Will be hunting {times_hunt} times. Each one of 'em in {set_sec} seconds.`"
                            f"\n\n`I will stop the hunting if I encounter any pokemon from the list.`"
                            f"\n\n`ETA for this hunt is around: {eta} minutes.`")
            async with client.conversation('Hexamonbot') as conv:
                for i in range(int(times_hunt)):
                    await conv.send_message('/hunt')
                    if int(i) == int(times_hunt)-1:
                        await event.reply("`Hunting complete.`")
                    else:
                        poke_r = await conv.get_response()
                        get_res_msg = poke_r.text.split(" ")
                        get_poke_n = get_res_msg[2].replace("**","") 
                        
                        if get_poke_n in poke_list:
                            print(f'In list: {get_poke_n}')
                            await event.reply(f"Master, {get_poke_n} has appeared. Let\'s catch it.")  
                            break
                        else:
                            time.sleep(int(set_sec))
        
    @client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "hexa (.*) (\w+)"))
    async def hexa(event):
        bid = 572621020
        msg = "/hunt"
        times_hunt = event.pattern_match.group(1)
        set_sec = event.pattern_match.group(2)
        eta = int((int(times_hunt) * int(set_sec))/60)
        if not times_hunt.isnumeric():
            text = "`Onii-sama nHunts and nSex both must be integers :)`"
            await event.edit(text)
        else:
            await event.edit("`Aye aye Captain... `"
                            "\n`Started hunting right away on yer command 🤠`"
                            f"\n\n`Will be hunting {times_hunt} times. Each one of 'em in {set_sec} seconds.`"
                            f"\n\n`ETA for this hunt is around: {eta} minutes.`")
            for i in range(int(times_hunt)):
                await client.send_message(bid,msg)
                if int(i) == int(times_hunt)-1:
                    await event.reply("`Hunting complete.`")
                else:
                    time.sleep(int(set_sec))

    @client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "list"))
    async def list(event):
        await event.reply(f"`{poke_list}`")

    client.run_until_disconnected()