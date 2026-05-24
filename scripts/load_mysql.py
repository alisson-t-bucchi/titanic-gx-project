import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("data/train.csv")

engine = create_engine(
    "mysql+pymysql://root:%23Atb081982SQL@localhost/titanic_quality"
)

df.to_sql(
    "titanic_passengers",
    engine,
    if_exists="replace",
    index=False
)

print("Dados carregados no MySQL.")