# Interview Test - Stamp Duty Calculator

## Task

The ask is to produce a stamp duty calculator. The calculator should accept the purchase price of the house and will return the total stamp duty they owe. You'll need to generate a new TS project.

Use the following rules to calculate the total stamp duty.

```
- Up to £125,000	Zero
- The next £125,000 (the portion from £125,001 to £250,000)	2%
- The next £675,000 (the portion from £250,001 to £925,000)	5%
- The next £575,000 (the portion from £925,001 to £1.5 million)	10%
- The remaining amount (the portion above £1.5 million)	12%
```

For example 1, a property with the value of £675,000 would be calculated as follows:

First £125,000 is 0% which is £0.
Next £125,000 is 2% which is £2,500.
Next £425,000 is 5% which is £21,250.
For a total stamp duty of £23,750.

For example 2, a property with the value of £2,000,000 would be calculated as follows:

First £125,000 is 0% which is £0.
Next £125,000 is 2% which is £2,500.
Next £675,000 is 5% which is £33,750.
Next £575,000 is 10% which is £57,500.
Next £500,000 is 12% which is £60,000.
For a total stamp duty of £153,750.

## Remember

- To write unit tests
- Build the best solution possible to showcase your skills
- You are allowed to google but don't google the problem
- You can ask me questions throughout
- Please speak aloud so I can understand your thought process
- Please ensure your AI tools are disabled
