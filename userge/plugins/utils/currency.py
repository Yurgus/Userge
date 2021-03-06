# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >
#
# All rights reserved.


from requests import get
from emoji import get_emoji_regexp
from userge import userge, Message, Config

CHANNEL = userge.getCLogger(__name__)


@userge.on_cmd("cr", about={
    'header': "use this to convert currency & get exchange rate",
    'description': "Convert currency & get exchange rates.",
    'examples': ".cr 1 BTC USD"})
async def cur_conv(message: Message):
    """
    this function can get exchange rate results
    """
    if Config.CURRENCY_API is None:
        await message.edit(
            "`Oops!!\nget the API from` (HERE)[https://free.currencyconverterapi.com] "
            "`& add it to Heroku config vars` (`CURRENCY_API`)", del_in=0)
        return

    filterinput = get_emoji_regexp().sub(u'', message.input_str)
    curcon = filterinput.upper().split()

    if len(curcon) == 3:
        amount, currency_to, currency_from = curcon
    else:
        await message.edit("`something went wrong!! do .help cr`")
        return

    if amount.isdigit():
        data = get(
            f"https://free.currconv.com/api/v7/convert?apiKey={Config.CURRENCY_API}&q={currency_from}_{currency_to}&compact=ultra"
            ).json()
        result = data[f'{currency_from}_{currency_to}']
        result = float(amount) / float(result)
        result = round(result, 5)
        await message.edit(
            "**CURRENCY EXCHANGE RATE RESULT:**\n\n"
            f"`{amount}` **{currency_to}** = `{result}` **{currency_from}**")
        await CHANNEL.log("`cr` command executed sucessfully")

    else:
        await message.edit(
            r"`This seems to be some alien currency, which I can't convert right now.. (⊙_⊙;)`"
            , del_in=0)
        return
