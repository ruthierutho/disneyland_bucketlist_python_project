import pdb
from models.park import Park

from repositories import park_repository

park1 = Park("Magic Kingdom")
park_repository.save(park1)

park2 = Park("Disney Studios")
park_repository.save(park2)


pdb.set_trace()