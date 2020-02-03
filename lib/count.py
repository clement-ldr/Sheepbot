import aiohttp
import json
import logging as log

DISCORD_BOTS_API = 'https://bots.discord.pw/api'

class count:
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()

    def __unload(self):
        # pray it closes
        self.bot.loop.create_task(self.session.close())

    async def update(self):
        payload = json.dumps({
            "shard_id": self.bot.shard_id,
            "shard_count": self.bot.shard_count,
            "server_count": len(self.bot.servers)  
        })

        headers = {
            'authorization': '',
            'content-type': 'application/json'
        }

        url = '{0}/bots/{1.user.id}/stats'.format(DISCORD_BOTS_API, self.bot)
        async with self.session.post(url, data=payload, headers=headers) as resp:
            log.info('DBots statistics returned {0.status} for {1}'.format(resp, payload))

        headers2 = {
            'Authorization': '',
            'content-type': 'application/json'
        }
        url2 = 'https://discordbots.org/api/bots/{0.user.id}/stats'.format(self.bot)
        
        async with self.session.post(url2, data=payload, headers=headers2) as resp2:
            log.info('sitedebotdemerde returned {0.status} for {1}'.format(resp2, payload))

        
    async def on_server_join(self, server):
        await self.update()

    async def on_server_remove(self, server):
        await self.update()

    async def on_ready(self):
        await self.update()

def setup(bot):
    bot.add_cog(count(bot))
