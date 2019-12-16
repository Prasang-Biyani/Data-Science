training_data = [
    ['Green', 3, 'Apple'],
    ['Yellow', 3, 'Apple'],
    ['Red', 1, 'Grape'],
    ['Red', 1, 'Grape'],
    ['Yellow', 3,'Green']
]

# Column Labels
header = ['color', 'diameter', 'label']

def unique_vals(rows, col):
    return set([row[col] for row in rows])

# Count the number of items in a given class
def class_counts(rows):
    counts = {}
    for row in rows:
        label = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts
# print(class_counts(training_data))

def is_numeric(value):
    return isinstance(value, int) or isinstance(value, float)

# print(is_numeric(7))

class Question:

    def __init__(self, column, value):
        self.column = column
        self.value = value

    def match(self, example):
        val = example[self.column]
        if is_numeric(val):
            return val >= self.value
        else:
            return val == self.value

    def __repr__(self):
        # helper method to print questions in a reaaable format.
        condition = "=="
        if is_numeric(self.value):
            condition = ">="
        return "Is %s %s %s?" % (
            header[self.column], condition, str(self.value)
        )

# print(Question(1, 2))
q = Question(0, 'Green')
# print(q)

example = training_data[0]
# print(example)
# print(q.match(example))

def partition(rows:list, question):
    """ Partitions a dataset

    For each row in the dataset, check if it matches the question.
    If so, add it to 'true_rows', otherwise, add it to 'false rows'.
    """

    true_rows, false_rows = [], []
    for row in rows:
        if question.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)

    return true_rows, false_rows

# true_rows, false_rows = partition(training_data, Question(1, 3))
# print(false_rows)

def gini(rows):
    """Calculates the Gini Impurity for a list of rows
    """

    counts = class_counts(rows)
    impurity = 1
    for lbl in counts:
        prob_of_labl = counts[lbl] / float(len(rows))
        impurity -= prob_of_labl**2
    return impurity

# test_gini = [['Yellow'], ['Apple'], ['Orange'], ['Green']]
# print(gini(test_gini))

def info_gain(left, right, current_uncertainity):
    """Information Gain.
    
    The uncertainity of the starting node, minuts the weighted impurity of two child nodes
    """

    p = float(len(left)) / (len(left) + len(right))
    return current_uncertainity - p * gini(left) - (1 - p) * gini(right)

current_uncertainity = gini(training_data)
# print(current_uncertainity)

# How much information do we gain by partioning on 'Green'?
# true_green, false_green = partition(training_data, Question(0, 'Green'))
# print('Information Gain(Green): ', info_gain(true_green, false_green, current_uncertainity))

# true_red, false_red = partition(training_data, Question(0, 'Red'))
# print('Information Gain(Red): ', info_gain(true_red, false_red, current_uncertainity))

# true_yellow, false_yellow = partition(training_data, Question(0, 'Yellow'))
# print('Information Gain(Yellow): ', info_gain(true_yellow, false_yellow, current_uncertainity))

def find_best_split(rows):
    """Finds the best question to ask by iterating over every feature / value
    and calculating the information gain"""
    
    best_gain = 0
    best_question = 0
    current_uncertainity = gini(rows)
    n_features = len(rows[0]) - 1
    for col in range(n_features):
        values = set([row[col] for row in rows])
        # {'Apple', 3}
        for val in values:
            question = Question(col, val)
            true_rows, false_rows = partition(rows, question)
            if len(true_rows) == 0 or len(false_rows) == 0:
                continue
            gain = info_gain(true_rows, false_rows, current_uncertainity)
            if gain >= best_gain:
                best_gain, best_question = gain, question
    return best_gain, best_question

best_gain, best_question = find_best_split(training_data)

class Leaf:
    """A leaf nodes classifies data. 
    This holds a dictionary of class (e.g., "Apple") -> number of times
    it appears in the rows from the training data that reaches the leaf.
    """

    def __init__(self, rows):
        self.predictions = class_counts(rows)

class Decision_Node:
    """ A Decision Node asks a question.
    This holds a reference to the question, and to the two child nodes.
    """

    def __init__(self, question, true_branch, false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch

def build_tree(rows):

    """Builds the tree

        Rules of recursion: 
        1) Believe that it works.
        2) Start by checking for the base case (no futher information gain).
        3) Prepare for giant stack traces.
        """

    gain, question = find_best_split(rows)
    # Base case: no further info gain
    # Since we can ask no further questions,
    # we'll return a leaf.
    if gain == 0:
        return Leaf(rows)
    # If we reach here, we have found a useful feature / value
    # to perform partition
    true_rows, false_rows = partition(rows, question)

    # Recursively build the true branch
    true_branch = build_tree(true_rows)

    # Recursively build the false branch
    false_branch = build_tree(false_rows)

    # Retur a Question node.
    # This records the best feature / value to ask at this point,
    # as well as the branches to follow
    # depend on the answer 
    return Decision_Node(question, true_branch, false_branch)

def print_tree(node, spacing=""):
    """World's most elegant tree printing function."""
    # Base case: we've reached a leaf
    if isinstance(node, Leaf):
        print(spacing + "Predict", node.predictions)
        return 

    # Print the question at this node
    print(spacing + str(node.question))

    # Call this function recursively on the true branch
    print(spacing + '--> True:')
    print_tree(node.true_branch, spacing + " ")

    # Call this function recursively on the false branch
    print(spacing + '--> False:')
    print_tree(node.false_branch, spacing + " ")

my_tree = build_tree(training_data)
# print_tree(my_tree)

def classify(row, node):
    """See the 'rules of recursion' above."""

    # Base case: we've reached a Leaf
    if isinstance(node, Leaf):
        return node.predictions

    # Decide whether to follow the true-branch or the false-branch.
    # Compare the feature / value stored in the node, 
    # to the example we're considering
    if node.question.match(row):
        return classify(row, node.true_branch)
    else:
        return classify(row, node.false_branch)
    
# print(classify(training_data[0], my_tree))

def print_leaf(counts):
    """A nicer way to print the predictions at a leaf."""
    total = sum(counts.values()) * 1.0
    probs = {}
    for lbl in counts.keys():
        probs[lbl] = str(int(counts[lbl] / total * 100)) +  "%"
    return probs

# print(print_leaf(classify(training_data[0], my_tree)))
testing_data = [
    ['Green', 3, 'Apple'],
    ['Yellow', 4, 'Apple'],
    ['Red', 2, 'Grape'],
    ['Red', 1, 'Grape'],
    ['Yellow', 3, 'Lemon'],
]

for row in testing_data:
    print ("Actual: %s. Predicted: %s" %
           (row[-1], print_leaf(classify(row, my_tree))))

