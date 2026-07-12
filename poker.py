#Cards in Kuhn Poker: Jack, Queen, King

def is_game_done(decisions):
    '''
    decisions: a string that tracks the history of the game (consists of check/s, bet/s, and fold/s)
    '''
    possible_endings = ["bet-call", "bet-fold", "check-check", 
    "check-bet-call", "check-bet-fold"]
    if decisions in possible_endings:
        return True
    else:
        return False

def get_possible_decisions(decisions):
    '''
    decisions: a string that tracks the history of the game (consists of check/s, bet/s, and fold/s)
    '''
    if len(decisions)==0:
        return ["bet", "check"]
    list_of_decisions = decisions.split("-")
    if list_of_decisions[-1]=="bet":
        return ["call", "fold"]
    elif list_of_decisions[-1]=="check":
        return ["bet", "check"]

def profit(decisions, players_cards):
    '''
    decisions: a string that tracks the history of the game (consists of check/s, bet/s, and fold/s)
    players_cards: a 2-element list containing Player1's card at 0th index and Player2's card at 1st index
    '''
    list_of_decisions = decisions.split("-")
    player_on_move = len(list_of_decisions)%2
    
    if list_of_decisions[-1]=="fold":
        return 1

    else:
        stake = 1 #case without betting
        if "bet" in list_of_decisions:
            stake = 2 #case with bettting

        #showdown analysis
        player_on_move_card=players_cards[player_on_move]
        opponent_card=players_cards[(1+player_on_move)%2]

        if player_on_move_card=="King":
            return stake
        elif player_on_move_card=="Queen":
            if opponent_card=="Jack":
                return stake
            else: #opponent has a King
                return -stake
        else: #player on move has a Jack
            return -stake


            


