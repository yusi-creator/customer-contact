import pandas as pd
import random

file_path = "data/slack/従業員情報.csv"

df = pd.read_csv(file_path)

slack_ids = [
    "U0BPYPURJ00",
    "U0BP4E7TVJN"
]

df["SlackID"] = [
    random.choice(slack_ids)
    for _ in range(len(df))
]

df.to_csv(file_path, index=False, encoding="utf-8-sig")

print("SlackIDを設定しました")
print(df[["SlackID"]])