facts = ["A", "B"]

changed = True

while changed:
    changed = False

    # Rule 1: If A and B then C
    if "A" in facts and "B" in facts:
        if "C" not in facts:
            facts.append("C")
            changed = True

    # Rule 2: If C then D
    if "C" in facts:
        if "D" not in facts:
            facts.append("D")
            changed = True

print("Derived facts:", facts)
