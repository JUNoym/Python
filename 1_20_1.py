# クラスの継承
class Car(object):
    def run(self):
        print('他のクラスに継承したいメソッド')


class ToyotaCar(Car):
    pass  # 何もしないという意味


class TeslaCar(Car):
    def auto_run(self):
        print('テスラの独自のメソッド')


car = Car()
car.run()
print('########################')
toyota_car = ToyotaCar()
toyota_car.run()
print('########################')
tesla_car = TeslaCar()
tesla_car.auto_run()
tesla_car.run()
