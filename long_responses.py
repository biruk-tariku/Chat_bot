import random

R_EATING = ['i am a robot i donot eat anything! ']

def unknown():
    response = ['could u please re-phrase that?', 
                "....", 
                'sounds about right',
                'what does that mean?'][random.randrange(4)]
    
    return response