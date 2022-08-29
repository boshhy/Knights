from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A is either a Knight or a Knave
    Or(AKnight, AKnave),
    # A is not both a Knight and a Knave
    Not(And(AKnight, AKnave)),

    # If A is a Knight then "I am both a knight and a knave." is true.
    Implication(AKnight, And(AKnight, AKnave)),
    # If A is a Knave then "I am both a knight and a knave." is false.
    Implication(AKnave, Not(And(AKnight, AKnave)))
)


# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A is either a Knight or a Knave
    Or(AKnight, AKnave),
    # A is not both a Knight and a Knave
    Not(And(AKnight, AKnave)),
    # B is either a knight or kanve
    Or(BKnight, BKnave),
    # B is not both a Knight and Knave
    Not(And(BKnight, BKnave)),

    # If A is a Knight then "We are both knaves." is true.
    Implication(AKnight, And(AKnave, BKnave)),
    # If A is a Knave then "We are both knaves." if false
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A is either a Knight or a Knave
    Or(AKnight, AKnave),
    # A is not both a Knight and a Knave
    Not(And(AKnight, AKnave)),
    # B is either a knight or kanve
    Or(BKnight, BKnave),
    # B is not both a Knight and Knave
    Not(And(BKnight, BKnave)),

    # If A is a Knight then "We are the same kind." is true.
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    # If A is a Knave then "We are the same kind." is flase.
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),

    # If B is a Knight then "We are of different kinds." is true.
    Implication(BKnight, Or(And(AKnight, BKnave), And(BKnight, AKnave))),
    # If B is a Knave then "We are of different kinds." is false.
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(BKnight, AKnave))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A is either a Knight or a Knave
    Or(AKnight, AKnave),
    # A is not both a Knight and a Knave
    Not(And(AKnight, AKnave)),
    # B is either a knight or kanve
    Or(BKnight, BKnave),
    # B is not both a Knight and Knave
    Not(And(BKnight, BKnave)),
    # C is either a knight or kanve
    Or(CKnight, CKnave),
    # C is not both a Knight and a Knave
    Not(And(CKnight, CKnave)),

    # If A is a Knight then "I am a knight." or "I am a knave." if true.
    Implication(AKnight, Or(AKnight, AKnave)),
    # If A is a Knave then "I am a knight." or "I am a knave." if False.
    Implication(AKnave, Not(Or(AKnight, AKnave))),

    # If B is a Knight then -> A is  a Knight and B is a Knave
    Implication(BKnight, Implication(AKnight, BKnave)),
    # If B is a Knave then -> A is  a Knave and B is a knight
    Implication(BKnave, Implication(AKnave, BKnight)),

    # If B is a Knight then "C is a knave." is true.
    Implication(BKnight, CKnave),
    # If B is a Knave then "C is a knave." is false.
    Implication(BKnave, Not(CKnave)),

    # If C is a Knight then "A is a knight." is true.
    Implication(CKnight, AKnight),
    # If C is a Knave then "A is a knight." is false.
    Implication(CKnave, Not(AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
