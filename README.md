# Captain Gains  
A Simple Capital Gains Calculator to Estimate Asset Sales Needed for a Purchase

## Summary
This Python script estimates how much asset value you need to sell in order to net a desired post-tax amount. For example, if you want to purchase a **$35,000** Tesla by selling a short-term asset, and you earn **$60,000** a year, you might need to sell roughly **$43,400.00** worth of assets. This tool provides a rough estimate only—the actual tax liability may differ. The calculation is based on the formula:

**Pre-tax sale amount = Post-tax amount ÷ (1 – tax rate)**

*Note: This approximation applies only to US federal tax calculations.*

## How to Run
1. Download the script.
2. Change directory (`cd`) into the folder containing the script.
3. Run the following command:

   ```bash
   python3 capitalGainsCalculator.py

## Paramters
* `float` - How much post-tax cash do you want?
* `float` - What is your annual income?
* `bool` - Are you married and filing jointly?
* `bool` - Have you held the asset you are selling for more than a year? (Determines whether long-term or short-term tax rates apply.)
* `float` - What did you pay for the asset? (Remember to account for percentages if you’re not selling the entire asset.)

## Tax Brackets
More Info can be found in the taxBracket.json file.
Tax bracket information comes from [NerdWallet](https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets).

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

## Disclaimer  
This tool is designed for **informational and estimation purposes only**. It does not provide official tax advice and should not be relied upon for making financial or tax-related decisions. The calculations are based on general **U.S. federal tax brackets** and may not account for **state taxes, deductions, exemptions, or other financial factors** that could affect your actual tax liability.  

For **accurate tax planning**, consult a **certified tax professional** or the **IRS**. By using this tool, you acknowledge that the author holds **no liability** for any financial decisions made based on these estimations.