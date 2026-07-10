def wait_for_element(page, selector):
    page.wait_for_selector(selector)

def take_screenshot(page, path):
    page.screenshot(path=path)