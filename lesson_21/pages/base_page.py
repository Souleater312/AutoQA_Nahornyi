('xpath', '//a[@class="header__action header__action_cart js-header-cart"]/div/div/text()')
self.locator_button_buy_one = ('xpath', '//div[@class="product__control"]/div[1]//a')
self.locator_button_buy_multiple = ('xpath', '//div[@class="product__control"]/div[2]//a')
self.locator_add_to_favourite = ('xpath', '//div[@class="product__line"]/div[@class="actions"]/button[@class="actions__button js-favorite-product "]')

def scroll_a_bit(self):
    actions = ActionChange

    def return_cart_counter(self):
        car_counter = self.wait_until_element_presence(self.location_cart_item_counter):
