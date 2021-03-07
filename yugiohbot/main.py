import logging
import os
import random

import facebook
import requests

from utilities import cloud_storage

logging.basicConfig(level=logging.DEBUG)


def function(request):
    request_json = request.get_json()
    print(request_json)

    title = 'ERROR'
    image = 'ERROR'
    image_id = 'ERROR'

    if request_json is not None:
        title = request_json['title']
        image = request_json['image']
        image_id = request_json['card_image']
    else:
        exit(1)

    print(title)
    print(image)
    print(image_id)

    message = choose_caption(title)
    cloud_storage.download_image(image)

    access_token = os.getenv('ACCESS_TOKEN')

    graph = facebook.GraphAPI(access_token, version="8.0")
    post = graph.put_photo(image=open('/tmp/' + image, 'rb'), message=message)

    url = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'
    params = {'name': image_id}
    res = requests.get(url, params=params)
    if res.status_code == 200:
        comment = graph.put_comment(object_id=post['post_id'],
                                    message="Card Name: {0}\nCard image: {1} - {2}".format(title, str(image_id),
                                                                                           res.json()[0]['name']))
        print("Posted comment with comment_id {}".format(comment['id']))
    else:
        comment = graph.put_comment(object_id=post['post_id'],
                                    message="Card Name: {0}\nCard image: {1}".format(title, str(image_id)))
        print("Posted comment with comment_id {}".format(comment['id']))

    print("Posted photo with post_id {}.".format(post['post_id']))


def choose_caption(title):
    captions = ["Wow! I can't believe I found {}.", "I SUMMON THE ALL-POWERFUL {}!",
                "HAH! Your monsters may be powerful, Kaiba, but they are no match for the heart of the cards! My grandfather gave me this card, and I will use it wisely. Go, {}!",
                "Oh no! How will Joey win when he's facing {}?!", "{}? What's that? I've never seen that card before!",
                "Let's Duel! {}!", "It's time to d-d-d-d-d-duel!", "With this {}, you're finished!",
                "My latest creation! {}!", "Welp, this one's going on the ban list...", "Aha! {} is just what my deck needed!"]
    chosen = random.choice(captions)
    return chosen.format(title)
