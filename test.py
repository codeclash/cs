# pip install duckdb==0.6.1

import duckdb

# using python-string-sql (https://marketplace.visualstudio.com/items?itemName=ptweir.python-string-sql) extensions to syntax-highlight sql in python string
# to get highlighting working, one must
# Insert --sql, --beginsql, or --begin-sql at the beginning of the part of the string you would like highlighted
# and a semicolon, --endsql, or --end-sql at the end of the highlighted section.

basepath = '/01-datasets/'
cursor = duckdb.connect()

# dim_date = f"read_csv_auto('{basepath}/dim_date.csv', delim=',', header=True)"
# dim_platform = f"read_csv_auto('{basepath}/dim_platform.csv', delim=',', header=True)"
# dim_product_type = f"read_csv_auto('{basepath}/dim_product_type.csv', delim=',', header=True)"
# dim_status = f"read_csv_auto('{basepath}/dim_status.csv', delim=',', header=True)"
# dim_user = f"read_csv_auto('{basepath}/dim_user.csv', delim=',', header=True)"
fct_listings = f"read_csv_auto('{basepath}/fct_listings.csv', delim=',', header=True)"


# Scenario 1: As a business intelligence developer, I would like to see all the listings (classifieds) changes in a daily basis for each platform in order to track its evolution and answer business questions.
# Task 1: Create a report for the entire period from Dec. 2021 to Jan. 2022 (2 months) and show the snapshot of listings (classifieds) for each day of the interval considering validity or the records (SCD type 2).

# task1 = f"""--sql
# SELECT platform_id, listing_date_key,listing_id,product_type_id,user_id,price,status_id
# FROM {fct_listings}
# GROUP by platform_id, listing_date_key, listing_id,product_type_id,user_id,price,status_id
# ORDER by listing_id;
# """

task1 = f"""--sql
SELECT * 
FROM {fct_listings}
"""

print(cursor.execute(task1).fetch_df())

