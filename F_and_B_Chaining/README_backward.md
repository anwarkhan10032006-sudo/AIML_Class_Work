# Backward Chaining
Idea

Start with a goal and work backwards to check if existing facts can prove it.
--- 

# Pseudocode for Backward chaining 
```
Initialize facts
Initialize goal
Initialize proved = False

If goal is present in facts:
    proved = True
Else:
    For each rule that gives the goal:
        If all rule conditions are present in facts:
            proved = True
            Stop

If proved is True:
    Goal is proved
Else:
    Goal cannot be proved

```