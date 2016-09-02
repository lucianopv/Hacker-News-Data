def subdomain(row):
    if len(str(row["url"]).split(".")) > 2:
        return str(row["url"]).split(".",1)[1]
    else: 
        return row["url"]

def domain_count():
    import pandas as pd
    import read
    df = read.load_data()
    df["url1"] = df.apply(subdomain, axis=1) 
    domains = df["url1"].value_counts()
    return domains[0:100]
    
for name, row in domain_count().items():
    print("{0}: {1}".format(name, row))