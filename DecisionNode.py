class DecisionNode:
    def __init__(self, possible_decisions):
        '''
        possible decisions: a 2-element list of possible moves 
        (will use get_possible_decisions from poker.py)
        '''
        self.possible_decisions=possible_decisions
        self.regret_so_far={decision: 0 for decision in possible_decisions}
        self.strategy_distribution={decision: 0 for decision in possible_decisions}

    
    def choose_decision(self, probability_of_the_state):
        '''
        probability_of_the_state: float from [0,1] stating the probability of reaching this state
        Returns: result - a dictionary with decisions as keys and their probability as values
        
        
        
        >>> node = DecisionNode(["bet", "check"])
        >>> node.choose_decision(1.0)
        {'bet': 0.5, 'check': 0.5}

        >>> node2 = DecisionNode(["bet", "check"])
        >>> node2.regret_so_far = {"bet": 30, "check": -10}
        >>> node2.choose_decision(1.0)
        {'bet': 1.0, 'check': 0.0}
        '''
        result={}
        #we only take positive regrets because regret is positive <=> we should do this decision more often
        decisions_with_positive_regret={
            decision: max(0, self.regret_so_far[decision])
            for decision in self.possible_decisions
        }

        total_regret = sum(decisions_with_positive_regret.values())

        if total_regret==0:
            result = {
                decision : 1/len(self.possible_decisions)
                for decision in self.possible_decisions
                #if no data so far, each decision gets equal probability
            }
        else:
            result = {
                decision: decisions_with_positive_regret[decision] / total_regret
                for decision in self.possible_decisions
            }

        for decision in self.possible_decisions:
            self.strategy_distribution[decision] += probability_of_the_state*result[decision]

        return result


    def compute_average_strategy(self):
        '''
        Returns: result - a dictionary with decisions as keys
        and their average probability across all iterations so far

        >>> node = DecisionNode(["bet", "check"])
        >>> node.compute_average_strategy()
        {'bet': 0.5, 'check': 0.5}

        >>> node2 = DecisionNode(["bet", "check"])
        >>> node2.strategy_distribution = {"bet": 70, "check": 30}
        >>> node2.compute_average_strategy()
        {'bet': 0.7, 'check': 0.3}
        '''
        result = {}
        total = sum(self.strategy_distribution.values())

        if total == 0:
            result = {
                decision: 1/len(self.possible_decisions)
                for decision in self.possible_decisions
            }
        else:
            result = {
                decision: self.strategy_distribution[decision] / total
                for decision in self.possible_decisions
            }

        return result
        