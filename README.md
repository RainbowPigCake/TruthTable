# TruthTable
Project I made so that I don't need to make truth tables manually 

Use this repl link to try it out!
https://replit.com/@rainbowpigcake/TruthTable#main.py


# **Features**
- Custom input letters 

- Builds truth table that you can see using boolean equations

- Export truth table to a .csv format

- Canonical and non-canonical sum of products and product of sums

- K-map visualizer



# **How to Use**
- Enter the number of variables you want or type in the letters for the variables you want separated by commas. (Ex. "x,y,z" or "4")

- Type in boolean equations:
  - \+ OR operator
  - \* AND operator
  - / XOR operator
  - ' NOT operator (unary)
  
  Example: (a+b)(c'b)'(a/b)'
  
  
# **Special Commands** (type "help" to see)
| Key    | Description |
| -------- | ------- |
|  d       | display table
|  f       | display as rows
|  e       | display as csv
|  r       | reset table
|  z       | undo most recent operation
|  dnf     | get the sum of minterms
|  cnf     | get the product of maxterms
|  sum     | get the sigma thing
|  product | get the pi thing
|  k       | display a k map for the most recent equation (max 4 var)
|  d       | display table
|  i       | insert a boolean output (ex. `00110001`)
