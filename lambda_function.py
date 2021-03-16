from __future__ import print_function
import gamefiles
import databaseinteractor

arrBad = [
'2g1c',
'2 girls 1 cup',
'acrotomophilia',
'anal',
'anilingus',
'anus',
'arsehole',
'ass',
'asshole',
'assmunch',
'auto erotic',
'autoerotic',
'babeland',
'baby batter',
'ball gag',
'ball gravy',
'ball kicking',
'ball licking',
'ball sack',
'ball sucking',
'bangbros',
'bareback',
'barely legal',
'barenaked',
'bastardo',
'bastinado',
'bbw',
'bdsm',
'beaver cleaver',
'beaver lips',
'bestiality',
'bi curious',
'big black',
'big breasts',
'big knockers',
'big tits',
'bimbos',
'birdlock',
'bitch',
'black cock',
'blonde action',
'blonde on blonde action',
'blow j',
'blow your l',
'blue waffle',
'blumpkin',
'bollocks',
'bondage',
'boner',
'boob',
'boobs',
'booty call',
'brown showers',
'brunette action',
'bukkake',
'bulldyke',
'bullet vibe',
'bung hole',
'bunghole',
'busty',
'butt',
'buttcheeks',
'butthole',
'camel toe',
'camgirl',
'camslut',
'camwhore',
'carpet muncher',
'carpetmuncher',
'chocolate rosebuds',
'circlejerk',
'cleveland steamer',
'clit',
'clitoris',
'clover clamps',
'clusterfuck',
'cock',
'cocks',
'coprolagnia',
'coprophilia',
'cornhole',
'cum',
'cumming',
'cunnilingus',
'cunt',
'darkie',
'date rape',
'daterape',
'deep throat',
'deepthroat',
'dick',
'dildo',
'dirty pillows',
'dirty sanchez',
'dog style',
'doggie style',
'doggiestyle',
'doggy style',
'doggystyle',
'dolcett',
'domination',
'dominatrix',
'dommes',
'donkey punch',
'double dong',
'double penetration',
'dp action',
'eat my ass',
'ecchi',
'ejaculation',
'erotic',
'erotism',
'escort',
'ethical slut',
'eunuch',
'faggot',
'fecal',
'felch',
'fellatio',
'feltch',
'female squirting',
'femdom',
'figging',
'fingering',
'fisting',
'foot fetish',
'footjob',
'frotting',
'fuck',
'fucking',
'fuck buttons',
'fudge packer',
'fudgepacker',
'futanari',
'g-spot',
'gang bang',
'gay sex',
'genitals',
'giant cock',
'girl on',
'girl on top',
'girls gone wild',
'goatcx',
'goatse',
'gokkun',
'golden shower',
'goo girl',
'goodpoop',
'goregasm',
'grope',
'group sex',
'guro',
'hand job',
'handjob',
'hard core',
'hardcore',
'hentai',
'homoerotic',
'honkey',
'hooker',
'hot chick',
'how to kill',
'how to murder',
'huge fat',
'humping',
'incest',
'intercourse',
'jack off',
'jail bait',
'jailbait',
'jerk off',
'jigaboo',
'jiggaboo',
'jiggerboo',
'jizz',
'juggs',
'kike',
'kinbaku',
'kinkster',
'kinky',
'knobbing',
'leather restraint',
'leather straight jacket',
'lemon party',
'lolita',
'lovemaking',
'make me come',
'male squirting',
'masturbate',
'menage a trois',
'milf',
'missionary position',
'motherfucker',
'mound of venus',
'mr hands',
'muff diver',
'muffdiving',
'nambla',
'nawashi',
'negro',
'neonazi',
'nig nog',
'nigga',
'nigger',
'nimphomania',
'nipple',
'nipples',
'nsfw images',
'nude',
'nudity',
'nympho',
'nymphomania',
'octopussy',
'omorashi',
'one cup two girls',
'one guy one jar',
'orgasm',
'orgy',
'paedophile',
'panties',
'panty',
'pedobear',
'pedophile',
'pegging',
'penis',
'phone sex',
'piece of shit',
'piss pig',
'pissing',
'pisspig',
'playboy',
'pleasure chest',
'pole smoker',
'ponyplay',
'poof',
'poop chute',
'poopchute',
'porn',
'porno',
'pornography',
'prince albert piercing',
'pthc',
'pubes',
'pussy',
'queaf',
'raghead',
'raging boner',
'rape',
'raping',
'rapist',
'rectum',
'reverse cowgirl',
'rimjob',
'rimming',
'rosy palm',
'rosy palm and her 5 sisters',
'rusty trombone',
's&m',
'sadism',
'scat',
'schlong',
'scissoring',
'semen',
'sex',
'sexo',
'sexy',
'shaved beaver',
'shaved pussy',
'shemale',
'shibari',
'shit',
'shota',
'shrimping',
'slanteye',
'slut',
'smut',
'snatch',
'snowballing',
'sodomize',
'sodomy',
'spic',
'spooge',
'spread legs',
'strap on',
'strapon',
'strappado',
'strip club',
'style doggy',
'suck',
'sucks',
'suicide girls',
'sultry women',
'swastika',
'swinger',
'tainted love',
'taste my',
'tea bagging',
'threesome',
'throating',
'tied up',
'tight white',
'tit',
'tits',
'titties',
'titty',
'tongue in a',
'topless',
'tosser',
'towelhead',
'tranny',
'tribadism',
'tub girl',
'tubgirl',
'tushy',
'twat',
'twink',
'twinkie',
'two girls one cup',
'undressing',
'upskirt',
'urethra play',
'urophilia',
'vagina',
'venus mound',
'vibrator',
'violet blue',
'violet wand',
'vorarephilia',
'voyeur',
'vulva',
'wank',
'wet dream',
'wetback',
'white power',
'women rapping',
'wrapping men',
'wrinkled starfish',
'xx',
'xxx',
'yaoi',
'yellow showers',
'yiffy',
'zoophilia']

