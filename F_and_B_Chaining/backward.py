facts = ["A", "B"]
goal = "D"

proved = False

# Step 1: Check if goal is already a fact
if goal in facts:
    proved = True
else:
    # Step 2: To prove D, we need C
    if goal == "D":
        if "C" in facts:
            proved = True
        else:
            # Step 3: To prove C, we need A and B
            if "A" in facts and "B" in facts:
                facts.append("C")   # derive C
                proved = True       # now D can be proved

print("Can we prove D?", proved)