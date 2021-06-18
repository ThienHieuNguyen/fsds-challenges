# A tester avec 1, 31, 33, 42, 59
change(1) # >> 'Transaction impossible'
change(31) # >> {'ten': 2, 'five': 1, 'two': 3}
change(33) # >> {'ten': 2, 'five': 1, 'two': 4}
change(42) # >> {'ten': 4, 'five': 0, 'two': 1}
change(59) # >> {'ten': 5, 'five': 1, 'two': 2}
