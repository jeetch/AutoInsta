from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd 


chromedriver_path = '/home/jeet/Documents/chromedriver/chromedriver'
webdriver = webdriver.Chrome(executable_path = chromedriver_path)

sleep(2)

webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys('your_username')
password = webdriver.find_element_by_name('password')
password.send_keys('your_password')

button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button')
button_login.click()
sleep(3)

notnow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
notnow.click() 

hashtag_list = ['travel']


new_followed = []
tag = -1
followed = 0
likes = 0
comments = 0



for hashtag in hashtag_list:
	tag += 1
	webdriver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
	sleep(5)
	first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
	
	first_thumbnail.click()
	sleep(randint(1,2))    
	try:
		print(f"inside try for tag {tag}")        
		for x in range(1,200):
			username = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/a').text
			print(username)
			
			
			if webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':
				print(f"Yep! Lets follow {username}")	
				sleep(5)
				webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
					
				new_followed.append(username)

				followed += 1

				# Liking the picture
				button_like = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
				print("liked!")
				button_like.click()
				likes += 1
				sleep(randint(18,25))

				# Comments and tracker
				comm_prob = randint(1,10)

				print('{}_{}: {}'.format(hashtag, x,comm_prob))
				
				comments += 1
				print("inside if!")
				webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[2]/button').click()
				print("click comment!")
				comment_box = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea')

				if (comm_prob < 7):
					comment_box.send_keys('Really cool!')
					sleep(1)
				elif (comm_prob > 6) and (comm_prob < 9):
					comment_box.send_keys('Nice work :)')
					sleep(1)
				elif comm_prob == 9:
					comment_box.send_keys('Nice gallery!!')
					sleep(1)
				elif comm_prob == 10:
					comment_box.send_keys('So cool! :)')
					sleep(1)
				# Enter to post comment
				comment_box.send_keys(Keys.ENTER)
				sleep(randint(22,28))

				# Next picture
				webdriver.find_element_by_link_text('Next').click()
				sleep(randint(25,29))
			else:
				webdriver.find_element_by_link_text('Next').click()
				sleep(randint(20,26))
	
	except:
		continue


print('Liked {} photos.'.format(likes))
print('Commented {} photos.'.format(comments))
print('Followed {} new people.'.format(followed))