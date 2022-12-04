from create_bot import dp
from aiogram.utils import executor
from handlers import fsm_client, admin


fsm_client.register_handlers_client(dp)
admin.register_handlers_admin(dp)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)