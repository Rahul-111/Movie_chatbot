from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
import requests
import json

from utils import fetch_reply
app=Flask(__name__)

@app.route("/")
def helloworld():
	return "Hello"

@app.route("/sms",methods=['GET','POST'])
def sms_ahoy_reply():
	resp = MessagingResponse()
	msg=request.form.get('Body')
	sender = request.form.get('From')
	resp = MessagingResponse()
	resp.message(fetch_reply(msg,sender))
	return str(resp)

	# resp.message(fetch_reply(msg,sender))
	# return str(resp)

if __name__ == "__main__":
	app.run(debug=True)

# import os
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "movie.json"


# import dialogflow_v2 as dialogflow
# dialogflow_session_client = dialogflow.SessionsClient()
# PROJECT_ID = "movie-bot-huscdl"



# def movie(parameters):
# 	x=parameters.get('movie')
# 	return x

# def detect_intent_from_text(text, session_id, language_code='en'):
#     session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
#     text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
#     query_input = dialogflow.types.QueryInput(text=text_input)
#     response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)
#     return response.query_result


# def fetch_reply(msg, session_id):
# 	response = detect_intent_from_text(msg, session_id)
# 	if response.intent.display_name == 'movie':
# 		return 'movie'
# 	elif response.intent.display_name == 'image':
# 		return 'image'
# 	else:
# 		return response.fulfillment_text
	# if response.intent.display_name == 'movie':
	# 	api_key='b9e0f604'
	# 	x=movie(dict(response.parameters))
	# 	movie_detail = requests.get('http://www.omdbapi.com/?t={0}&apikey={1}'.format(x,api_key)).content
	# 	movie_detail = json.loads(movie_detail)
	# 	news_str = 'Here is your news:'
	# 	news_str += "\n\n{}\n\n{}\n\n\n\n{}\n\n{}\n\n".format(movie_detail['Title'], movie_detail['Released'], movie_detail['Actors'], movie_detail['Plot'])
	# 	return news_str
	# elif response.intent.display_name == 'image':
	# 	url="https://picsum.photos/"
	# 	l = str(random.randint(1,100))
	# 	b = str(random.random(1,100))
	# 	url +="/"+l+"/"+b
	# 	resp.message("You get  {}".format(msg)).media(url)
	# 	return img
	# else:
	# 	return response.fulfillment_text


	# api_key='b9e0f604'
	# movie_detail = requests.get('http://www.omdbapi.com/?t={0}&apikey={1}'.format(msg,api_key)).content
	# movie_detail = json.loads(movie_detail)
	# news_str = 'Here is your news:'
	# news_str += "\n\n{}\n\n{}\n\n\n\n{}\n\n{}\n\n".format(movie_detail['Title'], movie_detail['Released'], movie_detail['Actors'], movie_detail['Plot'])

	# resp.message("you have typed:{}".format(msg))
	
	# if fetch_reply(msg,sender) == 'movie':
	# 	api_key='b9e0f604'
	# 	x=movie(dict(response.parameters))
	# 	movie_detail = requests.get('http://www.omdbapi.com/?t={0}&apikey={1}'.format(x,api_key)).content
	# 	movie_detail = json.loads(movie_detail)
	# 	news_str = 'Response to your query '
	# 	news_str += "\n\n{}\n\n{}\n\n\n\n{}\n\n{}\n\n".format(movie_detail['Title'], movie_detail['Released'], movie_detail['Actors'], movie_detail['Plot'])
	# 	resp.message(news_str)
	# 	return str(resp)
	#if fetch_reply(msg,sender) == 'image':
		# url="https://picsum.photos/"
		# l = str(random.randint(1,100))
		# b = str(random.random(1,100))
		# url +="/"+l+"/"+b
		# resp.message("You got  {}".format(msg)).media(url)
		# resp.message("image {}".format(msg))
		# return str(resp)