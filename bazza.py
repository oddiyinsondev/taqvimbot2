from aiogram.dispatcher.filters.state import State, StatesGroup

class Register(StatesGroup):
    first_name = State()
    last_name = State()
    phone_number = State()
    admin = State()



