from models.Ascents import Ascents
from models.Mountains import Mountains
from models.Regions import Regions
from models.Climbers import Climbers
from models.Model import Model

ascents = Ascents()
#climber = Climbers()
#regions = Regions()
#mountains = Mountains()

# for row, list in enumerate(climber.get()):
#     print(row, ' - ', list)

#for row, list in enumerate(regions.get()):
#    print(row, ' - ', list)

#for row, list in enumerate(mountains.get()):
#    print(row, ' - ', list)

for row, list in enumerate(ascents.get()):
    print(row, ' - ', list)

ascents.add()

for row, list in enumerate(ascents.get()):
    print(row, ' - ', list)
