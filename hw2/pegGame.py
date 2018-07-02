class Game:
    def __init__(self, m=4, n=4, state=None, start=9):
        self.m = m
        self.n = n
        self.numPegs = m * n
        self.start = start

        if state:
            self.boardState = state
        else:
            self.boardState = (pow(2, self.numPegs) - 1) - pow(2, self.start)


    def goal(self, state=None):
        if state == None:
            state = self.boardState

        # if there is one instance of '0' and it is in index self.start
        if state == pow(2, self.start):
            return True
        else:
            return False

    def softApplyRule(self, rule, state=None):

        if state == None:
            state = self.boardState

        binState = format(state, '0' + str(self.numPegs) + 'b')

        if self.precondition(rule=rule):
            results = self.boardState - pow(2, rule[0]) - pow(2, rule[1]) + pow(2, rule[2])
        return results

    def applyRule(self, rule, state=None):

        if state == None:
            state = self.boardState

        binState = format(state, '0' + str(self.numPegs) + 'b')

        if self.precondition(rule=rule):
            self.boardState = self.boardState - pow(2, rule[0]) - pow(2, rule[1]) + pow(2, rule[2])
        return self.boardState

    def precondition(self, rule, state=None):
        if state == None:
            state = self.boardState

        binState = format(state, '0' + str(self.numPegs) + 'b')

        try: # Check Peg values
            if binState[(self.numPegs - 1) - rule[0]] == '1' and binState[(self.numPegs - 1) - rule[1]] == '1' and binState[(self.numPegs - 1) - rule[2]] == '0': #check for valid peg type
                if rule[1] - (rule[0] - rule[1]) == rule[2] and (rule[0] - rule[1]) == self.m and rule[0] / self.m >= 2: #up
                    return True
                elif (rule[1] - rule[0]) + rule[1] == rule[2] and (rule[1] - rule[0]) == self.m and rule[0] / self.m <= self.n - 3: #down
                    return True
                elif rule[1] - (rule[0] - rule[1]) == rule[2] and (rule[0] - rule[1]) == 1 and rule[0] % self.m >= 2: #left
                    return True
                elif (rule[1] - rule[0]) + rule[1] == rule[2] and (rule[1] - rule[0]) == 1 and rule[0] % self.m <= 2: #right
                    return True
                elif rule[1] - (rule[0] - rule[1]) == rule[2] and (rule[0] - rule[1]) == self.m - 1 and rule[0] / self.m >= 2 and rule[0] % self.m <= 2: #up-right
                    return True
                elif rule[1] - (rule[0] - rule[1]) == rule[2] and (rule[0] - rule[1]) == self.m + 1 and rule[0] / self.m >= 2 and rule[0] % self.m >= 2: #up-left
                    return True
                elif (rule[1] - rule[0]) + rule[1] == rule[2] and (rule[1] - rule[0]) == self.m + 1 and rule[0] / self.m <= self.n - 3 and rule[0] % self.m <= 2: #down-right
                    return True
                elif (rule[1] - rule[0]) + rule[1] == rule[2] and (rule[1] - rule[0]) == self.m - 1 and rule[0] / self.m <= self.n - 3 and rule[0] % self.m >= 2: #down-left
                    return True
                else:
                    return False
        except IndexError:
            print "Invalid Rule: A rule parameter has an invalid index"


    def applicableRules(self,state=None):
        if state == None:
            state = self.boardState

        allRules = []

        for i in range(self.numPegs):
            for j in range(self.numPegs):
                for k in range(self.numPegs):
                    if self.precondition([i, j, k]):
                        allRules.append([i, j, k])

        return allRules



    # display reference numbers for board
    def refBoard(self):
        print '-' * (5 + (self.m * 4))
        print '|',
        for peg in reversed(range(self.numPegs)):
            print str(peg).zfill(2) + ' |',

            if peg % self.m == 0:
                print ''
                print '-' * (5 + (self.m * 4))
                if peg != 0:
                    print '|',

    # display numbers for board
    def describeState(self, state=None):
        if state == None:
            state = self.boardState

        for i, peg in enumerate(format(state, '0' + str(self.numPegs) + 'b')):
           if int(i) % self.m == 0:
                print ''
                print '-' * (5 + (self.m * 3))
                if peg != 0:
                    print '|',

           if peg == '1':
               print 'X |',
           elif peg == '0':
               print 'O |',

        print ''
        print '-' * (5 + ((self.m - 1) * 4))

    def describeRule(self, rule):
        if len(rule) == 3:
            print "The peg in slot {} jumps over the peg in slot {} and lands in slot {}.".format(rule[0], rule[1], rule[2])
def main():
    game = Game()

if __name__ == '__main__':
    main()
