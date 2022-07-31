--Initialize table to check
CREATE OR REFRESH LIVE TABLE bigmac
COMMENT "An artificially inflated dataset based on the Economist's big mac index, https://www.economist.com/big-mac-index"
AS SELECT * FROM bigmacdata;

--Check if duplicates exist
CREATE OR REFRESH LIVE TABLE duplicates
(CONSTRAINT check_duplicates EXPECT (entries = 0))
AS SELECT date, currency_code, COUNT(*) AS entries
   FROM live.bigmac
   GROUP BY date, currency_code;

--Check if dollar price exists for all entries
CREATE OR REFRESH LIVE TABLE priceinfo
(CONSTRAINT check_price EXPECT (dollar_price IS NOT NULL))
AS SELECT date, currency_code, dollar_price
   FROM live.bigmac;

--Check if Swiss currency code exists
CREATE OR REFRESH LIVE TABLE currencycode_Switzerland
(CONSTRAINT check_code EXPECT (availabledata > 0))
AS SELECT currency_code, count(*) AS availabledata
   FROM live.priceinfo
   WHERE currency_code = 'CHF'
   GROUP BY currency_code;
