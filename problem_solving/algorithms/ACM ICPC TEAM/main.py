# A slowly solution (timeout in several tests)
from itertools import combinations

def acmTeam(topic):
    amount_topics = len(topic[0])
    possibles = [number for number in range(0, len(topic))]
    comb = combinations(possibles, 2)
    amount_teams = 0
    max_topics = 0
    for i in list(comb):
        this_team = 0
        for number in range(0, amount_topics):
            if topic[i[0]][number] == 1 or topic[i[1]][number] == 1:
                this_team += 1
        if this_team >= max_topics:
            max_topics = this_team
    comb = combinations(possibles, 2)
    for t in list(comb):
        this_team = 0
        for number in range(0, amount_topics):
            if topic[t[0]][number] == 1 or topic[t[1]][number] == 1:
                this_team += 1
        if this_team == max_topics:
            amount_teams += 1
    print (max_topics, amount_teams)
    
# An effective solution using bit
def acmTeam(topic):
    topic_list = []
    for i in range(len(topic)-1):
        for j in range(i+1,len(topic)):
            result = int(topic[i], 2) | int(topic[j],2)
            topic_list.append(bin(result).count("1"))
    return (max(topic_list),topic_list.count(max(topic_list)))
