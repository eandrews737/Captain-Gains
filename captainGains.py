import json

def main():
    postTaxCash = float(input('How much post-tax money do you want? (decimal): '));
    annualIncome = float(input('How much did you expect to make this year? (decimal): '));
    assetInitialCost = float(input('How much did you pay for the asset? (decimal): '));
    # TODO: add long term gains tax brackets
    # isLongTermHold = yes_or_no('Did you hold it for more than a year?')
    isLongTermHold = FALSE
    isMarried = yes_or_no('Are you married?')

    # Accounting calculations
    estimatedIncome = annualIncome + postTaxCash - assetInitialCost
    estimatedTaxRate = taxBracket(estimatedIncome, isLongTermHold, isMarried)  # tax bracket might be slightly off since we don't know the real total yet
    estimatedTaxDue = postTaxCash * estimatedTaxRate  # tax rate cannot be estimated perfectly 

    total = postTaxCash + estimatedTaxDue
    print('You will need to sell roughly ' + formatCash(total) + ' worth of assets to have ' + formatCash(float(postTaxCash)) + ' after taxes.')

# Todo: account for longterm taxes
def taxBracket(annualIncome: float, isLongTermHold: bool, isMarried: bool):
    with open('taxBrackets.json') as taxBrackets:
        taxBracket = json.load(taxBrackets)

    # pull out JSON tax data
    if isMarried and not isLongTermHold:
        return findTaxRate(annualIncome, taxBracket['married'])
    elif isMarried and isLongTermHold:
        return findTaxRate(annualIncome, taxBracket['married'])
    elif not isMarried and not isLongTermHold:
        return findTaxRate(annualIncome, taxBracket['single'])
    else:
        return findTaxRate(annualIncome, taxBracket['single'])


def findTaxRate(annualIncome: float, taxBracket):
    for bracket in taxBracket:
        if float(annualIncome) >= bracket['min'] and float(annualIncome) <= bracket['max']:
            return float(bracket['rate'] / 100)

def formatCash(cash: float):
    return "${:,.2f}".format(cash)

def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[:1] == 'y':
            return True
        if reply[:1] == 'n':
            return False

if __name__ == "__main__":
    main()