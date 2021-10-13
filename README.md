# Papyrus

_A text-based level editor for the New Super Mario Bros. series, powered by [nsmbpy2](https://github.com/RoadrunnerWMC/nsmbpy)_

WIP. Everything subject to change, including the name.

Licensed under GNU GPL v3, see LICENSE for details.

Important Note: nsmbpy2 and Papyrus have strong backward-compatibility guarantees deeply baked into their design, but this is ***NOT*** being enforced yet at this early stage of development. I will remove this notice when this changes.

## Wat

Yep. Graphical level editors are great 99% of the time... but not in every single case. Papyrus aims to fill in the last 1%. Here are some examples where you might find it useful:

### Low-level data access

Unlike most graphical level editors, Papyrus gives you direct access to the raw byte data for almost everything in the level. This can be helpful when researching some of the more poorly-documented corners of a level file format, or when developing custom code that extends the existing data structures in some way.

### Scripting

None of the existing NSMB-series graphical level editors provide any sort of scripting functionality to automate repetitive or human-difficult tasks (for example, placing 20 coins in a perfect circle). Without Papyrus, to make a script for generating partial level data, you'd need to write some amount of code implementing the level file format yourself, which in many cases is more trouble than it'd be worth. Having a text-based level file format as an option, though, lowers the entry barrier for custom scripts tremendously.

(This mainly applies to scripts written in languages other than Python, since for Python scripts, it's better to use nsmbpy2 directly :) )

### Awkward cases

Occasionally there are situations that are just inherently awkward to deal with in graphical level editors.

For example, a fancy level design may call for a dozen or more rotation controllers all at the same position. This isn't difficult to set up, but tweaking them afterwards requires annoyingly "unstacking" and "restacking" them every time. But if they're defined in a text file, there's no unstacking required, and editing them is a breeze.

Or as another example, there are a few situations in which the order in which sprites appear in the level data affects their behavior. Most graphical editors don't provide a general way to reorder sprites; all you can do is delete and recreate them to move them to the top of the list. Papyrus shows you the exact order in which everything will appear in the level data, so you can rearrange sprites directly however you want.
