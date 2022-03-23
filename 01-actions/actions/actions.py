import datetime as dt 
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=f"La hora es: {dt.datetime.now()}")

        return []


        'GET' \
 \
  -H 'accept: application/json'

  




class ActionEmpleo(Action):

    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        resp = requests.get(  'https://www.zaragoza.es/sede/servicio/oferta-empleo/690?rf=html')

        dispatcher.utter_message(text=f"El empleo disponible es:  {dt.datetime.now()}")

        return []
