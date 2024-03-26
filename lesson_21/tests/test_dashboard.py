def test_go_to_sale(dashboard):
    dashboard.click_sale()
    assert dashboard.driver.title == "Харчування - "

def test_go_to_discount_and_check_product(dashboard):
    category = dashboard.click_header_discount()
    cat==

