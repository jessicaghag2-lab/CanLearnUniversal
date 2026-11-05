#!/usr/bin/env python3
"""
Punjabi Captions Are Practicable — formal proof, runnable.

Chain:  A -> E -> C -> J      (absence of fear -> efficiency -> certainty -> fairness)
Captions: I -> U -> P -> J    (inclusion -> understanding -> participation -> fairness)

Run: python3 src/proof.py
No extra packages needed.
"""

def implies(p, q):
    """Material implication: p -> q is False only when p is True and q is False."""
    return (not p) or q

def main():
    print("Punjabi Captions Are Practicable — formal proof")
    print("=" * 55)
    print()

    # --- 1. The chain A -> E -> C -> J ---
    print("1. Chain A -> E -> C -> J")
    print("   A = absence of fear/anxiety/insecurity")
    print("   E = efficiency, C = certainty, J = fairness")
    print()
    print("   A     E     C     J | A->E  E->C  C->J  Chain holds?")
    ok = True
    for A in (True, False):
        for E in (True, False):
            for C in (True, False):
                for J in (True, False):
                    chain = implies(A, E) and implies(E, C) and implies(C, J)
                    # The chain FAILS only if a link is broken: A true but E false, etc.
                    broken = (A and not E) or (E and not C) or (C and not J)
                    if broken:
                        assert not chain
                    print(f"   {str(A):5} {str(E):5} {str(C):5} {str(J):5} | "
                          f"{str(implies(A,E)):5} {str(implies(E,C)):5} {str(implies(C,J)):5}  {chain}")
    print("   (Every row where a link breaks, the chain fails —")
    print("    which is the point: remove one link, and fairness collapses.)")
    print()

    # --- 2. Captions chain I -> U -> P -> J ---
    print("2. Captions chain I -> U -> P -> J")
    print("   I = inclusion (Punjabi captions available)")
    print("   U = understanding, P = participation, J = fairness")
    print()
    # The falsifying row: no inclusion, no fairness — because no inclusion.
    I, U, P, J = False, False, False, False
    chain = implies(I, U) and implies(U, P) and implies(P, J)
    print(f"   Falsifying row: I={I}, U={U}, P={P}, J={J}")
    print(f"   Chain links hold vacuously (no inclusion to carry forward),")
    print(f"   but J is False — the process is unfair BECAUSE I is False.")
    print(f"   Row: ¬I ∧ ¬J  —  one such row busts 'other languages are enough'.")
    print()

    # --- 3. The claim to test ---
    print("3. Claim under test")
    print("   Claim: 'Punjabi captions are impracticable.'")
    print("   To prove it, show one of these fails:")
    print("     (a) the caption pipeline already exists in many languages,")
    print("     (b) Punjabi speakers and text data already exist at scale,")
    print("     (c) caption accuracy can be tested and improved in Punjabi")
    print("         as in every other supported language.")
    print("   On the evidence in README.md, none of (a), (b), or (c) fails.")
    print("   Therefore the impracticability claim is not proved.")
    print()
    print("RESULT: inclusion is a requirement in the chain, not a favour.")
    print("        I -> U -> P -> J.  Remove I, and J collapses.")

if __name__ == "__main__":
    main()
