
from models.Climbers import Climbers
from models.Model import Model
climber = Climbers()
climber.get()
for row, list in enumerate(climber.get()):
    print(row, ' - ', list)
#climber = Model()
#print(climber.get('Climbers'))

climber.add()


#climber.update()

for row, list in enumerate(climber.get()):
    print(row, ' - ', list)

