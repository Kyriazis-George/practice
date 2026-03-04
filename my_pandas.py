import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45],
  "day":["Monday", "Tuesday", "Wednesday"]
}

df = pd.DataFrame(data["calories"])
print(df)