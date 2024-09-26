from selene import browser, be, have


def test_search_with_results(browser_settings):
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text("yashaka/selene: User-oriented Web UI browser tests in Python"))


def test_search_without_results(browser_settings):
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('dfghuфмуikjgfdsadfgум!:*hjgfd').press_enter()
    browser.element('.card-section').should(have.text("Your search - dfghuфмуikjgfdsadfgум!:*hjgfd - did not match any documents."))
