# Cersei  
## A completely luck based game that's somehow entertaining!  

***Note: This game is experimental, and the python version of the game is to find game flaws.  Please report all issues with either  `bug` or `gameplay` flags in issues when you find them so that we can improve the game. Thanks! `-trevormurphy424`***

### What is Cersei?  
Cersei is a modification of the classic game "War" in which players play cards and higher-valued cards win.  
  
### What's different?  
#### Card Names  
* Ace -> Cannoneer
* 2 -> Scout
* 3 -> Pawn (3)
* 4 -> Benedict
* 5 -> Lieutenant
* 6 -> Pawn (6)
* 7 -> Pawn (7)
* 8 -> Captain
* 9 -> Diplomat
* 10 -> Pawn (10)
* Jack -> Assassain
* Queen -> Cersei
* King -> King
* Joker -> Eunich
  
#### New Card Values
* Cannoneer -> -14/0/14 (See Rules)
* 2-10 -> Respective Values
* Assassain -> 11
* Circe -> 2/Infinite (See Rules)
* King -> 10/Infinite (See Rules)
* Eunich -> 15
  
### Rules
The game plays exactly like war, with a few exceptions:
1. All queens except for the queen of diamonds are removed.  The queen of diamonds is called *Cersei*.
2. Once Cersei is played three times, the game ends.
3. If a player runs out of cards before Cersei is played 3 times, they automatically lose.

#### Modifier Cards:
* Lieutenant (5): Draw the next card from the top of deck and add to the value of five.  New value beats all cards with lower combined value.  If a Lieutenant is placed on top of another, it can be chained and played again.  (ie. you can place a 5, 5, and another card.)
* Captain (8): Draw the next card and subtract values from all opponents' cards.  Only the drawn card is subtracted.  This ability can also be chained (see Lieutenant rules).  All modified opponent cards will be played against the value of 8.

#### In-Round Cards:
* Cannoneer (Ace): If the color of the Cannoneer matches that of the highest opponent, it is worth +14.  Otherwise, it is worth -14.
* Scout (2): If a scout is played, a battle takes place.  (See Battles section below.)
* Diplomat (9): If played during a battle or war, all cards are returned to original respective players.  Overridden by both King and Cersei
* Cersei (Queen): Defeats all cards aside from pawns.  Otherwise, worth 2.
* King (King): The king wins all battles and wars __except those against Cersei__.

#### Post-Round Cards:
* Benedict (4): If a Benedict is played, and loses, the Benedict must be taken back by the player who played it and the next card from the top of the player's deck must be given instead.
* Assassain (Jack): If played, and wins, winning player may select one (facedown) card from each other player's deck.
* Eunich (Joker): If a Eunich is played at any point in a round, all players must shuffle their decks upon the conclusion of the round.  *Additionally*, if the player who plays the Eunich has Cersei in their deck, Cersei must be moved to the bottom of the deck.

#### Wars & Battles:
Wars and battles consist of a player placing down either 3 or 1 face down cards and then drawing another on top.  This creates higher stakes as more cards will be lost.  
* For wars, 3 cards are played face-down before one is played face-up on top.
* For battles, 1 card is played face-down before one is played face-up on top.
* Modifier cards *can* be applied to cards played in wars.

### So what about winning?
The player with the most cards in their deck at the end of the game wins.  The end of the game happens either when Cersei is played 3 times, or when a player runs out of cards.

### Help! I'm stubborn and have a conflict with another player!
In case of a conflict, simply add up values of all cards and give the player with the higher value of cards the win for the round.  
**Still can't decide?**  
Take this handy chart for the order in which turns should be played.  This eliminates any conflicts if played correctly.
1. Place initial cards.
2. Add all modifier cards.
3. Check for wars.
    1. Check for Cersei.
    2. Check for King.
    3. Check for Diplomat.
4. Check for battles.
    1. Check for Cersei.
    2. Check for King.
    3. Check for Diplomat.
5. Play modifier cards in battle/war.
6. Winning card takes all.
7. Play post-round cards.
