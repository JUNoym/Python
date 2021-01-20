# コマンドライン引数
# import lesson_package.utils
from lesson_package import utils
import sys

print(sys.argv)

for i in sys.argv:
    print(i)

r = utils.say_twice('helll')
print(r)
