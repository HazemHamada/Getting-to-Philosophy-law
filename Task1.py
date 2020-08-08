try:
  import urllib.request as urllib2
except:
  import urllib2

from bs4 import BeautifulSoup
import warnings

warnings.filterwarnings("ignore")
warnings.filterwarnings("error", message=".*check_inverse*.", category=UserWarning, append=False)

source = "https://en.wikipedia.org"

# get the html from address
def read_html(address):
 if address.__contains__("https://en.wikipedia.org/wiki"):
  return urllib2.urlopen(address).read()
 else:
  return urllib2.urlopen(source+address).read()

# get the first link from a BeautifulSoup object
def first_link(soup):
 for p in soup.find('div',{'id':'bodyContent'}).findAll('p'):
  for a in p.findAll('a'):
   if a and a.get('href').startswith('/wiki/') and not ":" in a.get('href'):
    return a.get('href')

# run search
def run_search_to_philosophy_page(initial_address, max_iterations=100, verbose=False):
 target_page = "/wiki/Philosophy"
 iteration = 0
 pages_visited = []
 current_address = initial_address if "/wiki/" in initial_address else "/wiki/"+initial_address
 if verbose:
  print("\ninitial address: " + current_address+"\n Will you go to "+target_page+" ?...\n")
 while iteration < max_iterations:
  current_address = first_link(BeautifulSoup(read_html(current_address)))
  if verbose:
   print(current_address)
  if current_address in pages_visited:  # checks for loops
   print("Loop " + str(iteration - pages_visited.index(current_address)) + " nodes found from "+str(pages_visited.index(current_address))+" iterations")
   return
  elif current_address.lower() == target_page.lower():  # finish
   print(str(iteration) + " iterations to get to the Philosophy page")
   return
  else:
   pages_visited.extend([current_address])
   iteration += 1
 return str(max_iterations)+" iterations reached"


if __name__ == "__main__":
  b=1
  while b==1:
   print("enter the topic to begin search with 'ex: spotify, music, dance, etc.' or the link itself or 0 to exit")
   address=input()
   if address!='0':
    try:
     run_search_to_philosophy_page(str(address), verbose=True)
    except:
     print("no search resulta found")
   else:
    break
