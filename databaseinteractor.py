import pymongo
from pymongo import MongoClient

cluster = MongoClient(
    "mongodb+srv://fruitmachine:BcIzoGj60y2SQUGC@cluster0.pudch.mongodb.net/scores?retryWrites=true&w=majority")
db = cluster.Scores
posts = db.Score


def make_ordinal(n):
    n = int(n)
    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    return str(n) + suffix


def sort(scores, userids, names):
    n = len(scores)
    print(scores)
    print(names)
    for _ in range(n - 1):
        flag = 0
        for j in range(n - 1):
            if scores[j] > scores[j + 1]:
                print("sort")
                tmp = scores[j]
                tmp2 = names[j]
                tmp3 = userids[j]
                scores[j] = scores[j + 1]
                names[j] = names[j + 1]
                userids[j] = userids[j + 1]
                names[j+1] = tmp2
                userids[j+1] = tmp3
                scores[j+1] = tmp
                flag = 1
        if flag == 0:
            break
    return scores, userids, names


def new_entry(userid, score ,name):
    post = {"_id": userid,
            "score": score,
            "name":name
            }
    print("pushing now")
    posts.insert_one(post)
    check = find_entry(userid)
    if not check:
        return False
    else:
        return True


def find_entry(userid):
    try:
        score = posts.find_one({"_id": userid})
    except:
        score = None
    if score == None:
        return False
    else:
        print(score)
        return score["score"], score["name"]

def get_top_player():
    scores = []
    userids = []
    names = []
    for post in posts.find():
        scores.append(post["score"])
        userids.append(post["_id"])
        names.append(post["name"])
    scores, userids, names = sort( scores, userids, names)
    top5scores = []
    top5names = []
    print(scores)
    print(names)
    if scores == "":
        return False
    elif len(scores) > 5:
        for i in range(0, 4):
            top5scores.append(scores[i])
            top5names.append(names[i])
            print(names[i])
    else:
        top5scores = scores
        top5names = names
    response = "Here are the top 5 scores. "
    i = len(top5scores)
    for item in top5scores:
        response = response+str(len(top5scores) - i + 1)+" . "+str(top5names[i-1])+" with a score of £"+str(top5scores[i-1])+". "
        i = i-1
    return response


def get_leaderboard_position(userid):
    scores = []
    userids = []
    names = []
    for post in posts.find():
        scores.append(post["score"])
        userids.append(post["_id"])
        names.append(post["name"])
    scores,userids, names = sort(scores, userids, names)
    try:
        location = userids.index(userid)+1
    except:
        return "We did not find a high score under your name, are you sure you've saved one? To save a score, say 'save my score'. "
    score = scores[location-2]
    position = make_ordinal(location)
    response = "You have the top score of £"+str(score)+". You are the "+str(position)+". 'Say who are the top players'" \
                                                                                       " to see the highest scores."
    return response


def check_score(userid,money):
    score = find_entry(userid)
    current_score = score[0]
    print(current_score)
    print(money)
    if int(money) < int(current_score):
        return False
    else:
        return True


def update_score(userid,score, name):
    posts.update_one({"_id":userid}, {"$set":{"score":score}})
    posts.update_one({"_id":userid},{"$set":{"name":name}})
    score2 = find_entry(userid)
    if score == score2:
        return True
    else:
        return False

f = get_top_player()
print(f)