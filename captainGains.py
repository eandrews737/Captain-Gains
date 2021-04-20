import sys, json

def main(postTaxCash: float, annualIncome: float, assetInitialCost: float, isMarried: bool, isLongTermCapitalGains: bool):
    netProfit = float(postTaxCash) - float(assetInitialCost)
    estimatedIncome = float(annualIncome) + float(postTaxCash)
    taxRate = taxBracket(estimatedIncome, isMarried);
    tax = float(netProfit) * float(taxRate)
    total = float(tax) + float(postTaxCash)

    print('You will need to sell ' + formatCash(total) + ' worth of assets to have ' + formatCash(float(postTaxCash)) + ' after taxes.')

def taxBracket(annualIncome: float, isMarried: bool):
    with open('taxBrackets.json') as taxBrackets:
        taxBracket = json.load(taxBrackets)
    if isMarried:
        return findTaxRate(annualIncome, taxBracket['married'])
    else:
        return findTaxRate(annualIncome, taxBracket['single'])

def findTaxRate(annualIncome: float, taxBracket):
    for bracket in taxBracket:
        if float(annualIncome) >= bracket['min'] and float(annualIncome) <= bracket['max']:
            return float(bracket['rate'] / 100)

def formatCash(cash: float):
    return "${:,.2f}".format(cash)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])