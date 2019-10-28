import logging
import os

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

    message = "Wow! I can't believe I found {}.".format(title)
    cloud_storage.download_image(image)

    access_token = os.getenv('ACCESS_TOKEN')
    page_id = os.getenv('FB_PAGE_ID')

    graph = facebook.GraphAPI(access_token)
    post = graph.put_photo(image=open(image, 'rb'), message=message)

    logging.debug("Posted photo with post_id {}.".format(post['post_id']))
