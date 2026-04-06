import pandas as pd
import random

truth_templates = [
"I sometimes {}",
"I forgot to {}",
"I occasionally {}",
"I didn't manage to {}",
"I rarely {}"
]

lie_templates = [
"I always {}",
"I never {}",
"I definitely {} every day",
"I strictly {} daily",
"I never ever {}"
]

actions = [
"exercise",
"wake up early",
"finish my homework",
"avoid my phone",
"study before exams",
"eat healthy food"
]

data = []

for _ in range(500):
    text = random.choice(truth_templates).format(random.choice(actions))
    data.append([text,"truth"])

for _ in range(500):
    text = random.choice(lie_templates).format(random.choice(actions))
    data.append([text,"lie"])

df = pd.DataFrame(data, columns=["text","label"])
df.to_csv("dataset/lie_truth_dataset.csv", index=False)

print("Dataset generated successfully!")