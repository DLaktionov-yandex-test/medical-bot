from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types
from callbacks import DrugCallBackFactory


def drug_keyboard(drugs):
    builder = InlineKeyboardBuilder()
    sizes = []
    for drug in drugs:
        builder.button(text=drug, callback_data=DrugCallBackFactory(drug_id=1, action="show"))
        builder.button(text="✏️", callback_data=DrugCallBackFactory(drug_id=1, action="edit"))
        builder.button(text="✖️", callback_data=DrugCallBackFactory(drug_id=1, action="remove"))
        sizes += [1, 2]
    builder.button(text="Добавить", callback_data=DrugCallBackFactory(drug_id=0, action="add"))   
    builder.adjust(*sizes, 1)
    return builder.as_markup()