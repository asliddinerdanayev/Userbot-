

from .. import loader, utils

from telethon.errors.rpcerrorlist import MessageNotModifiedError

import logging
import asyncio

logger = logging.getLogger(__name__)


@loader.tds
class TyperMod(loader.Module):
    """Xabarlarni yozishni sekinlashtiradi"""
    strings = {"name": "Typewriter",
               "no_message": "<b>( ꈍᴗꈍ) Hech narsa yoza olmaysiz!</b>",
               "type_char_cfg_doc": "¯\_(ツ)_/¯ Yozuv mashinkasi uchun belgi koʻrsating",
               "delay_typer_cfg_doc": "Yozuv mashinkasi xarakterini ko'rsatishni qancha vaqt kechiktirish kerak",
               "delay_text_cfg_doc": "Matnni ko'rsatishni qancha vaqt kechiktirish kerak?"}

    def __init__(self):
        self.config = loader.ModuleConfig("TYPE_CHAR", "░", "░", lambda m: self.strings("type_char_cfg_doc", m),
                                          "DELAY_TYPER", 0.02, lambda m: self.strings("delay_typer_cfg_doc", m),
                                          "DELAY_TEXT", 0.1, lambda m: self.strings("delay_text_cfg_doc", m))

    @loader.ratelimit
    async def typecmd(self, message):
        """.type <message>"""
        a = utils.get_args_raw(message)
        if not a:
            await utils.answer(message, self.strings("no_message", message))
            return
        m = ""
        entities = message.entities or []
        for c in a:
            m += self.config["TYPE_CHAR"]
            message = await update_message(message, m, entities)
            await asyncio.sleep(0.04)
            m = m[:-1] + c
            message = await update_message(message, m, entities)
            await asyncio.sleep(0.02)


async def update_message(message, m, entities):
    try:
        return await utils.answer(message, m, parse_mode=lambda t: (t, entities))
    except MessageNotModifiedError:
        return message
