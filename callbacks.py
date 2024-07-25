from aiogram.filters.callback_data import CallbackData

class DrugCallBackFactory(CallbackData, prefix="drugs"):
    drug_id:int
    action:str
