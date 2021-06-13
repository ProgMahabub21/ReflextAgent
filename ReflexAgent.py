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

    # status = {
    #     loc_A: random.choice(['Clean', 'Dirty']),
    #     loc_B: random.choice(['Clean', 'Dirty'])
    # }

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
        if action == 'Right':
            agent.location = loc_B
        elif action == 'Left':
            agent.location = loc_A
        elif action == 'Suck':
            self.status[agent.location] = 'Clean'


class simpleReflexVacuumAgent(Agent):

    def __init__(self, rules):

        Agent.__init__(self)

        def program(percept):

            action = rules.get(tuple(percept))

            print("Agent Has Perceived: ", percept,
                  " And Performed Action: ", action)
            return action

        self.program = program


class simpleModelReflexVacuumAgent(Agent):

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

            print("Agent Has Perceived: ", percept,
                  " And Performed Action: ", action)
            return action

        self.program = program


def getRules():
    rules = {
        ('A', 'Clean'): 'Right',
        ('A', 'Dirty'): 'Suck',
        ('B', 'Clean'): 'Left',
        ('B', 'Dirty'): 'Suck',
    }
    return simpleModelReflexVacuumAgent(rules)


# WRITE YOUR OWN CODE HERE


rAgent = getRules()
env = vaccumEnvironemt()
env.add_object(rAgent)
for x in range(20):
    action = rAgent.program(env.percept(rAgent))
    env.execute_action(rAgent, action)
