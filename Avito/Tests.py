from AvitoPages import SearchHelper
import time
import urllib

def test_avito_favorites(browser):
    # Создаём объект, соответствующий веб-странице (согласно паттерну Page Object)
    avito_ad_page = SearchHelper(browser)
    # Переходим на страницу нужного объявления
    avito_ad_page.go_to_site()

    # Добавляем объявление в Избранное
    avito_ad_page.click_on_add_to_favorites_button()
    #time.sleep(20)

    # Кликаем на иконку Избранное
    avito_ad_page.click_on_favorites_icon()
    
    # Создаём объект, соответствующий странице избранных объявлений
    avito_favorites_page = SearchHelper(browser)
    avito_favorites_page.driver.get(avito_favorites_page.driver.current_url)
    #time.sleep(20)

    # Проверяем, что нужное объявление присутствует на странице избранных объявлений
    favorites_ad_text = avito_favorites_page.get_relevant_ad()
    assert favorites_ad_text == "Domain-Driven Design Distilled Vaughn Vernon"


