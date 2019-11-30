from policeScraper.policeScraper import PoliceScraper
from policeDB.databaseLoader import DatabaseLoader

policeScraper = PoliceScraper();
databaseLoader = DatabaseLoader("localhost", "root", 3306, "root", "mysql")


scrap_dict = policeScraper.scrap_period("24-8-2019", "25-11-2019")
databaseLoader.upload_into_db(scrap_dict)
