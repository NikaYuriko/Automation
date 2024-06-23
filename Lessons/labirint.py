
# зайти на сайт Лабиринт
# найти книги по слову Python
# собрать все карточки товаров
# вывести в консоль инфо: (кол-во?), название, автор, цена для каждой карточки товара

# открыть хром

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.labirint.ru/")


# найти локатор поисковика через консоль

search_locator = "#search-field" #сохранили текст в переменную

search_input = driver.find_element(By.CSS_SELECTOR, search_locator) #заставляем драйвер найти элемент по локатору, в переменную сохранили ссылку на элемент и работаем уже с ним

# send_keys - вставить значение 

search_input.send_keys("Python")

search_input.send_keys(Keys.RETURN)

book_locator = "div.product-card"

#теперь нужно собрать все элементы, которые есть на странице (их 60)

books = driver.find_elements(By.CSS_SELECTOR, "div.product-card")

print(len(books))

# вывести в консоль инфо: название, автор, цена 

for book in books:
	title = book.find_element(By.CSS_SELECTOR, "a.product-card__name").text
	price = book.find_element(By.CSS_SELECTOR, "div.product-card__price-current").text
	author = " " 
	try:
		author = book.find_element(By.CSS_SELECTOR, "div.product-card__author").text
	except:
		author = "Автор не указан"
	print(author + "\t" + title + "\t" + price)


sleep(5)