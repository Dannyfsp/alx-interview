# Prime Game
Maria and Ben are playing game. Given a set of consecutive integers starting from from 1 up to and including n, they take turns choosing a prime number from the set and removing that number and its multiplies from the set. The player that cannot take a move loses the game.

They play x rpunds of the game, where n may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.
- prototype: `def isWinner(x, nums)`
- where `x` is the number of rounds and `nums` is an array of `n`
- Return: name of the player that won the most rounds
- If the winner cannot be determined, return `None`
- You can assume `n` and `x` will not be larger than 10000
- You cannot import any packages in this task

Example:
- `x` = `3` `nums` = `[4, 5, 1]`

First rounds: `4`
- Maria picks 2 and removes 2, 4, leabinf 1, 3
- Ben picks 3 and removes 3, leaving 1
- Ben wins because there are no prime numbers left for Maria to choose

Secomd round: `5`
- Maria picks 2 and removes 2, 4, leaving 1, 3, 5
- Ben picks 3 and removes 3, leaving 1, 5
- Maria wins because there are npo prime numbers left for Ben to choose


Third round: `1`
- Ben wins because there are no prime numbers for Maria to choose
**Result: Ben has the most wins**


## My take:
For each round, find the number of primes in the range 1 to num. Since each player takes out a prime number and it's multiples, the number of available moves equals the number of prime numbers in that range (1 to num). Since Maria always starts, then if number of primes in range is odd, Maria will have the last move, thus she wins. If number of primes is even, Ben will have the last move, thus he wins. Track each player's number of wins for all the rounds and return player with most wins. If they equal number of wins, return None since a winner cannot be found.

### Edge cases
```
- if x is 0 or None, a winner cannot be found. Return None.
- if nums is None or empty, a winner cannot be found. Return None
```
