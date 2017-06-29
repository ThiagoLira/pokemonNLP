import requests,re
from bs4 import BeautifulSoup
# import modules & set up logging
from pathlib import Path

def prepareEpisode (link):
  #cria episodename.txt com corpus para episodio do link argumento
  html = requests.get(link).text

  episode_name = re.search('/epiguide/(.*).shtml',link)

  episode_name = episode_name.group(1)

  episode_name = re.sub(r'/', '', episode_name)

  """If you do not want to use requests then you can use the following code below 
     with urllib (the snippet above). It should not cause any issue."""
  soup = BeautifulSoup(html, "lxml")

  tudo = soup.get_text()
  try:
    #pega pedaco que importa do texto da url  
    episode_text = tudo.split("Do Not Translate it into your languange and claim ownership",1)[1]  

    #sem resuminho no final
    episode_text2 = episode_text.split("\n\n\n\n\n\n",1)[0]
  except IndexError:
    #nao tem texto por algum motivo aqui
    return(-1)

  file_name = episode_name + '.txt'


  file = Path('pokeCorpus/' + file_name)

  #se ja existe nao precisa fazer tudo de novo
  if( not file.is_file()):
    
    with open('pokeCorpus/'+file_name, "w") as text_file:
      text_file.write(episode_text2)




  #with open("Output.txt", "r") as text_file:

  #  print(clean(text_file.read()))
prepareEpisode("http://www.serebii.net/anime/epiguide/indigo/039.shtml")
