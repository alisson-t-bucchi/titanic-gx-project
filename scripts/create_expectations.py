import great_expectations as gx

context = gx.get_context()

try:
    context.suites.delete("titanic_suite")
    print("Suite antiga removida.")
except Exception:
    print("Nenhuma suite antiga encontrada.")

# Recupera datasource

datasource = context.data_sources.get("titanic_datasource")
asset = datasource.get_asset("titanic_csv")
batch_definition = asset.get_batch_definition("whole_file")

batch = batch_definition.get_batch()

# Cria suite

suite = gx.ExpectationSuite(name="titanic_suite")

# Expectations

suite.add_expectation(
    gx.expectations.ExpectColumnValuesToNotBeNull(
        column="PassengerId"
    )
)

suite.add_expectation(
    gx.expectations.ExpectColumnValuesToBeBetween(
        column="Age",
        min_value=0,
        max_value=100
    )
)

suite.add_expectation(
    gx.expectations.ExpectColumnValuesToBeInSet(
        column="Sex",
        value_set=["male", "female"]
    )
)

suite.add_expectation(
    gx.expectations.ExpectTableRowCountToBeBetween(
        min_value=500,
        max_value=2000
    )
)

suite.add_expectation(
    gx.expectations.ExpectColumnMeanToBeBetween(
        column="Fare",
        min_value=20,
        max_value=40
    )
)

suite.add_expectation(
    gx.expectations.ExpectColumnMedianToBeBetween(
        column="Fare",
        min_value=10,
        max_value=30
    )
)

suite.add_expectation(
    gx.expectations.ExpectColumnQuantileValuesToBeBetween(
        column="Fare",
        quantile_ranges={
            "quantiles": [0.25, 0.5, 0.75],
                "value_ranges": [
                    [0, 20],
                    [10, 30],
                    [20, 50]
            ]
        }
    )
)

suite.add_expectation(
    gx.expectations.ExpectColumnUniqueValueCountToBeBetween(
        column="Survived",
        min_value=2,
        max_value=2
    )
)


# Salva suite

context.suites.add(suite)

print("Expectation Suite criada")