import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

TOKEN = '1739338543:AAEwkcEXLAVv_jZ5SJhNHnv-WbUEkP2zEV4'
memory_storage = MemoryStorage()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot,storage=memory_storage)
logging.basicConfig(level=logging.INFO)