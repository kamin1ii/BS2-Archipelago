# Black Souls 2 Archipelago (kamin1ii fork)

Fork of [cthulhusshoes/BS2-Archipelago](https://github.com/cthulhusshoes/BS2-Archipelago) Beta v7 with these changes.

- Boss Shuffle (on by default) swaps which boss you fight in each boss arena, scaled to the arena. Boss souls and fairy tales still come from the arena, so progress is unchanged
- Enemy Shuffle (off by default) swaps the regular enemy groups, scaled to the group they replace
- Both options replace the installer's old enemy randomization when you connect to Archipelago
- Fixed 27 checks that were never sent because their pool names did not match the apworld (mostly Crimean Nursing Graveyard, White Castletown and Winterbell, plus Fairy Tale [Pinocchio]). 31 more pool names were also corrected but were already sent by other code
- Fixed Fairy Tale [Peter Pan] never being sent after the Jubjub fight
- Fixed Drink Me and Eat Me never sending their checks, and their pickups vanishing while you hold the item
- Fixed Griffy vanishing from the Fox and the Grapes arena after the Ripon Cathedral scene with Bill
- Added Covenant: Margaret and Covenant: Jabberwock items and checks. Only the covenant choice is gated, so both can still be fought without the item
- Fixed Prickett giving her ring on every visit after the Prickett's Ring fix
- Fixed the Tyrant Ring check never being sent if you already had the ring from Archipelago
- Fixed the Cheeky Oyster quest never ending when non-AP item shuffle swapped the 99 Polluted Fish she gives you
- The installer converts the three 24-bit WAV files (the kiss sound, the Infinite Food and little river ambience) to 16-bit, which fixes the high-pitched squeal. The originals are kept as backups and Restore puts them back
- Rebuilt the installer exe so it carries the fixed script

Setup is the same as below. Use this fork's apworld, yaml and installer together.

---

Installer for Black Souls 2 archipelago integration.

Should work with all versions, including steam (though achievements will be disabled).


steps:

1. drag everything from the "Game Folder" into your Black Souls 2 directory, replace anything it asks to.

2. run either Launch GUI.bat or BS2_archi_installer.py and follow the instructions there (.exe included for anyone who doesn't feel like installing python) 

3. install the Black Souls 2 apworld located in the apworld folder

4. Put your name into the Yaml File & rename. Place into players folder within archipelago

4. fill archipelago.json (located in game folder) with relevant info (archipelago port & player name)

5. should be all set to connect & play.

if any problems occur feel free to reach out to me on discord @CthulhusShoes



Credits: archipelago X vx ace connection script & tools -- EggSlashEther
	 base randomization & installer base -- Alice_Of_Nhility
	 original bs2 manual apworld -- MayruhiShiinamiya & SpearOfLies
	 Black Souls 2 integration & archipelago installer -- CthulhusShoes
