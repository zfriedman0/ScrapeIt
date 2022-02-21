#This code is adapted from https://www.geeksforgeeks.org/scraping-reddit-using-python/
#Reference: https://praw.readthedocs.io/en/latest/code_overview/models/submission.html

#This 'scraper' is designed to retrieve the URLs of the top 100 images from a few hand-selected subreddits for the purposes of training the BrutalGAN
#List of potential subs: Brutalism, UrbanHell, sovietarchitecture, AbandonedPorn, Abandoned, Asylums, ImaginaryDerelicts, ImaginaryWastelands, RustyRails, UrbanExploration

import os.path
import praw
import requests
import shutil

PATH = './img'
LIMIT = 100
reddit_read_only = praw.Reddit(client_id='9ZjVoxUW3X-VqVMeqFvUxQ', client_secret='9r8LqCpH6wkP8UG2cIC3P-haTGtfAQ', user_agent='BigScrapes')

#subs = ['Brutalism', 'UrbanHell', 'sovietarchitecture', 'AbandonedPorn', 'Abandoned', 'UrbanExploration']
s = input("Enter a subreddit: ")
urls = [] #a list of image URLs to be downloaded

#for s in subs:
subreddit = reddit_read_only.subreddit(s)

#print("\n***Subreddit*** " + s)

for post in subreddit.top(limit=LIMIT):
    if not post.selftext:
        #print("\nTitle: " + post.title)
        #print("\nURL: " + post.url)

        urls.append(post.url)

print(urls)

for u in urls:
    res = requests.get(u, stream=True)
    filename = u.split('/')[-1]
    
    if res.status_code == 200:
        with open(os.path.join(PATH, filename), 'wb') as f:
            for chunk in res:
                f.write(chunk)
        print('\nImage download successful.')
    else:
        print('\nError downloading image.')
