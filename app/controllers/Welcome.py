"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
from random import randrange
from time import strftime
from datetime import datetime

search_settings = {
    'farm': {'min': 10 , 'max': 20},
    'cave': {'min': 5, 'max': 10},
    'house': {'min': 2, 'max': 5},
    'casino': {'min': -50, 'max': 50},
    }

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        
   
    def index(self):
        if not 'total_gold' in session:
            session['total_gold'] = 0
            session['activity-feed'] =[]
        
        return self.load_view('index.html')
    def process_money(self):
        location = request.form['location']
        range_max = search_settings[location]['max']
        range_min = search_settings[location]['min']
        rand_gold = randrange(range_min, range_max + 1)
        session['total_gold'] += rand_gold
        current_time =datetime.now().strftime("%Y-%m-%d %I:%M%p")
        if rand_gold < 0:
            text_color = 'red'
            sentence = "Entered a {} and lost {} golds... Ouch... ({})".format(location,rand_gold * -1, current_time)
        else:
            text_color = 'green'
            sentence = "Earned {} golds from the {}! ({})".format(rand_gold, location, current_time)
            outcome = {
            'description': sentence,
            'text_color': text_color
            }
            session['activity-feed'].insert(0, outcome)
            return redirect('/')
        return redirect('/')
