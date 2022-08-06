CREATE TABLE bigmacdata_prtdate 
            (id long, date STRING, currency_code STRING, local_price STRING, id_batch long)
PARTITIONED BY (date);

CREATE TABLE bigmacdata_prtidbatch 
            (id long, date STRING, currency_code STRING, local_price STRING, id_batch long)
PARTITIONED BY (id_batch);

MERGE INTO bigmacdata_prtdate prt
USING bigmacdata
ON prt.id = bigmacdata.id
WHEN NOT MATCHED THEN INSERT *;

MERGE INTO bigmacdata_prtidbatch prt
USING bigmacdata
ON prt.id = bigmacdata.id
WHEN NOT MATCHED THEN INSERT *;

SELECT * 
FROM bigmacdata_prtdate
WHERE currency_code = "ARS";

SELECT * 
FROM bigmacdata_prtidbatch
WHERE currency_code = "ARS";

DROP TABLE bigmacdata_prtdate;
DROP TABLE bigmacdata_prtidbatch;
