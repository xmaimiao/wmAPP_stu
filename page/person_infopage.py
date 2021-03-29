from page.basepage import BasePage
from page.settingspage import Settings


class PersonInfo(BasePage):
    def goto_settings(self):
        self.step("../data/person_infopage.yaml", "goto_settings")
        return Settings(self.driver)

