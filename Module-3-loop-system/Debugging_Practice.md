# Step9: Debugging Practice (examples with explanations)
# -----------------------------------------------------------------
# BUG 1 - Forgot to update counter (infinite loop)
# -----------------------------------------------------------------
# counter = 1
# while counter <= 5:
#     print(counter)
#     # counter += 1   <- missing! -> loop never ends
#
# FIX:
# counter = 1
# while counter <= 5:
#     print(counter)
#     counter += 1     <- counter is updated every iteration

# -----------------------------------------------------------------
# BUG 2 - Wrong indentation (logic error)
# -----------------------------------------------------------------
# for i in range(3):
#     print("Task", i)
# print("Done")       <- if this were inside the loop it would print 3×
#
# FIX: keep the final print at the correct indentation level (outside loop)