from selenium import webdriver
import time

class Instagram:
    def __init__(self,userName,Password,UnfollerNO):
        self.userName = userName
        self.Password = Password
        self.UnfollerNo= UnfollerNO + 4
        self.driver = webdriver.Chrome('.\chromedriver.exe')
        self.base_Url = 'https://www.instagram.com/'
        self.login()
    def login(self):

        self.driver.get(f'{self.base_Url}accounts/login/')
        time.sleep(2)

        self.driver.find_element_by_name("username").send_keys(self.userName)
        self.driver.find_element_by_name("password").send_keys(self.Password)
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/"
                                              "article/div/div[1]/div/form/div[4]/button/div").click()

        self.profile()
    def profile(self):
        # move into profile
        time.sleep(5)
        self.driver.get(f"{self.base_Url}{self.userName}")
        time.sleep(2)
        # click on following button
        A_element = self.driver.find_elements_by_tag_name("a")
        A_element[2].click()
        time.sleep(2)
        self.UnFollowing()
    def UnFollowing(self):
        ##how much to un follow
        y = self.UnfollerNo
        for x in range(4,y):
            # click on(x) no to un-follow
            
            unfollow_button = self.driver.find_elements_by_tag_name("button")
            unfollow_button[x].click()
            time.sleep(2)
            if x == 15:
                
                time.sleep(5)
                

            # click on un-follow which conferm on every (x) un follow
            unfollow_button_click = self.driver.find_elements_by_tag_name("button")
            unfollow_button_click[-2].click()
            time.sleep(3)
            
                



if __name__ == "__main__":
    igbot = Instagram('coder_vs','pokeymon@178',150)