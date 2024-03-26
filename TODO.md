# TODO
- Move UI strings to separate files
  - Doesn't seem possible without decreasing readability. 
- Stop mixing dummy answers and real answers or find better convention.
- Consider existence and the belonging of third-party python code
- Better database migrations
- Add card type groups (text, number, etc.)      (maybe)
  - Add custom card types
  - Draw dummy answers from pool of similar card types in same group.
- Do some crazy dot-product similarity or KNN to find dummy answers most similar 
  to the actual answer.
- Add interleaving.
    - interleaved heavy draws. 
- Card difficulties (0, 1, 2, etc) 
  - as mastery of lower tiers is achieved, increase liklihood that higher tiered
    cards are displayed.
