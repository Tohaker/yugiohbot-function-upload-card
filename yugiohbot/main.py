import logging
import os
import random

import facebook

from utilities import cloud_storage

logging.basicConfig(level=logging.DEBUG)


def function(request):
    request_json = request.get_json(silent=True)
    request_args = request.args
    logging.debug(request_json)
    logging.debug(request_args)

    title = request_json['title']
    image = request_json['image']

    message = choose_caption(title)
    cloud_storage.download_image(image)

    access_token = os.getenv('ACCESS_TOKEN')

    graph = facebook.GraphAPI(access_token)
    post = graph.put_photo(image=open('/tmp/' + image, 'rb'), message=message)

    logging.debug("Posted photo with post_id {}.".format(post['post_id']))


def choose_caption(title):
    captions = ["Wow! I can't believe I found {}.", "I SUMMON THE ALL-POWERFUL {}!",
                "HAH! Your monsters may be powerful, Kaiba, but they are no match for the heart of the cards! My grandfather gave me this card, and I will use it wisely. Go, {}!",
                "Oh no! How will Joey win when he's facing {}?!", "{}? What's that? I've never seen that card before!",
                "Let's Duel! {}!", "It's time to d-d-d-d-d-duel!", "With this {}, you're finished!"]
    chosen = random.choice(captions)
    return chosen.format(title)
