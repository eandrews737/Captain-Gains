import sys, json

# Check README for more details about parameters
def main(postTaxCash: float, annualIncome: float, isMarried: bool, isLongTermCapitalGains: bool, assetInitialCost: float):
    taxRate = taxBracket(annualIncome, isMarried);
    totalNeeded = float(postTaxCash)

    print('You will need: ' + formatCash(totalNeeded))

def taxBracket(annualIncome: float, isMarried: bool):
    with open('taxBrackets.json') as taxBrackets:
        taxBracket = json.load(taxBrackets)
    if isMarried:
        findTaxRate(taxBracket['married'])
    else:
        findTaxRate(taxBracket['single'])

def findTaxRate(taxBracket):
    print(taxBracket)

def formatCash(cash: float):
    return "${:,.2f}".format(cash)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])