import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

engine = create_engine(
    "mysql+pymysql://root:SENHA@localhost/titanic_quality"
)

results = []

for result in validation_result.results:
    results.append({
        "expectation": result.expectation_config.type,
        "success": result.success,
        "execution_time": datetime.now()
    })

df = pd.DataFrame(results)

df.to_sql(
    "gx_validation_results",
    engine,
    if_exists="append",
    index=False
)

print("Resultados salvos.")