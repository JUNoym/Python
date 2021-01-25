# プロパティーを使った属性の設定
class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('Carのメソッド')


class ToyotaCar(Car):
    def run(self):
        print('fast')


class TeslaCar(Car):
    def __init__(self, model='Model S', enable_auto_run=False):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run  # _をつけている

    @property  # こうすることで読み込みはできるけど設定はできない
    def enable_auto_run(self):
        return self._enable_auto_run

    def run(self):
        print('super fast')

    def auto_run(self):
        print('テスラ独自のメソッド')


# toyota_car = ToyotaCar('レクサス')
# print(toyota_car.model)

tesla_car = TeslaCar('電気自動車')
# print(tesla_car.model)
# 勝手にオブジェクトが生成されて値が変更されている　それを避けるためにプロパティーを使う
tesla_car.enable_auto_run = True　  # _がついてデコレータもついてるので値を変更できない
print(tesla_car.enable_auto_run)
