def load_data():
    import pandas as pd
    data = pd.read_csv("hn_stories.csv", names=["submission_time","upvotes","url","headline"])
    if data.columns.tolist() == ["submission_time","upvotes","url","headline"]:
        print("Columns seem to be OK")
    else: 
        print("There's somethings wrong")
    return data
        
if __name__ == "__main__":
    load_data()