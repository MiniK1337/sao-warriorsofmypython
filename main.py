import random
from threading import Thread, enumerate
from time import sleep
from helpers import *

anime = dict(
  title = "Sword Art Online: Warriors of my Python",
  type = "OVA",
  dubtype = "Полный дубляж",
  voices_count = 12,
  voices = [
    "Reform",
    "fieryrage",
    "SquareTude",
    "Sotarks",
    "Nevo",
    "monstrata",
    "Alumetri",
    #"Fatfan Kolek", #он сказал что ему это больше не интересно
    "MaximBogdan",
    "Keijia", #ура новые голоса в аниме
    "SweetDream",
    #"Gasha", #он разбился на машине, подробнее - https://vk.com/wall-188841623_269
    "firedigger", #ура, он воскрес! https://vk.com/wall-188841623_412
    "karthy", #озвучивать ему будет сложно, он попал в тюрьиу - https://vk.com/wall-188841623_420 . Будем бороться за его высвобождение, наша команда уверена, что он не виноват
  ],
  dub = "Sotarks PP Studio",
  episodes_count = 3
)

_plot = [
  "Битва с союзником",
  "Бег персонажа куда то",
  "Пафосная фраза",
  "Спасение какого-то долбаеба",
  "Защита какой-то деревни",
  "Повторение опенинга (драматичный момент)",
  "Смерть друга гг",
  "Предыстория",
  "Флешбеки из реальной жизни",
  "Спасение человека",
  "ФАрм ЛеСА",
  "стакаем на 50 минуте пацаны и идем пушить",
  "ZXC",
  "Закуп двух сапогов и осознание того что они не стакаются",
  "Рекламная пауза (10 минута аниме)"
]

def generateLandshaft():
    print("Генерация ландшафта...")
    sleep(random.randint(1, 6))

def calculate():
    print("Расчет полей...")
    sleep(random.randint(1, 6))

def paint():
    print("Отрисовка персонажей...")
    sleep(random.randint(1, 6))

def loadWorld():
    print("Загрузка мира...")
    sleep(random.randint(1, 6))

def genPlot(plot=_plot):
  out = []
  while len(out) != len(_plot):
      r = random.choice(_plot)
      if r not in out:
          out.append(r)
  return "\n".join(out)

def renderAnime(plot, renderer=True):
    RENDERER_MAIN = random.randint(0, 99400)
    print("Запуск потоков обработки...")
    for i in plot.split("\n"):
        print(f"Обработка сюжетной линии \"{i}\"")
        multi_loader_thread(RENDERER_MAIN - 44100, i)
    while len(enumerate()) != 1:
        pass
    print("Сюжетные успешно отработаны и готовы к рендеру")

    if RENDERER_MAIN and RENDERER_MAIN > 44100:
        return False
    else:
        return True


def animeLoad():
  return "Аниме успешно загружено, приятного просмотра"

def main():
  print("Просчет событий...")
  sleep(random.randint(1, 10))

  plot = genPlot()

  print("Сгенерирован сюжет")

  print("Рендеринг...")

  renderer_main = renderAnime(plot)

  if renderer_main:
      generateLandshaft()
      calculate()
      paint()
      loadWorld()
      print("Рендер аниме успешен")

      return print(animeLoad())
  else:
    print("Рендеринг завершился с ошибкой, вероятно, произошли несостыковки сюжетных линий")
    print("Начинаем процесс заново")
    return main()

def multi_loader_thread(renderer, line):
    try:
        while renderer:
            for i in range(random.randint(100, 1000)):
                continue
            break

        t = Thread(target=threadHelper, args=[line])
        t.start()

        if not renderer:
            raise

        return "Поток успешно запущен"
    except:
        return "Поток успешно запущен в режиме совместимости"

if __name__ == "__main__":
    print("Генерация аниме")
    print(f"Название - {anime['title']}")
    print(f"Серии - {anime['episodes_count']}")
    print(f"Озвучка - {anime['dub']} ({anime['dubtype']})")
    print(f"Тип - {anime['type']}")
    print("Озвучили:")
    for i in anime['voices']:
        print(" " * 4 + i)
    print(f"В серии будет {len(_plot)} событий")
    main()
    input()
