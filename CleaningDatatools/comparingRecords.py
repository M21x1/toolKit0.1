# We want to compare records in the two tables for example in the listed_in column 
# of the productions_new and productions_old Dataframes using similarity threshold.
# Pairs have already been generated and defined for you in the pairs object.

import recordlinkage 

comp_cl = recordlinkage.Compare()
comp_cl.compare(
    'listed_in', 'listed_in', label='listed_in', threshold=0.3
)

potential_matches = comp_cl.compute(
    pairs, productions_old, productions_new
)

print(potential_matches)