class Plugboard:

    def __init__(self, pairs):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for pair in pairs:
            A = pair[0]
            B = pair[1]
            position_A = self.left.find(A)
            position_B = self.left.find(B)
            self.left = self.left[:position_A] + B + self.left[position_A+1:]
            self.left = self.left[:position_B] + A + self.left[position_B+1:]

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal