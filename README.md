# sm64 sound extractor 9000

Turns data directly from the [SM64 Decompilation](https://github.com/n64decomp/sm64) and converts audio data into .sfz formats, usable in Polyphone for .sf2 soundfonts! Also includes a thingy for midi files in case you also want that

> ![NOTE]
> requires a built sm64 decomp in the root folder, i can't get you a rom that's evil sauce bro

> ![NOTE]
> if you wanna use generate-midis.py make sure you have seq64 (i used v2.4.1) in your env variables

`generate-banks-per-song.py` will loop thru each song in `sm64/sound/sequences.json` and create a unique folder for each, helpful if you're only trying to get the data of one song

`generate-master-bank.py` will create the mega soundfont data, should include every unique instrument (sfx should be in a different soundfont since max is 127), and if envelopes are unique it should not overrite

`generate-midis.py` uses seq64 to convert .m64 sequence data to .midi files. this is because i'm lazy and don't feel like using the gui 400 times Ok

> ![WARNING]
> comes bundled with [seq64 v2.4.1](https://github.com/sauraen/seq64/releases/tag/2.4.1), that was not made by me haha common mistake we kinda just look the same heh guess it's genetics or something

## Awesome TODO list

- [ ] converting percussion is horrible. kill everyone nothing ever happens
- [ ] start writing the master bank

## Cool Idea! (ebk) Can I Contribute?

yeah make a pr and also dm me on discord wizardmantis441 because idk if i get github notifs