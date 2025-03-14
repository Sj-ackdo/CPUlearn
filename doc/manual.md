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
## Usage and Explanation (Nederlands)
<!--![explanation](/images/explain.png)-->
![explanation](/images/explain2.png)
Hierboven volgt een uitleg over de verschillende knoppen die in de GUI staan.

De gebruiker kan zelf de instructie invullen en vervolgens uitvoeren met de *Step* knop. Beschikbare instructie's zijn:</br>

| 0 | 0000 | NOPO | Geen verandering RR = RR, O vlag = 1          |
|---|------|------|-----------------------------------------------|
| 1 | 0001 | LD   | Laad Data (Xin) -> RR                         |
| 2 | 0010 | LDC  | Laad Inv. Data (Xin) -> RR                    |
| 3 | 0011 | AND  | AND gate, Data (Xin) * RR -> RR               |
| 4 | 0100 | ANDC | Inv. AND gate, Inv. Data (Xin) * RR -> RR     |
| 5 | 0101 | OR   | OR gate, Data (Xin) + RR -> RR                |
| 6 | 0110 | ORC  | Inv. OR gate, Inv. Data (Xin) + RR -> RR      |
| 7 | 0111 | XNOR | Exclusive OR gate, als Data = RR, RR = 1      |
| 8 | 1000 | STO  | Bewaar, RR -> Data (Xin) -> Output (Yin)      |
| 9 | 1001 | STOC | Bewaar, RR -> Inv. Data (Xin) -> Output (Yin) |
| A | 1010 | IEN  | Input enable, Inp. vlag = 1                   |
| B | 1011 | OEN  | Output enable, Out. vlag = 1                  |
| C | 1100 | JMP  | Jump, JMP vlag = 1                            |
| D | 1101 | RTN  | Return, RTN vlag = 1                          |
| E | 1110 | SKZ  | Skip, als RR = 0 skip volgende instructie     |
| F | 1111 | NOPF | Geen verandering RR = RR, F vlag = 1          |

De instructie's IEN, OEN, JMP, RTN, SKZ, NOPO & NOPF worden niet gebruikt tenzij 4-bit mode is geselecteerd (deze werkt nog niet). Daarom kunnen deze zelf worden geconfigureerd als extra vlaggen voor code executie.