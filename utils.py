import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "movie.json"

import json
import requests
from twilio.twiml.messaging_response import MessagingResponse
import dialogflow_v2 as dialogflow
dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "movie-bot-huscdl"


def movie(parameters):
	x=parameters.get('movie')
	return x

def detect_intent_from_text(text, session_id, language_code='en'):
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result

def fetch_reply(msg, session_id):
	response = detect_intent_from_text(msg, session_id)
	if response.intent.display_name == 'movie':
		api_key='xxxxxxxxxx'
		x=movie(dict(response.parameters))
		movie_detail = requests.get('http://www.omdbapi.com/?t={0}&apikey={1}'.format(x,api_key)).content
		movie_detail = json.loads(movie_detail)
		news_str = 'Here is your details:'
		news_str += "\n\n{}\n\n{}\n\n\n\n{}\n\n{}\n\n".format(movie_detail['Title'], movie_detail['Released'], movie_detail['Actors'], movie_detail['Plot'])
		return news_str
	elif response.intent.display_name == 'image':
		url="https://picsum.photos/"
		l = str(random.randint(1,100))
		b = str(random.random(1,100))
		url +="/"+l+"/"+b
		resp = MessagingResponse()
		resp.message(fetch_reply(msg,sender))
		resp.message("You get  {}".format(msg)).media(url)
		return 'image'
	else:
		return response.fulfillment_text

