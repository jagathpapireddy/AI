
from itertools import product

def solve(title, p_text, q_text, r_text):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    print("P:", p_text)
    print("Q:", q_text)
    print("R:", r_text)

    print("\nTruth Table:")
    print("P Q R | P->Q Q->R | Premises | Conclusion")
    print("-" * 48)

    valid = True

    for P, Q, R in product([True, False], repeat=3):
        p_implies_q = (not P) or Q
        q_implies_r = (not Q) or R

        premises = p_implies_q and q_implies_r and P

        print(
            int(P), int(Q), int(R), " | ",
            int(p_implies_q), "   ",
            int(q_implies_r), "   | ",
            int(premises), "       | ",
            int(R)
        )

        if premises and not R:
            valid = False

    print("\nConclusion:")

    if valid:
        print("The argument is VALID.")
        print("Whenever all premises are true, the conclusion is true.")
    else:
        print("The argument is INVALID.")
        print("The premises can be true while the conclusion is false.")


solve(
    "Question 1: Rain and Road Accident",
    "It is raining",
    "The road becomes wet",
    "An accident may occur"
)

solve(
    "Question 2: Student and Degree",
    "The student studies",
    "The student passes the exam",
    "The student gets the degree"
)

print("\n" + "=" * 60)
print("FINAL CONCLUSION")
print("=" * 60)
print("Both arguments are VALID according to propositional logic.")
