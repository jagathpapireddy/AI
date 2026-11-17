
import re

def is_variable(term):
    return isinstance(term, str) and term[0].islower()


def apply_substitution(term, theta):
    if isinstance(term, str):
        while term in theta:
            term = theta[term]
        return term

    name, args = term
    return (name, tuple(apply_substitution(arg, theta) for arg in args))


def occurs(var, term, theta):
    term = apply_substitution(term, theta)

    if term == var:
        return True

    if isinstance(term, tuple):
        return any(occurs(var, arg, theta) for arg in term[1])

    return False


def unify(t1, t2, theta):

    t1 = apply_substitution(t1, theta)
    t2 = apply_substitution(t2, theta)

    if t1 == t2:
        return theta

    if is_variable(t1):
        if occurs(t1, t2, theta):
            return None
        theta[t1] = t2
        return theta

    if is_variable(t2):
        if occurs(t2, t1, theta):
            return None
        theta[t2] = t1
        return theta

    if isinstance(t1, tuple) and isinstance(t2, tuple):

        if t1[0] != t2[0] or len(t1[1]) != len(t2[1]):
            return None

        for a, b in zip(t1[1], t2[1]):
            theta = unify(a, b, theta)

            if theta is None:
                return None

        return theta

    return None


def parse(expression):
    tokens = re.findall(r'[A-Za-z_]\w*|[(),]', expression)
    pos = 0

    def read():
        nonlocal pos

        name = tokens[pos]
        pos += 1

        if pos < len(tokens) and tokens[pos] == '(':
            pos += 1
            args = []

            while True:
                args.append(read())

                if tokens[pos] == ')':
                    pos += 1
                    break

                pos += 1

            return (name, tuple(args))

        return name

    return read()


questions = [
    ("Knows(x,y)", "Knows(Ram,Sita)",
     "Substitute x with Ram and y with Sita."),

    ("P(f(x),y)", "P(f(Ram),Sita)",
     "Match f(x) with f(Ram) and y with Sita."),

    ("P(x,x)", "P(Ram,y)",
     "Substitute x with Ram and y with Ram."),

    ("P(f(x),g(y))", "P(f(Ram),g(Sita))",
     "Match corresponding function arguments."),

    ("P(x)", "P(f(x))",
     "Unification fails because x occurs inside f(x) (Occurs Check).")
]


for i, (a, b, explanation) in enumerate(questions, 1):

    t1 = parse(a)
    t2 = parse(b)

    theta = unify(t1, t2, {})

    print("\nQuestion", i)
    print("Expression 1:", a)
    print("Expression 2:", b)

    if theta is None:
        print("Theta = Unification Failed")
    else:
        print("Theta =", theta)

    print("Explanation:", explanation)
