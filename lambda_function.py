from __future__ import print_function
import gamefiles


def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event)
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event)
    elif event['request']['type'] == "SessionEndedRequest":
        session_attributes = {
            "Money": 0
        }
        card_title = "Game End"
        speech_output = "Thanks for playing fruit machine, if you'd like to play again. Say, Launch Fruit Machine."
        reprompt_text = speech_output
        should_end_session = True
        return build_response(session_attributes,
                              build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def on_intent(event):
    if event["request"]["intent"]["name"] == "AMAZON.StopIntent":
        session_attributes = {
            "Money": 0
        }
        card_title = "Game End"
        speech_output = "Thanks for playing fruit machine, if you'd like to play again. Say, Launch Fruit Machine."
        reprompt_text = speech_output
        should_end_session = True
        return build_response(session_attributes,
                              build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))
    if event["request"]["intent"]["name"] == "roll":
        Money = getmoney(event)
        tempmoney, Message = gamefiles.Game(Money)
        tempmoney = round(tempmoney, 2)
        if tempmoney <= 0:
            session_attributes = {
                "Money": 0
            }
            card_title = "Ran out of money"
            speech_output = "You have ran out of money, unfortunatly this means you've lost. If you'd like to launch the game again say, Launch Fruit Machine."
            reprompt_text = speech_output
            should_end_session = True
            return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text,
                                                                               should_end_session))
        else:
            Message = Message + " You have £" + str(tempmoney) + " left."
            session_attributes = {
                "Money": tempmoney
            }
            card_title = "Roll Complete"
            speech_output = Message
            reprompt_text = speech_output
            should_end_session = False
            return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text,
                                                                               should_end_session))


def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print(
        "on_session_started requestId=" + session_started_request['requestId'] + ", sessionId=" + session['sessionId'])


def on_launch(event):
    event["session"]["attributes"] = {}
    Money = 1.0
    return get_welcome_response(event)


def getmoney(event):
    Money = event["session"]["attributes"]["Money"]
    return Money


def on_session_ended(session_ended_request, session):
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])


def get_welcome_response(event):
    session_attributes = {
        "Money": 1.0
    }
    card_title = "Welcome"
    speech_output = "Welcome to the fruit machine test game. you currently have £1 if you would like to play say Roll else you can quit or say help."
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