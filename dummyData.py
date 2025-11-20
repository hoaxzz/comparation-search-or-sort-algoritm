import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Generate dummy transaction data
n = 10000

np.random.seed(42)

transaction_ids = [f"TX{100000+i}" for i in range(n)]
customer_names = [f"Customer_{random.randint(1,2000)}" for _ in range(n)]
amounts = np.random.uniform(10, 5000, n).round(2)

# Random dates within last 60 days
start_date = datetime.now() - timedelta(days=60)
dates = [start_date + timedelta(days=random.randint(0,60)) for _ in range(n)]

df = pd.DataFrame({
    "transaction_id": transaction_ids,
    "customer_name": customer_names,
    "amount": amounts,
    "date": dates
})

output_path = "/mnt/data/dummy_transactions_10000.csv"
df.to_csv(output_path, index=False)

output_path
