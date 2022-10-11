from bs4 import BeautifulSoup
import random
import requests
class Parsing():
	def Putin_jokes_parsing():
		url = "https://www.anekdot.ru/tags/%D0%9F%D1%83%D1%82%D0%B8%D0%BD"
		req = requests.get(url)
		src = req.text
		with open('index.html', 'w', encoding='utf-8') as file:
			file.write(src)
		soup = BeautifulSoup(src, "lxml")
		jokes = soup.find_all('div', class_="text")
		random_index = random.randrange(len(jokes))
		Generated_joke = jokes[random_index].text
		return Generated_joke

	def Obama_jokes_parsing():
		url = "https://www.anekdot.ru/tags/%D0%9E%D0%B1%D0%B0%D0%BC%D0%B0"
		req = requests.get(url)
		src = req.text
		with open('index.html', 'w', encoding='utf-8') as file:
			file.write(src)
		soup = BeautifulSoup(src, "lxml")
		jokes = soup.find_all('div', class_="text")
		random_index = random.randrange(len(jokes))
		Generated_joke = jokes[random_index].text
		return Generated_joke

	def Ukrain_jokes_parsing():
		url = "https://www.anekdot.ru/tags/%D0%A3%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%B0"
		req = requests.get(url)
		src = req.text
		with open('index.html', 'w', encoding='utf-8') as file:
			file.write(src)
		soup = BeautifulSoup(src, "lxml")
		jokes = soup.find_all('div', class_="text")
		random_index = random.randrange(len(jokes))
		Generated_joke = jokes[random_index].text
		return Generated_joke

	def Pensioners_jokes_parsing():
		url = "https://www.anekdot.ru/tags/%D0%BF%D0%B5%D0%BD%D1%81%D0%B8%D0%BE%D0%BD%D0%B5%D1%80%D1%8B"
		req = requests.get(url)
		src = req.text
		with open('index.html', 'w', encoding='utf-8') as file:
			file.write(src)
		soup = BeautifulSoup(src, "lxml")
		jokes = soup.find_all('div', class_="text")
		random_index = random.randrange(len(jokes))
		Generated_joke = jokes[random_index].text
		return Generated_joke

	def Fishing_jokes_parsing():
		url = "https://www.anekdot.ru/tags/%D1%80%D1%8B%D0%B1%D0%B0%D0%BB%D0%BA%D0%B0"
		req = requests.get(url)
		src = req.text
		with open('index.html', 'w', encoding='utf-8') as file:
			file.write(src)
		soup = BeautifulSoup(src, "lxml")
		jokes = soup.find_all('div', class_="text")
		random_index = random.randrange(len(jokes))
		Generated_joke = jokes[random_index].text
		return Generated_joke

	def Politics_jokes_parsing():
		url = "https://www.anekdot.ru/tags/%D0%BF%D0%BE%D0%BB%D0%B8%D1%82%D0%B8%D0%BA%D0%B0"
		req = requests.get(url)
		src = req.text
		with open('index.html', 'w', encoding='utf-8') as file:
			file.write(src)
		soup = BeautifulSoup(src, "lxml")
		jokes = soup.find_all('div', class_="text")
		random_index = random.randrange(len(jokes))
		Generated_joke = jokes[random_index].text
		return Generated_joke

	def Stirlitz_jokes_parsing():
		url = "https://www.anekdot.ru/tags/%D0%A8%D1%82%D0%B8%D1%80%D0%BB%D0%B8%D1%86"
		req = requests.get(url)
		src = req.text
		with open('index.html', 'w', encoding='utf-8') as file:
			file.write(src)
		soup = BeautifulSoup(src, "lxml")
		jokes = soup.find_all('div', class_="text")
		random_index = random.randrange(len(jokes))
		Generated_joke = jokes[random_index].text
		return Generated_joke

	def Chukchi_jokes_parsing():
		url = "https://www.anekdot.ru/tags/%D1%87%D1%83%D0%BA%D1%87%D0%B0"
		req = requests.get(url)
		src = req.text
		with open('index.html', 'w', encoding='utf-8') as file:
			file.write(src)
		soup = BeautifulSoup(src, "lxml")
		jokes = soup.find_all('div', class_="text")
		random_index = random.randrange(len(jokes))
		Generated_joke = jokes[random_index].text
		return Generated_joke

	def Junkies_jokes_parsing():
		url = "https://www.anekdot.ru/tags/%D0%BD%D0%B0%D1%80%D0%BA%D0%BE%D1%82%D0%B8%D0%BA%D0%B8"
		req = requests.get(url)
		src = req.text
		with open('index.html', 'w', encoding='utf-8') as file:
			file.write(src)
		soup = BeautifulSoup(src, "lxml")
		jokes = soup.find_all('div', class_="text")
		random_index = random.randrange(len(jokes))
		Generated_joke = jokes[random_index].text
		return Generated_joke



	





