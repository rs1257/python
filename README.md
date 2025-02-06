# Python Interview Test - Stamp Duty Calculator

## Task

The ask is to produce a stamp duty calculator. The calculator should accept the purchase price of the house and will return the total stamp duty they owe.

Use the following rules to calculate the total stamp duty.
```
- Up to £125,000	Zero
- The next £125,000 (the portion from £125,001 to £250,000)	2%
- The next £675,000 (the portion from £250,001 to £925,000)	5%
- The next £575,000 (the portion from £925,001 to £1.5 million)	10%
- The remaining amount (the portion above £1.5 million)	12%
```

Remember to write tests and build the best solution possible to showcase your skills.

## Extensions

1 - Adjust your solution to calculate the rate for a first time buyer as well. You'll need to add another parameter.

The following rules should be implemented.
```
First time property
- no SDLT up to £300,000
- 5% SDLT on the portion from £300,001 to £500,000
- If the price is over £500,000, you cannot claim the relief. Follow the rules for people who’ve bought a home before.
```

2 - Adjust your solution to calculate the rate for buying an additional home.

The following rules should be implemented.

```
Additional home
- Up to £125,000	5%
- The next £125,000 (the portion from £125,001 to £250,000)	7%
- The next £675,000 (the portion from £250,001 to £925,000)	10%
- The next £575,000 (the portion from £925,001 to £1.5 million)	15%
- The remaining amount (the portion above £1.5 million)	17%
```

3 - Add an additional date parameter, if the date is in 2019 or earlier, then the total stamp duty should be 0.

4 - (Open ended) How can this be enhanced in the future? And what would you implement first?

5 - Is there an alternative approach which is better that you could have implemented given more time?

6 - What is the time complexity of your current implementation? In terms of Big O.
