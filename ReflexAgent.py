import random


class Object:
    def __repr__(self):
        return '<%s>' % getattr(self, 'name', self.__class__.__name__)


class Agent(Object):

    def __init__(self):
        def program(percept):
            pass
        self.program = program


loc_A, loc_B = 'A', 'B'


class vaccumEnvironemt(Object):


    def __init__(self):
        self.status = {
            loc_A: random.choice(['Clean', 'Dirty']),
            loc_B: random.choice(['Clean', 'Dirty'])
        }

    def add_object(self, agent, location=None):
        agent.location = location or self.default_location()

    def default_location(self):
        return random.choice([loc_A, loc_B])

    def percept(self, agent):
        return (agent.location, self.status[agent.location])

    def execute_action(self, agent, action):
        # if
        if action == 'Left':
            agent.location = loc_A
        elif action == 'Right':
            agent.location = loc_B
        elif action == 'Suck':
            self.status[agent.location] = 'Clean'


class simpleReflexVacuumAgent(Agent):

    def __init__(self, rules):

        Agent.__init__(self)

        def program(percept):
             
             ## ADD YOUR OWN CODE HERE
            action = rules.get(tuple(percept))

            print("Agent Has Perceived: ", percept, " And Performed Action: ", action)
            return action

        self.program = program

## WRITE YOUR OWN CODE HERE
class modelReflexVacuumAgent(Agent):

    def __init__(self, rules):

        Agent.__init__(self)
        model = {
            "A": "None",
            "B": "None"
        }

        def program(percept):

            model.update({percept})
            if model["A"] == "Clean" and model["B"] == "Clean":
                action = "No action"
            else:
                action = rules.get(tuple(percept))

            print("Agent Has Perceived: ", percept, " And Performed Action: ", action)
            return action

        self.program = program


def rulesSet():
    rules = {
        ('A', 'Clean'): 'Right',
        ('A', 'Dirty'): 'Suck',
        ('B', 'Clean'): 'Left',
        ('B', 'Dirty'): 'Suck',
    }
    return modelReflexVacuumAgent(rules)


# WRITE YOUR OWN CODE HERE


reflexAgent = rulesSet()
environment = vaccumEnvironemt()
environment.add_object(reflexAgent)
for x in range(20):
    action = reflexAgent.program(environment.percept(reflexAgent))
    environment.execute_action(reflexAgent, action)