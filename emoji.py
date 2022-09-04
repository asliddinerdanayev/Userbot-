from .. import loader
from asyncio import sleep
@loader.tds
class HeartsMod(loader.Module):
	strings = {"name": "Emoji"}
	@loader.owner
	async def emojicmd(self, message):
		for _ in range(100):
			for police in ['😀','😃','😄','😁','😆','😅','😂','🤣','😭','😉','😗','😙','😚','😘','🥰','😍','🤩','🥳','🙃','🙂','🥲']:
				await message.edit(police)
				await sleep(0.3)
