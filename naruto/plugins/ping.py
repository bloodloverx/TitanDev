from . import ping
@naruto.on_message(filters.command(filters.user(AdminSettings) & ("ping", Command))
async def_(_, message)
   await ping(_, message)
