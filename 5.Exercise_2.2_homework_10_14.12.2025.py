# class Logger:
#     def log(self, message):
#         print(f" [Log] {message}")
#
# class Senrvice:
#     def __int__(self, logger):
#         self.logger = logger
#     def process(self):
#         self.logger.log('Начал обработку')
#         print("Обработка данных")
#         self.logger.log('Закончил обработку')
#
# logger = Logger()
# service = Service(logger)
# service.process()
class Logger:
    def log(self, message):
        print(f" [Log] {message}")

class Service(Logger):
     def process(self):
        self.log('Начал обработку')
        print("Обработка данных")
        self.log('Закончил обработку')

service = Service()
service.process()