def profanityFilter(text):
    text = text.lower
    text = str(text)
    brokenStr1 = text.split()
    new = ''
    for word in brokenStr1:
        if word in arrBad:
            return True
        return False

def lambda_handler(event, context):
    if event["context"]["System"]["application"]["applicationId"] != \
            "amzn1.ask.skill.4fbb14b4-0a0b-41b7-ba47-191e1987e566":
        return error()
    elif event["context"]["System"]["application"]["applicationId"] == \
            "amzn1.ask.skill.4fbb14b4-0a0b-41b7-ba47-191e1987e566":
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


def leaderboard(event):
    response = databaseinteractor.get_top_player()
    money = getmoney(event)
    session_attributes = {
        "Money": money
    }
    card_title = "Top Players"
    speech_output = response
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes,
                          build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def position(event):
    userid = event["session"]["user"]["userId"]
    money = getmoney(event)
    response = databaseinteractor.get_leaderboard_position(userid)
    session_attributes = {
        "Money": money
    }
    card_title = "Leaderboard Position"
    speech_output = response
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes,
                          build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def savescore(event):
    money = getmoney(event)
    userid = event["session"]["user"]["userId"]
    if databaseinteractor.check_score(userid,money):
        response = "What should I save your name as?"
        name = True
    else:
        response = "Your score is lower than the score we have saved, therefore we can't save your current score."
        name = None
    session_attributes = {
        "Money": money,
        "name": name
    }
    if response == "":
        response = "error"
    card_title = "Save Score"
    speech_output = response
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes,
                          build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def name(event):
    userid = event["session"]["user"]["userId"]
    money = getmoney(event)
    check = databaseinteractor.check_score(userid, money)
    try:
        name = event["request"]["intent"]["slots"]["firstname"]["value"]
    except:
        session_attributes = {
            "Money": money,
        }
        card_title = "Save Score"
        speech_output = "Error saving your score, no name found."
        reprompt_text = speech_output
        should_end_session = False
        return build_response(session_attributes,
                              build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))
    initials = ""
    entry = databaseinteractor.find_entry(userid)
    censor = profanityFilter(name)
    if not censor:
        if entry:
            update = databaseinteractor.update_score(userid, money,name)
            if not update:
                message = "There was a problem updating your score."
        else:
            score = getmoney(event)
            databaseinteractor.new_entry(userid,score,initials)
        check = databaseinteractor.find_entry(userid)
        if check:
            message = "Score saved."
        if not check:
            message = "There was an error saving your score, please send an email to the developer."
    else:
        message = "That name was found to contain profanity, please make sure your name isn't explicit and try again."
    session_attributes = {
            "Money": money,
        }
    card_title = "Save Score"
    speech_output = message
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes,
                            build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def on_intent(event):
    if event["request"]["intent"]["name"] == "name":
        return name(event)
    if event["request"]["intent"]["name"] == "savescore":
        return savescore(event)
    if event["request"]["intent"]["name"] == "position":
        return position(event)
    if event["request"]["intent"]["name"] == "leaderboard":
        return leaderboard(event)
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
            Message = Message + " You have ran out of money, this means the game is over. Launch the skill again to play " \
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
    card_title = "Rules"
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
    speech_output = "To play you can say, Roll. If you want to learn the rules, you can say what are the rules. And to" \
                    " leave the game, you can say Stop."\
                    "You can now save your score to our leaderboard, to do so just ask to save your score, maybe you'll come out on top!"\
                    "To check the leaderboard just ask, who are the top players. If you want to know your position ask Alexa what position you are on the leaderboard."
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
    speech_output = "Welcome to the fruit machine game. you currently" \
                    " have £1. if you would like to play say Roll. If you'd like to quit, say Quit. If you need some" \
                    " tips,say help."
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
            'content': output
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