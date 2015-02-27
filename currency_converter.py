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

# Active currency codes - http://en.wikipedia.org/wiki/ISO_4217#Active_codes
# Retrieved - 27th February
currency_codes = ("AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BOV", "BRL", "BSD", "BTN", "BWP", "BYR", "BZD", "CAD", "CDF", "CHE", "CHF", "CHW", "CLF", "CLP", "CNY", "COP", "COU", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MUR", "MVR", "MWK", "MXN", "MXV", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "SSP", "STD", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "USN", "USS", "UYI", "UYU", "UZS", "VEF", "VND", "VUV", "WST", "XAF", "XAG", "XAU", "XBA", "XBB", "XBC", "XBD", "XCD", "XDR", "XFU", "XOF", "XPD", "XPF", "XPT", "XSU", "XTS", "XUA", "XXX", "YER", "ZAR", "ZMW", "ZWL") 

instructions = '''Error... python currency_converter.py amount [source currency code] [target currency code]
Example: python currency_converter.py 15 gbp usd'''


def get_latest_rates(source_currency, target_currency):
    query_url = api_url % (source_currency, target_currency)
    currency_csv = urllib2.urlopen(query_url).read()
    currency_rate = currency_csv.split(",")[1]
    return float(currency_rate)


def main():
    #ipdb.set_trace()
    if len(sys.argv) != 4:
        if len(sys.argv) == 1:
            print(__doc__)
            exit(0)
        else:
            print(instructions)
            sys.exit(1)
    elif (sys.argv[2].upper() not in currency_codes or 
            sys.argv[3].upper() not in currency_codes):
        print(instructions)
        sys.exit(2)
    elif (sys.argv[2].upper() == sys.argv[3].upper()):
        print("Your source and target currencies are the same")
        sys.exit(3)

    amount, source_currency, target_currency = (sys.argv[1], sys.argv[2].upper(), sys.argv[3].upper())
    
    if "." in amount:
        amount = float(amount)
    else:
        amount = int(amount)
    
    try:
        rate = get_latest_rates(source_currency, target_currency)
    except Exception as err:
        print("Could not retrieve latest currency rates due to following error: %s" % str(err))
        exit(4)
    
    result = amount * rate
    result = format(result, ".2f")
    print("%s %s (currency rate: %s %s/%s)" % (result, target_currency, rate, target_currency, source_currency))


if __name__ == "__main__":
    main()
