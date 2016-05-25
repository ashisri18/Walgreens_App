from selenium.webdriver.common.by import By

class HomeLoc(object):

    WALGREEN_LOGO = (By.ID, "ivWagLogo")                            # Using Id attribute
    INBOX_ICN = (By.ID, "inbox")
    SETTINGS_ICN = (By.XPATH, "//android.widget.TextView[@content-desc='Settings']")        # Using Content-desc
    PRESCRIPTIONS_BTN = (By.XPATH,"//android.widget.LinearLayout[contains(@resource-id,'btn_home_pharmacy')]") # Using Xpath and contains fun.
    SHOP_BTN = (By.ID, "btn_home_shop")
    PHOTO_BTN = (By.XPATH,"//android.widget.TextView[@text='Photo']")                       # Using Xpath and text
    WEEKLY_ADS_TXT = (By.NAME, "Weekly Ad & Coupons")               # Using Text attribute
    REFILL_ICN = (By.ID, "icon_home_refill_rx")                     # Using Id attribute
    REWARDS_BTN = (By.XPATH, "//android.widget.LinearLayout[@content-desc='Balance®Rewards']")
    STORE_LOCATOR_TXT = (By.NAME, "StoreLocator")
