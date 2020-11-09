import pdb
from models.park import Park
from models.land import Land
from models.attraction import Attraction

from repositories import park_repository
from repositories import land_repository
from repositories import attraction_repository

attraction_repository.delete_all()
land_repository.delete_all()
park_repository.delete_all()

park1 = Park("Magic Kingdom")
park_repository.save(park1)

park2 = Park("Disney Studios")
park_repository.save(park2)


pdb.set_trace()