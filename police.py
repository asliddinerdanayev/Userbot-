#by #Prosta_Umid
from .. import loader
from asyncio import sleep
@loader.tds
class HeartsMod(loader.Module):
	strings = {"name": "Police"}
	@loader.owner
	async def policecmd(self, message):
		for _ in range(12):
			for police in ['❤️❤️❤️❤️🤍🤍🤍💙💙💙💙\n❤️❤️❤️❤️🤍🤍🤍💙💙💙💙\n❤️❤️❤️❤️🤍🤍🤍💙💙💙💙','💙💙💙💙🤍🤍🤍❤️❤️❤️❤️\n💙💙💙💙🤍🤍🤍❤️❤️❤️❤️\n💙💙💙💙🤍🤍🤍❤️❤️❤️❤️']:
				await message.edit(police)
				await sleep(0.3)
