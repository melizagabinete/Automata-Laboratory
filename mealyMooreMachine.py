class Process:
    def __init__(self):
        self.state = None
        self.accepted = False

    def reset(self):
        self.state = self.initial_state
        self.accepted = False

    def process(self, input_str):
        raise NotImplementedError("Subclasses must implement this method")

    def is_accepted(self):
        return "Accepted" if self.accepted else "Rejected"


class MooreMachine(Process):
    def __init__(self):
        super().__init__()
        self.initial_state = 'A'
        self.state = 'A'
        self.outputs = {'A': 'b', 'B': 'b', 'C': 'a'}

    def transition(self, inp):
        if self.state == 'A':
            if inp == '0':
                self.state = 'B'
            else:
                self.state = 'A'

        elif self.state == 'B':
            if inp == '1':
                self.state = 'C'
                self.accepted = True
            else:
                self.state = 'B'

        elif self.state == 'C':
            if inp == '0':
                self.state = 'B'
            else:
                self.state = 'A'

        return self.outputs[self.state]

    def process(self, input_str):
        output = [self.outputs[self.state]]
        for bit in input_str:
            output.append(self.transition(bit))
        return ''.join(output)

    def get_steps(self, input_str):
        steps = []
        current_state = self.state
        steps.append({'input': '', 'output': self.outputs[current_state], 'state': current_state})
        for bit in input_str:
            output = self.transition(bit)
            steps.append({'input': bit, 'output': output, 'state': self.state})
        return steps


class MealyMachine(Process):
    def __init__(self):
        super().__init__()
        self.initial_state = 'A'
        self.state = 'A'

    def transition(self, inp):
        if self.state == 'A':
            if inp == '0':
                self.state = 'B'
                return 'b'
            else:
                self.state = 'A'
                return 'b'

        elif self.state == 'B':
            if inp == '1':
                self.state = 'C'
                self.accepted = True
                return 'a'  
            else:
                self.state = 'B'
                return 'b'

        elif self.state == 'C':
            if inp == '0':
                self.state = 'B'
            else:
                self.state = 'A'
            return 'b'

    def process(self, input_str):
        output = []
        for bit in input_str:
            output.append(self.transition(bit))
        return ''.join(output)

    def get_steps(self, input_str):
        steps = []
        for bit in input_str:
            output = self.transition(bit)
            steps.append({'input': bit, 'output': output, 'state': self.state})
        return steps


if __name__ == "__main__":
    def print_table(machine_name, input_str, steps, accepted):
        print(f"\n{machine_name} - Input: {input_str}")
        print("+-------+-------+-------+")
        print("| Input | State | Output|")
        print("+-------+-------+-------+")
        for step in steps:
            print(f"| {step['input']:5} | {step['state']:5} | {step['output']:5} |")
        print("+-------+-------+-------+")
        print(f"Result: {accepted}")

    while True:
        print("\nOptions:")
        print("1. Display Moore Machine")
        print("2. Display Mealy Machine")
        print("3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == '4':
            break
        elif choice in ['1', '2']:
            input_str = input("Enter a binary string (only 0s and 1s): ").strip()
            if not all(c in '01' for c in input_str):
                print("Invalid input. Please try again.")
                input_str = input("Enter a binary string (only 0s and 1s): ").strip()
                if not all(c in '01' for c in input_str):
                    print("Invalid input again. Exiting.")
                    break
            table_mode = input("Do you want to display in table format? (y/n): ").lower() == 'y'
            if choice == '1':
                machine = MooreMachine()
                machine_name = "Moore Machine"
            else:
                machine = MealyMachine()
                machine_name = "Mealy Machine"
            if table_mode:
                steps = machine.get_steps(input_str)
                print_table(machine_name, input_str, steps, machine.is_accepted())
            else:
                result = machine.process(input_str)
                print(f"Input: {input_str} - Output: {result}, {machine.is_accepted()}")
        else:
            print("Invalid option. Please choose 1, 2, or 3.")
