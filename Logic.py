class Logic:
    def __init__(self, values):
        self.min_value = min(values)
        self.max_value = max(values)
        self.n = len(values)

        self.stack_a = values
        self.stack_b = []

    def _push(self, stack_from, stack_to):
        if stack_from:
            value = stack_from.pop(0)
            stack_to.insert(0, value)

    def _rotate(self, stack):
        if stack:
            value = stack.pop(0)
            stack.append(value)

    def _reverse_rotate(self, stack):
        if stack:
            value = stack.pop()
            stack.insert(0, value)

    def pa(self):
        self._push(self.stack_b, self.stack_a)

    def pb(self):
        self._push(self.stack_a, self.stack_b)

    def ra(self):
        self._rotate(self.stack_a)
    
    def rb(self):
        self._rotate(self.stack_b)

    def rr(self):
        self.ra()
        self.rb()

    def rra(self):
        self._reverse_rotate(self.stack_a)
    
    def rrb(self):
        self._reverse_rotate(self.stack_b)

    def rrr(self):
        self.rra()
        self.rrb()
