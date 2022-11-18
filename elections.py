# Name: Alisha Gursahaney
# Net Id: amg9zd

elections = {}
candidates = {}

def clear():
    global elections
    elections = {}
    global candidates
    candidates = {}


def add_state(name, votes):
    """
    adds the state name and winner to the elections dictionary
    also, adds the winning candidate names as keys in the candidates dictionary, defaulting their values/amount of electoral votes to zero
    :param name: name of the state being added
    :param votes: the dictionary of the amount of votes each candidate received in that state
    :return: elections dictionary with state names and winners, candidates dictionary with winning candidates and zero values
    """
    highest_votes = 0
    top_candidate = ''
    for results in votes:
        if votes[results] > highest_votes:
            highest_votes = votes[results]
            top_candidate = results
    elections[name] = top_candidate
    for state in elections:
        candidates[elections[state]] = 0


def winner(college):
    """
    adds electoral votes for each candidate (from each of their state wins to total their electoral votes)
    decides if their is a winner depending on if the winning candidate has the minimum amount of electoral votes (50%)
    :param college: the dictionary of states and their designated amount of electoral votes
    :return: the winner of the election
    """
    total_electoral_votes = 0
    for state in elections:
        if state in college:
            state_candidate = elections[state]
            electoral_votes = college[state]
            total_electoral_votes += electoral_votes
            candidates[state_candidate] += electoral_votes
    highest_vote = 0
    top_candidate = ''
    for results in candidates:
        if candidates[results] > highest_vote:
            highest_vote = candidates[results]
            top_candidate = results
    if highest_vote > (0.5 * total_electoral_votes):
        return top_candidate
    else:
        return "No Winner"
