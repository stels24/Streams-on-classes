from threading import Thread

import time


class Knight(Thread):

    def __init__(self, name, skill):

        Thread.__init__(self)
        self.Warriors = 100
        self.name = name
        self.skill = skill
        self.days_to_protect = self.Warriors // skill

    def run(self):
        print(f' {self.name} У нас не званные гости!!!')
        for day in range(self.days_to_protect):
            time.sleep(1)
            enemies_rest = self.Warriors - self.skill * (day + 1)
            print(f' {self.name} защищает крепость в течение {day + 1} дня(дней)... осталось {enemies_rest} воинов.')
            if enemies_rest == 0:
                print(f' {self.name} ликвидировал врагов спустя  {day + 1} день(дней).')


Knight1 = Knight('Sir Lancelot', 10) # Низкий уровень умения
Knight2 = Knight('Sir Galahad', 20) # Высокий уровень умения

Knight1.start()
Knight2.start()

Knight1.join()
Knight2.join()

print("Все битвы закончились!")