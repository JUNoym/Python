# クラスの継承 メソッドのオーバーライド
class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('他のクラスに継承したいメソッド')


class ToyotaCar(Car):
    def run(self):
        print('fast')  # Carクラスから継承したメソッドもオーバーライドできる


class TeslaCar(Car):
    def __init__(self, model='Model S', enable_auto_run=False):
        # self.model = model
        super().__init__(model)  # 親の__init__を呼び出すことができる
        self.enable_auto_run = enable_auto_run

    def run(self):
        print('super fast')  # Carクラスから継承したメソッドもオーバーライドできる

    def auto_run(self):
        print('テスラの独自のメソッド')


car = Car()
car.run()
print('########################')
toyota_car = ToyotaCar('レクサス')
print(toyota_car.model)
toyota_car.run()
print('########################')
tesla_car = TeslaCar('Model S')
print(tesla_car.model)
tesla_car.auto_run()
tesla_car.run()
