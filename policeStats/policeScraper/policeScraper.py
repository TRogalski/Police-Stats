import datetime
import requests
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import numpy as np

class PoliceScraper():
    def getDates(self, start, end):
        
        start_dt = datetime.datetime.strptime(start, '%d-%m-%Y')
        end_dt = datetime.datetime.strptime(end, '%d-%m-%Y')
        step = datetime.timedelta(days = 1)
        
        series = []
        
        while start_dt < end_dt:
            series.append(start_dt)
            start_dt += step   
        return series;
        
    def formatDate(self, date):
        return date.strftime('%d%m%Y')
    
    def scrap_day(self, date):
        daily_stats = {}
        
        try:
            response = requests.get('http://malopolska.policja.gov.pl/pl/content/' + self.formatDate(date))
            html_soup = BeautifulSoup(response.content, 'html.parser');
            bs_daily_stats = html_soup.find("article", {"class" : "node-statystyka-dnia"}).findAll("dd")
            
            for element in bs_daily_stats:
                daily_stats[element['title']] = int(element.div.get_text())
            return daily_stats
        except (HTTPError, AttributeError) as e:
            #Errors should be logged somehow
            print(e)
            return {'Zatrzymani na gorącym uczynku': None,
                    'Zatrzymani poszukiwani': None, 
                    'Zatrzymani nietrzeźwi kierujący': None, 
                    'Wypadki drogowe': None, 
                    'Zabici w wypadkach drogowych': None, 
                    'Ranni w wypadkach drogowych': None}

    def scrap_period(self, start_dt, end_dt):
        period_stats = {}
        dates = self.getDates(start_dt, end_dt)
        
        for date in dates:
            period_stats[date.strftime('%d-%m-%Y')] = self.scrap_day(date)
        return period_stats
