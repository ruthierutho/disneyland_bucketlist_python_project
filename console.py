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

park1 = Park("Disneyland Park")
park_repository.save(park1)
park2 = Park("Walt Disney Studios Park")
park_repository.save(park2)

land1 = Land("Fantasyland", park1, True)
land_repository.save(land1)
land2 = Land("Discoveryland", park1, False)
land_repository.save(land2)
land3 = Land("Toon Studio", park2, False)
land_repository.save(land3)
land4 = Land("Adventureland", park1, False)
land_repository.save(land4)
land5 = Land("Production Courtyard", park2, False)
land_repository.save(land5)

attraction1 = Attraction("It's a small world", land1, True, "So cute!")
attraction_repository.save(attraction1)
attraction2 = Attraction("Space Mountain", land2, False, "Bit scared!")
attraction_repository.save(attraction2)
attraction3 = Attraction("Peter Pan's Flight", land1, False, "So excited for this!")
attraction_repository.save(attraction3)
attraction4 = Attraction("Crush's Coaster", land3, False, "Looks awesome!")
attraction_repository.save(attraction4)



pdb.set_trace()