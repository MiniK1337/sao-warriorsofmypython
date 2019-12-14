import random
from time import sleep

anime = dict(
  title = "Sword Art Online: Warriors of my Python",
  type = "OVA",
  dubtype = "Полный дубляж",
  voices_count = 9,
  voices = [
    "Reform",
    "fieryrage",
    "SquareTude",
    "Sotarks",
    "Nevo",
    "monstrata",
    "Alumetri",
    "Fatfan Kolek",
    "MaximBogdan",
  ],
  dub = "Sotarks PP Studio",
  episodes_count = 2
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
    sleep(random.randint(1,6))

def calculate():
    print("Расчет полей...")
    sleep(random.randint(1,6))

def paint():
    print("Отрисовка персонажей...")
    sleep(random.randint(1,6))

def loadWorld():
    print("Загрузка мира...")
    sleep(random.randint(1,6))

def genPlot(plot=_plot):
  out = []
  while len(out) != len(_plot):
      r = random.choice(_plot)
      if r not in out:
          out.append(r)
  return "\n".join(out)

def renderAnime(plot, renderer=True):
  RENDERER_MAIN = random.randint(0, 99400)
  for i in plot.split("\n"):
    print("Загрузка сюжетной линии \"{}\"".format(i))
    sleep(random.randint(1,6))
  print("Сюжетные линии загружены и готовы к рендеру")

  if RENDERER_MAIN and RENDERER_MAIN > 44100:
    return False
  else:
    return True


def animeLoad():
  return "Аниме успешно загружено, приятного просмотра"


print("Генерация аниме")
print(f"Название - {anime['title']}")
print(f"Серии - {anime['episodes_count']}")
print(f"Озвучка - {anime['dub']} ({anime['dubtype']})")
print(f"Тип - {anime['type']}")
print("Озвучили:")
for i in anime['voices']:
  print("     " + i)
  print(f"В серии будет {len(_plot)} событий")

def main():
  print("Просчет событий...")
  sleep(random.randint(1,6))

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


if __name__ == "__main__":
  main()
