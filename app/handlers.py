import os
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from dotenv import load_dotenv


import app.keyboards as kb
import app.database.requests as rq

router = Router()

number = os.getenv("NUMBER")


@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer('Добро пожаловать в Autopaint09!🎨', reply_markup=kb.main)


@router.message(F.text == 'Услуги Autopaint09🚗')
async def catalog(message: Message):
    await message.answer('Выберите категорию ремонта🛠️', reply_markup=await kb.categories())
    
    
@router.message(F.text == 'Контакты ☎️')
async def catalog(message: Message):
    await message.answer(f'Номер телефона:{number}\nГрафик работы: "уточнять по номеру телефона"')

@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Выберите ремонт по категории',
                                  reply_markup=await kb.items(callback.data.split('_')[1]))
                                  
                                    
                                 


@router.callback_query(F.data.startswith('item_'))
async def category(callback: CallbackQuery):
    item_data = await rq.get_item(callback.data.split('_')[1])
    await callback.answer('Вы выбрали тип работ')
    await callback.message.answer(f'Название: {item_data.name}\nОписание:{item_data.description}\nЦена: {item_data.price}тг')
                                  
    
    
    
    
 
               