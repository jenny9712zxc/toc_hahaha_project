from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_state1(self, text):
        return text.lower() == 'go to state1'

    def is_going_to_state2(self, text):
        return text.lower() == 'go to state2'

    def is_going_to_state3(self, text):
        return text.lower() == 'go to state3'

    def is_going_to_state4(self, text):
        return text.lower() == 'go to state4'

    def is_going_to_state5(self, text):
        return text.lower() == 'go to state5'

    def is_going_to_state6(self, text):
        return text.lower() == 'go to state6'

    def is_going_to_go_back(self, text):
        return text.lower() == 'go back'


    def on_enter_state1(self, event):
        print("I'm entering state1")
        print('CURRENT STATE: ' + machine.state)
        self.go_back()

    def on_exit_state1(self):
        print('Leaving state1')


    def on_enter_state2(self, event):
        print("I'm entering state2")
        print('CURRENT STATE: ' + machine.state)
        self.go_back()

    def on_exit_state2(self):
        print('Leaving state2')


    def on_enter_state3(self, event):
        print("I'm entering state3")
        print('CURRENT STATE: ' + machine.state)
        self.go_back()

    def on_exit_state3(self):
        print('Leaving state3')


    def on_enter_state4(self, event):
        print("I'm entering state4")
        print('CURRENT STATE: ' + machine.state)
        #self.go_back()

    def on_exit_state4(self,event):
        print('Leaving state4')


    def on_enter_state5(self, event):
        print("I'm entering state5")
        print('CURRENT STATE: ' + machine.state)
        #self.go_back()

    def on_exit_state5(self,event):
        print('Leaving state5')


    def on_enter_state6(self, event):
        print("I'm entering state6")
        print('CURRENT STATE: ' + machine.state)
        self.go_back()

    def on_exit_state6(self,event):
        print('Leaving state6')





machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2',
        'state3',
        'state4',
        'state5',
        'state6'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state4',
            'conditions': 'is_going_to_state4'
        },
        {
            'trigger': 'advance',
            'source': 'state4',
            'dest': 'state5',
            'conditions': 'is_going_to_state5'
        },
        {
            'trigger': 'advance',
            'source': 'state5',
            'dest': 'state6',
            'conditions': 'is_going_to_state6'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state1',
                'state2',
                'state3',
                'state4',
                'state5',
                'state6'
            ],
            'dest': 'user'
        },
        {
            'trigger': 'advance',
            'source': [
                'state1',
                'state2',
                'state3',
                'state4',
                'state5',
                'state6'
            ],
            'dest': 'user',
            'conditions': 'is_going_to_go_back'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


if __name__ == "__main__":
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    while True:
        text = input('input: ')
        print('---')
        print('LAST STATE: ' + machine.state)        

        machine.advance(text)
        print('FINAL STATE: ' + machine.state)
        print('---')
