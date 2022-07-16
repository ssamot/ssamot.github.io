import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
import inflect

# url = 'https://www.southampton.ac.uk/~cpd/history.html'
# page = requests.get("").content

with open("timeline.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
table = soup.find_all('table')[2]
df_list = pd.read_html(str(table))
df = df_list[-1]

prefixes = ["I. COSMOLOGICAL ANTECEDENTS",
            "II. HUMAN ANCESTRY AND EVOLUTION",
            "III. CULTURAL DEVELOPMENT",
            "IV. PLANETARY MANAGEMENT"]

inf = inflect.engine()

rows = table.find_all('tr')
era = 0
map = {"time":[], "event":[]}
col = None
era_changed = False
saved_dir = "../timeline"
sign = "-"
current_prefix = None
prev_col = ""
prev_prefix = prefixes[0]

print("File")

for i, row in enumerate(rows):
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]


    if(len(cols) == 1):
        era+=1
        era_changed = True

    if( era > 0):
        if(len(cols) == 1 and era_changed):
            col = cols[0]

            for prefix in prefixes:
                if (prefix in col):
                    current_prefix = prefix
                    col = col.replace(prefix, "")
                    break
            if (len(map["event"]) > 0):
                df = pd.DataFrame(map)
                fullname = prev_prefix + prev_col
                name = prev_prefix + "__" + prev_col
                name = name.replace(" ", "_")
                print(f" [{name}](/timeline/{name}.csv)")
                prev_prefix = current_prefix
                prev_col = col
                df.to_csv(f"./{saved_dir}/{name}.csv")

            map = {"time": [], "event": []}
            era_changed = False
        else:
            formatted = cols[0].replace(',', '')
            if("BCE" in formatted):
                sign = "-"
            elif ("CE" in formatted):
                sign = "+"

            formatted = re.sub("[^0-9]", "", formatted)
            n = inf.number_to_words(int(formatted))
            map["time"].append(int(sign + formatted))
            map["event"].append(cols[-1])

    if(len(rows) -1 == i):
        df = pd.DataFrame(map)
        fullname = prev_prefix + prev_col
        name = prev_prefix + "__" + prev_col
        name = name.replace(" ", "_")
        print(f" [{name}](/timeline/{name}.csv)")
        prev_prefix = current_prefix
        prev_col = col
        df.to_csv(f"./{saved_dir}/{name}.csv")

