# ULRtA-
A simple asm-like language with advanced features.

# Commands:

## in 
Read a string from Standard Input to the specified register, with the prompt specified

Syntax: in \[prompt string\] \[register\]

Example: in $PROMPT $asn

## out
Print a String, Int or register to Standard Output

Syntax: out \[register, string, int\]

Example: out $RESULT

## mov
Store the specified value in the specified register

Syntax: mov\[value\] \[register\]

Example: mov 5 $ADD

Note: Register name should be CAPS, and begin with $

## add

Add the first and second registers, and store it in the third register

Syntax: add \[int or register\] \[int or register\] \[register\]

Example: add 5 5 $RESULT

## sub

Subtract the first and second registers, and store the result in the third register

Syntax: sub \[int or register\] \[int or register\] \[register\]

Example sub 7 5 $RESULT

## times

Mulitply the first and second registers, and store the result in the third register

Syntax: times \[int or register\] \[int or register\] \[register\]

Example: times 7 6 $RESULT

## div

Divied the first and second registers, and store the result in the third register

Syntax: div \[int or register\] \[int or register\] \[register\]

Example: div 47 6 $RESULT

## goto

Goto the specified label

Syntax: goto \[label\]

Example: goto .MAIN

## if 

If the two specified terms match, then goto the label. Else, continue

Syntax: if \[register, string, int\] (is) \[register, string, int\] (then) (goto) \[label\]\*

\**Terms in parenthesis optional, but recommended*

Example: if 5 is $ANS then goto .YES

## end

Stop execution

Syntax: end

Example: end

## dump

Print the raw content of the registers to Standard Output. Good for debugging

Syntax: dump

Example: dump

## How to label

To make a label for a goto or if, just prefix it with a '.'

Syntax: .\[label\]

Example: .MAIN

