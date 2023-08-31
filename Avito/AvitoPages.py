from BaseApp import BasePage
from selenium.webdriver.common.by import By

from urllib.parse import unquote

class AvitoSearchLocators:
    # локатор для кнопки Добавить в избранное
    LOCATOR_AVITO_ADD_TO_FAVORITES_BUTTON = (By.XPATH, "//button[@title='Добавить в избранное']")
    # локатор для иконки Избранное
    LOCATOR_AVITO_FAVORITES_ICON = (By.XPATH, "//a[@title='Избранное']")
    # локатор для объявления с нужным названием на странице избранных объявлений
    LOCATOR_AVITO_RELEVANT_AD = (By.XPATH, "//strong[text()='Domain-Driven Design Distilled Vaughn Vernon']")
    
    
class SearchHelper(BasePage):
    def click_on_add_to_favorites_button(self):
        # Получим кнопку "Добавить в избранное" и кликнем на неё
        button = self.find_element(AvitoSearchLocators.LOCATOR_AVITO_ADD_TO_FAVORITES_BUTTON, time = 10)
        return self.driver.execute_script("arguments[0].click();", button)
        
    def click_on_favorites_icon(self):
        # Получим иконку Избранное и кликнем на неё
        return self.find_element(AvitoSearchLocators.LOCATOR_AVITO_FAVORITES_ICON, time = 10).click()

    def get_relevant_ad(self):
        # Получим текст нужного объявления, если оно в Избранном
        return self.find_element(AvitoSearchLocators.LOCATOR_AVITO_RELEVANT_AD, time = 10).text
    
    
