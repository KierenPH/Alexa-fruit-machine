from __future__ import print_function
import gamefiles


def lambda_handler(event, context):
    if event["context"]["System"]["application"][
        "applicationId"] != "amzn1.ask.skill.4fbb14b4-0a0b-41b7-ba47-191e1987e566":
        return error()
    elif event["context"]["System"]["application"][
        "applicationId"] == "amzn1.ask.skill.4fbb14b4-0a0b-41b7-ba47-191e1987e566":
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
            return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text,
                                                                               should_end_session))
    else:
        return error()


def error():
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
    if event["request"]["intent"]["name"] == "rules":
        return rules(event)
    if event["request"]["intent"]["name"] == "AMAZON.HelpIntent":
        return help(event)
    if event["request"]["intent"]["name"] == "AMAZON.CancelIntent":
        session_attributes = {
            "Money": 0
        }
        card_title = "Exit"
        speech_output = "Thanks for playing the Fruit Machine skill, if you'd like to play again. Say, Launch Fruit " \
                        "Machine. "
        reprompt_text = speech_output
        should_end_session = True
        return build_response(session_attributes,
                              build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))
    if event["request"]["intent"]["name"] == "AMAZON.NavigateHomeIntent":
        Money = getmoney(event)
        session_attributes = {
            "Money": Money
        }
        card_title = "Game End"
        speech_output = "You currently have £" + Money + ". Say Roll to play!"
        reprompt_text = speech_output
        should_end_session = True
        return build_response(session_attributes,
                              build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))
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
        Message = Message + " You have £" + str(tempmoney) + " left."
        if tempmoney <= 0:
            Message = Message+" You have ran out of money, this means the game is over. Launch the skill again to play " \
                              "another time."
            should_end_session = True
        else:
            Message = Message + " You have £" + str(tempmoney) + " left."
            should_end_session = False
        session_attributes = {
            "Money": tempmoney
        }
        card_title = "Roll Complete"
        speech_output = Message
        reprompt_text = speech_output
        return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text,
                                                                               should_end_session))


def rules(event):
    Money = getmoney(event)
    session_attributes = {
        "Money": Money
    }
    card_title = "Help"
    speech_output = "There are only a few game rules, these are;" \
                    "1. Each roll cost 20p. " \
                    "2. If you get to of the same you win 50p. " \
                    "3. You get £1 for 3 of the same. " \
                    "4. And the golden win, £5 for 3 bells. " \
                    "5. However, if you get 2 skulls, you lose 50p. " \
                    "6. If you get 3 skulls, you lose all your money. "
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes,
                          build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))

def help(event):
    Money = getmoney(event)
    session_attributes = {
        "Money": Money
    }
    card_title = "Help"
    speech_output = "To play you can say, Roll. If you want to learn the rules, you can say what are the rules. And to leave the game, you can say Stop."
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes,
                          build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))

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
    speech_output = "Welcome to the fruit machine game, we are currently in beta. you currently have £1 if you would like to play say ,Roll else you can quit, or say help."
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
            'title': title,
            'content':output
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