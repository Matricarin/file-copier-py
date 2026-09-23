# процесс журналирования

# класс представляет собой обертку для сбора журналов по приложению
# необходимо писать в один файл путь к которому указан в конструкторе
# методы определены асинхронными для корректному доступа к файлу 


class FileLog():
    
    def __init__(self, path):
        self.path = path
    
    async def log_error(message):
        ...
        
    async def log_debug(message):
        ...
    
    async def log_info(message):
        ...
        
    
        
    
    