#!/usr/bin/env python2
'''
# Simple Realtime Currency Converter #
- Converts money between active currencies (as of February 2015)
- Gets latest information via Yahoo finance API
- Usage: python currency_converter.py amount [source currency code] [target currency code]
- Example:
python currency_converter.py 15 gbp usd
'''
import sys
import urllib2

api_url = "http://finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1d1t1&s=%s%s=X"

instructions = ("Error... python currency_converter.py amount "
                "[source currency code] [target currency code]\n"
                "Example: python currency_converter.py 15 gbp usd")


def get_latest_rates(source_currency, target_currency):
    query_url = api_url % (source_currency, target_currency)
    currency_csv = urllib2.urlopen(query_url).read()
    currency_rate = currency_csv.split(",")[1]
    if currency_rate == "0.00":
        print("Error...Please check your currency codes")
        sys.exit(3)
    return float(currency_rate)


def main():
    if len(sys.argv) != 4:
        if len(sys.argv) == 1:
            print(__doc__)
            sys.exit(0)
        else:
            print(instructions)
            sys.exit(1)
    elif (sys.argv[2].upper() == sys.argv[3].upper()):
        print("Your source and target currencies are the same")
        sys.exit(2)

    amount, source_currency, target_currency = (sys.argv[1], sys.argv[2]
                                                .upper(), sys.argv[3].upper())

    if "." in amount:
        amount = float(amount)
    else:
        amount = int(amount)

    try:
        rate = get_latest_rates(source_currency, target_currency)
    except Exception as err:
        print("Could not retrieve latest currency rates due to following "
              "error: %s" % str(err))
        sys.exit(4)

    result = amount * rate
    result = format(result, ".2f")
    print("%s %s (currency rate: %s %s/%s)" % (result, target_currency, rate,
                                               target_currency,
                                               source_currency))


if __name__ == "__main__":
    main()
