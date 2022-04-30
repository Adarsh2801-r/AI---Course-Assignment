'''
If an honest politician has given a promise he keeps the promise. If a party has given a promise,
and a person is a leader of the party, then that means the person has given a promise. If the person
keeps his promise and he is the leader of the party then the party keeps its promise. If a person is
the leader of a party then the person is a politician. Party ABCD makes a promise P1. ABCD did
not keep the promise P1. The leader of the party ABCD is XYZ . XYZ is a person
'''
'''
First order logic

person(x) : x is a person
politician(x) : x is a politician
givePromise(x,y) : x made a promise y
keepPromise(x,y): x keeps promise y
party(x) : x is party
leader(x,y) : x is leader of y
honest(x) : x is honest
promise(x) : x is a promise
Constants : ABCD , P1 , XYZ
'''

import aima.utils
import aima.logic
# The main entry point for this module
def main():
    # Create an array to hold clauses
    clauses = []
    # Add first-order logic clauses (rules and fact)
    clauses.append(aima.utils.expr("(person(x) & politician(x) & honest(x) & promise(y) & givePromise(x, y)) ==> keepPromise(x, y)"))
    clauses.append(aima.utils.expr("(person(x) & party(z) & promise(y) & givePromise(z, y) & leader(x, z)) ==> givePromise(x, y)"))
    clauses.append(aima.utils.expr("(person(x) & party(z) & promise(y) & keepPromise(x, y) & leader(x, z)) ==> keepPromise(z, y)"))
    clauses.append(aima.utils.expr("(person(x) & party(z) & leader(x, z)) ==> politician(x)"))

    # Create a first-order logic knowledge base (KB) with clauses
    KB = aima.logic.FolKB(clauses)
    # Add rules and facts with tell
    KB.tell(aima.utils.expr("party(ABCD)"))
    KB.tell(aima.utils.expr("promise(P1)"))
    KB.tell(aima.utils.expr("givePromise(ABCD, P1)"))
    KB.tell(aima.utils.expr("keepPromise(ABCD, P1)"))
    KB.tell(aima.utils.expr("leader(XYZ, ABCD)"))
    KB.tell(aima.utils.expr("person(XYZ)"))

    # Get information from the knowledge base with ask - forward chaining
    print("Sample inferences (using forward chaining)")
    party = aima.logic.fol_fc_ask(KB,aima.utils.expr("party(x)")) # query to get list of party names from knowledge base
    person = aima.logic.fol_fc_ask(KB,aima.utils.expr("person(x)")) # query to get list of person names from knowledge base
    politician = aima.logic.fol_fc_ask(KB,aima.utils.expr("person(x)")) # query to get list of politician names from knowledge base
    leader  =  aima.logic.fol_fc_ask(KB,aima.utils.expr("leader(x,y)")) # query to get list of leader names from knowledge base
    # Print answers
    print('Party?')
    print(list(party))
    print()
    print('Persons?')
    print(list(person))
    print()
    print('Politicians?')
    print(list(politician))
    print()
    print('Leader?')
    print(list(leader))
    print()
    print('Give Promise?')
    print(list(aima.logic.fol_fc_ask(KB,aima.utils.expr("givePromise(x,y)"))))
    print()
# Tell python to run main method
if __name__ == "__main__": main()