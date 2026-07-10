from playwright.sync_api import sync_playwright
import os

def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(
        headless=False
    )

def before_scenario(context, scenario):
    context.browser_context = context.browser.new_context()
    context.page = context.browser_context.new_page()

def after_scenario(context, scenario):
    if scenario.status == "failed":
        os.makedirs("screenshots", exist_ok=True)
        os.makedirs("logs", exist_ok=True)

        context.page.screenshot(
            path=f"screenshots/{scenario.name}.png"
        )

        with open(f"logs/{scenario.name}.html", "w", encoding="utf-8") as f:
            f.write(context.page.content())

    context.browser_context.close()

def after_all(context):
    context.browser.close()
    context.playwright.stop()