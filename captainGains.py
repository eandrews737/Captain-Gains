import json

def main():
    postTaxCash = float(input('How much post-tax money do you want? (decimal): '))
    annualIncome = float(input('How much did you expect to make this year? (decimal): '))
    assetInitialCost = float(input('How much did you pay for the asset? (decimal): '))
    
    # Ask user about long term hold
    isLongTermHold = yes_or_no('Did you hold it for more than a year?')
    isMarried = yes_or_no('Are you married?')

    # Accounting calculations
    estimatedIncome = annualIncome + postTaxCash - assetInitialCost
    estimatedTaxRate = taxBracket(estimatedIncome, isLongTermHold, isMarried)
    estimatedTaxDue = postTaxCash * estimatedTaxRate

    total = postTaxCash + estimatedTaxDue
    print('You will need to sell roughly ' + formatCash(total) +
          ' worth of assets to have ' + formatCash(postTaxCash) + ' after taxes.')

def taxBracket(annualIncome: float, isLongTermHold: bool, isMarried: bool):
    with open('taxBrackets.json') as file:
        taxData = json.load(file)

    # Use different tax brackets based on filing status and holding period.
    if isMarried:
        if isLongTermHold:
            return findTaxRate(annualIncome, taxData['marriedLongTerm'])
        else:
            return findTaxRate(annualIncome, taxData['married'])
    else:
        if isLongTermHold:
            return findTaxRate(annualIncome, taxData['singleLongTerm'])
        else:
            return findTaxRate(annualIncome, taxData['single'])

def findTaxRate(annualIncome: float, taxBracket):
    for bracket in taxBracket:
        if annualIncome >= bracket['min'] and annualIncome <= bracket['max']:
            return bracket['rate'] / 100
    # If no matching bracket is found, return the rate from the last bracket as a fallback.
    return taxBracket[-1]['rate'] / 100

def formatCash(cash: float):
    return "${:,.2f}".format(cash)

def yes_or_no(question):
    while True:
        reply = input(question + ' (y/n): ').strip().lower()
        if reply and reply[0] == 'y':
            return True
        elif reply and reply[0] == 'n':
            return False
        else:
            print("Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
