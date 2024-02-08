# BeamSearch
# Indroduction 
It is an assignment of beamSearch, the instruction is at the file "[Assignment 1_ Beam Search](/Assignment%201_%20Beam%20Search.pdf)".

It is a simple algorithm of generating a completed sentence by a pre-word.

# How to run it 
```bash=1
python3 Assignment1Main.py
```

The Expected output:
```
The probability of "Water" appearing after "<s>" is 0.0004
The probability of "<s>" appearing after "Water" is 0
The probability of "economy" appearing after "planned" is 0.046511627906976744
The probability of "</s>" appearing after "." is 1.0
< Beam Search V1 >
-5.404447778507953      <s> He said . </s>
-2.954910279033736      <s> Israel and Jordan signed the peace process . </s>
-5.83196914992102       <s> It is expected . </s>
< Beam Search V2 >
-0.028355627480674335   <s> He said that he said that he said that he added . </s>
-0.03124848443072709    <s> Israel and Jordan signed the peace agreement on the two countries , the two countries . </s>
-0.03403087458554624    <s> It is expected to be held talks on January 8 . </s>
```
It obvious to see the diffent between beamSearchV1 and beamSearchV2. 

BeamSearchV2 involves the length-normalization in the score evaluation, which encourages the model generating a longer sentence.

# Misc
In usual, I code python program in snake style, however, the instruction has defined the class name and method name. So that the coding style is a little bit confusing. 


