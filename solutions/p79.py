def build_dag(partials):
    dag = dict() # char -> set of previous chars
    for partial in partials:
        dag.setdefault(partial[2], set()).add(partial[1])
        dag.setdefault(partial[1], set()).add(partial[0])
        dag.setdefault(partial[0], set())
    return dag

def build_code(dag):
    code = ""
    while len(dag) > 0:
        chosen = None
        for c in dag:
            if len(dag[c]) == 0:
                chosen = c
                break
        if chosen is None:
            print("<{}>".format(code), dag)
            raise Exception("no topology found")
        code += chosen
        del dag[chosen]
        for c in dag:
            dag[c].discard(chosen)
    return code

def find_code(partials):
    # assumes that there  is only one of each character in the code
    return build_code(build_dag(partials))

input_str = """\
319
680
180
690
129
620
762
689
762
318
368
710
720
710
629
168
160
689
716
731
736
729
316
729
729
710
769
290
719
680
318
389
162
289
162
718
729
319
790
680
890
362
319
760
316
729
380
319
728
716\
"""

if __name__ == "__main__":
    partials = input_str.split("\n")
    print(find_code(partials))

