# CPU Learn Tool
The CPULEARN Tool is a tool written for beginning high-school CS students whom are studying instructionsets / binary processing. CPULEARN the Motorola MC14500B instruction set with a simplified interface. This program is written so the user can change the instruction set into their own instructions. (i.e. in the main program the Return(RTN) & Jump (JMP) instructions only set a flag since the GUI only takes a 1 bit input / output)

## Motorola MC14500B and its application
In our program we used the Motorola MC14500B as inspiration for our instruction set. We also wanted to add extra registers and outputs but these need additional configuration. (This will be a part of update v1.09)</br>
So until the update this program only supports a 1 bit input/output/bus.

## Getting started
Clone the repo in a directory to your liking and start the program at the main.py file.
``` bash
    git clone https://github.com/sj-ackdo/CPULearn
    cd CPULearn/
    python main.py
```
Use the first 4 bits as your instruction and the right one as the data bit 