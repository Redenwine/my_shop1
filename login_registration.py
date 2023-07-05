# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# myacc = driver.find_element_by_link_text("My Account")
# myacc.click()
# mailmy = driver.find_element_by_id("reg_email")
# mailmy.send_keys("baracuda23@mal.ru")
# time.sleep(3)
# mail_adr = driver.find_element_by_id("reg_password")
# mail_adr.send_keys("Dd652066shop")
# registr_btn = driver.find_element_by_css_selector("p.woocomerce-FormRow.form-row > input.woocommerce-Button.button")
# registr_btn.click()
# # driver.quit()

# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# myacc = driver.find_element_by_link_text("My Account")
# myacc.click()
# mailmy = driver.find_element_by_id("username")
# mailmy.send_keys("baracuda23@mal.ru")
# time.sleep(3)
# mail_adr = driver.find_element_by_id("password")
# mail_adr.send_keys("Dd652066shop")
# login_btn = driver.find_element_by_css_selector("p:nth-child(3) > input.woocommerce-Button.button")
# login_btn.click()
# logoutbtn = driver.find_element_by_xpath('//*[@id="page-36"]/div/div[1]/nav/ul/li[6]/a')
# logoutbtn_get_text = logoutbtn.text
# assert logoutbtn_get_text == "Logout"
# driver.quit()