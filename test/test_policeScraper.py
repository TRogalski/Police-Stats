from nose.tools import *
from policeStats.policeScraper.policeScraper import PoliceScraper
import requests

def test_scrap_period_1():
    policeScraper = PoliceScraper()
    result = policeScraper.scrap_period("24-11-2019", "25-11-2019")
    
    expected = {
        '24-11-2019': {
            'Zatrzymani na gorącym uczynku': 56, 'Zatrzymani poszukiwani': 13,
            'Zatrzymani nietrzeźwi kierujący': 12, 'Wypadki drogowe': 5, 
            'Zabici w wypadkach drogowych': 0, 
            'Ranni w wypadkach drogowych': 6}
    }

    assert expected == result
    

def test_scrap_period_2():
    policeScraper = PoliceScraper()
    result = policeScraper.scrap_period("20-11-2019", "21-11-2019")
    
    expected = {
        '20-11-2019': {
            'Zatrzymani na gorącym uczynku': None, 
            'Zatrzymani poszukiwani': None, 
            'Zatrzymani nietrzeźwi kierujący': None, 
            'Wypadki drogowe': None, 
            'Zabici w wypadkach drogowych': None, 
            'Ranni w wypadkach drogowych': None}
    }

    assert expected == result


def test_scrap_period_3():
    policeScraper = PoliceScraper()
    result = policeScraper.scrap_period("20-11-2019", "22-11-2019")
    
    expected = {
        '20-11-2019': {
            'Zatrzymani na gorącym uczynku': None, 
            'Zatrzymani poszukiwani': None, 
            'Zatrzymani nietrzeźwi kierujący': None, 
            'Wypadki drogowe': None, 
            'Zabici w wypadkach drogowych': None, 
            'Ranni w wypadkach drogowych': None}, 
        '21-11-2019': {
            'Zatrzymani na gorącym uczynku': 57, 
            'Zatrzymani poszukiwani': 28, 
            'Zatrzymani nietrzeźwi kierujący': 16, 
            'Wypadki drogowe': 5, 
            'Zabici w wypadkach drogowych': 2, 
            'Ranni w wypadkach drogowych': 3}
    }

    assert expected == result
