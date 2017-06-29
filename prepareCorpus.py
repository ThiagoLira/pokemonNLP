import requests,re
from bs4 import BeautifulSoup
from prepareEpisode import prepareEpisode

main_link = "http://www.serebii.net/anime/epiguide/"


html = requests.get(main_link).text

"""If you do not want to use requests then you can use the following code below 
   with urllib (the snippet above). It should not cause any issue."""
soup = BeautifulSoup(html, "lxml")


episode_links = soup.find_all('a')


for episode_link in episode_links:

  if(("anime/epiguide" in  episode_link.get('href')) and (".shtml" in episode_link.get('href') )):
        full_link = "http://www.serebii.net"+ episode_link.get('href')
        print(full_link)        
        prepareEpisode(full_link)


#print(episode_links)