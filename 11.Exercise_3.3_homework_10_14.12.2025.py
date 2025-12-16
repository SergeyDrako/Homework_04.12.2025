from abc import ABC, abstractmethod
class BaseTestCase(ABC):
    @abstractmethod
    def prepare_data(self):
        def run_test(self):
               pass

    def run(self):
        self.prepare_data()
        self.run_test()

class LoginTest(BaseTestCase):
    def prepare_data(self):
        print('Готовим пользователя для логина')
    def run_test(self):
        print('Проверяем успешный логин')


class PaymentTest(BaseTestCase):
    def prepare_data(self):
        print('Готовим данные карты и баланс')

    def run_test(self):
        print('Проверяем успешный платеж')

tests = [LoginTest(), PaymentTest()]
for t in tests:
    t.run()
