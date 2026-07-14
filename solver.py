from decision_node import DecisionNode
from poker import is_game_done, profit, get_possible_decisions


'''
DecisionTree stores every DecisionNode created during the iterations
Keys in the dictionary are connected strings representing decisions so far and the card of the
player on move
'''
DecisionTree={}

def solver(cards, decisions, pr):
    '''
    cards: 2 element list with Player1's card and Player2's card
    decisions: a string representing the decisions made during the game so far
    pr: 2 element list with probabilities of each player to reach a given state under their strategy (considered separately)
    
    Returns: the expected value of the game from the perspective of the player on move 
    '''
    if is_game_done(decisions):
        return profit(decisions, cards)
    
    else:
        list_of_decisions = decisions.split("-")
        player_on_move = len(list_of_decisions)%2
        # "".split("-") returns [''] (a list with one empty string), not an empty list,
        # so len() would incorrectly give 1 instead of 0 for the very first move of the game.
        # Player 1 always moves first, so we need to explicitly override this edge case.
        if(decisions==""):
            player_on_move=0

        key = cards[player_on_move] + decisions #both are strings so we can do it
        if key not in DecisionTree:
            DecisionTree[key]=DecisionNode(get_possible_decisions(decisions))
        
        DN=DecisionTree[key]
        strategy = DN.choose_decision(pr[player_on_move])
        decision_values={}

        for Dec in get_possible_decisions(decisions):
            if len(decisions)==0:
                new_decision = Dec
            else:
                new_decision = decisions+"-"+Dec
        
            new_pr=[pr[0], pr[1]]
            new_pr[player_on_move]*=strategy[Dec]

            decision_values[Dec] = -solver(cards, new_decision, new_pr)
        
        node_value = sum(strategy[Dec] * decision_values[Dec]
        for Dec in get_possible_decisions(decisions))

        opponent = (player_on_move+1)%2
        
        for Dec in get_possible_decisions(decisions):
            regret = decision_values[Dec] - node_value
            DN.regret_so_far[Dec] += pr[opponent] * regret

        return node_value 


