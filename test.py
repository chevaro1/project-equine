from selectorlib import Extractor
import requests 

# Create an Extractor by reading from the YAML file
e = Extractor.from_yaml_file('naylors.yml')

# Download the page using requests
r = requests.get('https://www.naylors.com/women/country')
# Pass the HTML of the page and create 
data = e.extract(r.text)
# Print the data 
print(data)

# Download another page of similar structure
r = requests.get('https://www.naylors.com/men/country')
# Use the same extractor to get the data 
data = e.extract(r.text)
# Print it again

dist = data
key = dist.keys()

for x in dist:
  print(dist[x])
  print("hello there")
  print(x)
  for a in dist[x]:
    #print(a)
    print("\n" + "\n" + "inside: individual products" + "\n" + "\n")
    for i in a:
      print(a[i])
      #print("inside: I")


#print(key)

