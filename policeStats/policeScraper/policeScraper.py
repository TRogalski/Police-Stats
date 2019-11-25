import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup

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
        html = urlopen('http://malopolska.policja.gov.pl/pl/content/' + self.formatDate(date))
        bs_page = BeautifulSoup(html);
        bs_daily_stats = bs_page.find("article", {"class" : "node-statystyka-dnia"}).findAll("dd")
        
        for element in bs_daily_stats:
            daily_stats[element['title']] = int(element.div.get_text())
        
        return daily_stats

    def scrap_period(self, start_dt, end_dt):
        period_stats = {}
        dates = self.getDates(start_dt, end_dt)
        
        for date in dates:
            period_stats[date.strftime('%d-%m-%Y')] = self.scrap_day(date)
        
        return period_stats
