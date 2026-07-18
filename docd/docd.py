from playwright.sync_api import sync_playwright, expect


class Browser:
    def __init__(self):
        self.history = []
        self.openPages = 0

    def open(self):
        with sync_playwright() as self.p:
            self.browser = self.p.chromium.launch()
    
    def openPage(self, url: str):
        self.url = url.strip()
        page = self.browser.new_page()
        page.goto(self.url)    
        page.wait_for_load_state("networkidle")
        self.history.append(self.url)
        self.openPages = self.openPages + 1
        return page
            
    def closePage(page: playwright.sync_api._generated.Page): ################################ 
        page.close()
        self.openPages = self.openPages - 1
        
    def close(self):
        self.browser.close()
        
    def checkInHistory(self, url: str):
        if url in self.history:
            return true
        else:
            return false
        
# Only scrape trusted doc site   (Contains the word Documentation, Reference, Tutorial)     
# Go To Contents
# Limit depth to 4
# Link content