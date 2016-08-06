import facebook
import util
import datetime
import humanize
import re

#---------------------- Event List ----------------------
event_ids = ['788861314549484', # Battle above the clouds
            #'692430650895680',  # STS
            '1787573954810921', # Bad Manners 4
            '1216950281690985', # No Contest 8/20
            '924707064342438',  # NACL August 8/27
            '835712656564201',  # NACL September
            '272904843091886',  # NACL October
            ]  
#--------------------------------------------------------
secrets = open('graphapi.secret', 'r')
at = util.get_fb_token(secrets.readline().strip(), secrets.readline().strip())
graph = facebook.GraphAPI(access_token = at, version = '2.2')

results = open('EventChart.result', 'w+')
results.write("------------------- Upcoming Events -------------------\n---------------------------------------------------------------\n\n")

csv = open('EventChart.csv', 'w+')
csv.write("Name,Date,Addresses,Venue,Facebook Page\n")

for event_id in event_ids:
    event = graph.get_object( id = event_id)
    
    name = re.sub("\(.*\)","",event['name'])
    print event['place']
    
    date = datetime.datetime.strptime(event['start_time'][:10], "%Y-%m-%d")
    date = humanize.naturalday(date).title()
    
    city = event['place']['location']['city']
    state = event['place']['location']['state']
    address = event['place']['location']['street']
    location = event['place']['name']
    
    url = "facebook.com/events/"+event_id
    
    results.write(date + " - " + name + " [" + city + ", " + state + "]\n"+url+"\n----------------------------------------------------------------\n")
    csv.write(name+","+date+","+address+","+location+","+url+"\n")
    
results.close()
csv.close()