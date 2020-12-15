from __future__ import print_function
import gamefiles
import database

Money = float(1.0)


def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event)
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])


def on_intent(event):
    if event["request"]["intent"]["name"] == "roll":
        tempmoney, Message = gamefiles.Game(Money)
        Message = Message + " You have £" + str(tempmoney) + " left."
        session_attributes = {}
        card_title = "Roll Complete"
        speech_output = Message
        reprompt_text = speech_output
        should_end_session = False
        return build_response(session_attributes,
                              build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    return get_welcome_response()


def on_session_ended(session_ended_request, session):
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])


def get_welcome_response():
    temp = str(Money)
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to the fruit machine test game. you currently have £" + temp + " if you would like to play say Roll else you can quit or say help."
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': 'SessionSpeechlet - ' + title,
            'content': 'SessionSpeechlet - ' + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }