# Captain Gains
A Simple Captial Gains Calculator

## Summary
A simple python script for calculating how much money you would need to have **X** amount after taxes.
For example, if you wanted to purchase a **$35,000** Tesla by selling a short-term asset and you make $60,000 a year, you would need to pull out **$43,400.00**.
This is designed to give you a rough estimate of how much you would need.
The formula is used to estimate the pre-tax income formula used by auditors: 
`Pre-tax cost of equity = Post-tax cost of equity ÷ (1 – tax rate)`

## How to Run
1) Download the script
2) CD into the folder
3) Run the following command (remove the brackets and fill in the parameters)

`python3 capitalGainsCalculator`

## Paramters
* `float` - How much post-tax cash do you want?
* `float` - How much do you normally make a year?
* `bool` - Are you married and filing together?
* `bool` - Have you held the asset your selling for more than a year?
* `float` - How much did you pay for the asset? (Remember to account for percentages if you're not selling all of it).

## Tax Brackets
More Info can be found in the taxBracket.json file.
Tax bracket information comes from [here](https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets).

### Single Filers
| Tax Rate | Tax Bracket |
| - | - |
| 10% | $0 to $9,875 |
| 12% | $40,126 to $85,525 |
| 22% | $40,126 to $85,525 |
| 24% | $85,526 to $163,300 |
| 32% | $163,301 to $207,350 |
| 35% | $207,351 to $518,400 |
| 37% | $518,401 to infinity |

### Married
| Tax Rate | Tax Bracket |
| - | - |
| 10% | $0 to $19,750 |
| 12% | $19,751 to $80,250 |
| 22% | $80,251 to $171,050 |
| 24% | $171,051 to $326,600 |
| 32% | $326,601 to $414,700 |
| 35% | $414,701 to $622,050 |
| 37% | $622,051 to infinity |