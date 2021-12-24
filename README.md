# PokeStats
A Pokemon IV breeding simulator, intending to add shiny hunting functionality later.

Pokemon is copyrighted by Nintendo/Creatures Inc./GAME FREAK Inc. 1995-present.

## Before using
- Note the IVs of both parent pokemon; If you can not find the exact number, try to estimate about what it might be
    - IV range:
        - No good: 0
        - Decent: 1-15
        - Pretty Good: 16-25
        - Very Good: 26-29
        - Fantastic: 30
        - Best: 31
- Keep track of if any items are used in breeding that might affect IV inheritance
    - Power Anklet: Speed (SPE)
    - Power Band: Special Defense (SPD)
    - Power Belt: Defense (DEF)
    - Power Bracer: Attack (ATK)
    - Power Lens: Special Attack (SPA)
    - Power Weight: HP (HP)
    - Destiny Knot: 5 IVs at random from both parents, including any inheritance from power items (i.e. 5 IVs inherited or 4 IVs plus one from power item inherited)
 - Remember that this program is a simulation; the results shown here will not be exactly the same as in game
    - This simulation was intended as a visualization of the approximate expected results for each scenario, it does not necessarily predict your luck and due to the random nature of the generation, it is highly likely that your numbers could be different from those generated


## Functionality
Currently, there are 3 options:

### 1. Simulate one egg for IVs
This option will simulate a single egg and provide you the results based on the criteria you enter.

### 2. Simulate one egg until desired IVs
This option will continue to simulate eggs until your specified criteria is met. You will choose how many IVs you want to be at exactly what value. The simulation will stop once at least that many IVs have the specified value. The result produced will be how many eggs it took to get to that result, and what the IVs were for that offspring.

### 3. Simulate one egg until desired IVs one hundred times
This option has the same functionality as running option 2 one hundred times. The result is the average amount of eggs it took to achieve at least as many IVs at the specified value across all 100 encounters. No IVs are output, since that would be 100 IV lists and frankly that's way too many to display.

## While Using
Most of the prompting is very straight-forward. You will first be prompted to enter the IVs for parent 1, then the same for parent 2. If you aren't sure of the exact values, try to guess as best as possible for the most accurate results. If choosing options 2 or 3, you will then be prompted to enter at least how many IVs out of 6 you want to meet a certain criteria, followed by a prompt asking what specific value you want those IVs to be. You will not be able to specifically choose which IVs are at what value; the program will look for at least however many specified out of six match exactly the value that you enter. Next (for any option), you will be prompted on any guaranteed IVs (from POWER ITEMS ONLY) inherited. Parent 1 is the first parent whose IVs were entered, and parent 2 is the second. After choosing yes to either or both options, you will be asked which IVs will be inherited, while the program will display the parent's IVs once again for you to reference. Enter in the two or three letter code for the IV to be passed down. Then, you will be asked if any parent is holding a destiny knot (only if less than 2 parents are holding a power item, because 2 power items and a destiny knot is impossible). After choosing yes or no on the destiny knot, the simulation will commence and the results will be displayed! Again, please note that these results rely heavily on random number generation. Thus, your actual in-game results may vary. If this simulator is, in fact, exactly right, it is because I am a genie.

## To Do
- I might add functionality for that value or greater eventually for IVs
- Shiny hunting addition
- Shiny hunting/IV compatibility?

