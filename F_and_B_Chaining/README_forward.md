# Forward Chaining
Idea

Start with known facts and apply rules repeatedly to infer new facts until a goal is reached or no new facts can be derived.
--- 

# Pseudocode for Forward chaining 
```
Initialize facts with A and B
Set changed to true

While changed is true:
    Set changed to false

    If A and B are in facts:
        If C not in facts:
            Add C to facts
            Set changed to true

    If C is in facts:
        If D not in facts:
            Add D to facts
            Set changed to true

Print all facts
```