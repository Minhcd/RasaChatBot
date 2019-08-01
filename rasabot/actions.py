# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
from rasa_sdk import Action

logger = logging.getLogger(__name__)

class ActionOrderProduct(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_order_product"

    def run(self, dispatcher, tracker, domain):
        product = tracker.get_slot('product')
        model = tracker.get_slot('model')
        response = "Your product is {}, model is {} ".format(product, model)
        dispatcher.utter_message(response) #send the message back to the user
        return []