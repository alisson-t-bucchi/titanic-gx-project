import great_expectations as gx

context = gx.get_context()

suite = context.suites.get("titanic_suite")

datasource = context.data_sources.get("titanic_datasource")
asset = datasource.get_asset("titanic_csv")
batch_definition = asset.get_batch_definition("whole_file")

batch = batch_definition.get_batch()

validation_result = batch.validate(suite)

print("\nResultado geral:")
print(validation_result.success)

print("\nDetalhes:")

for result in validation_result.results:
    print(
        f"{result.expectation_config.type}: {result.success}"
    )

# Salva validation result no contexto
context.validation_definitions.add_or_update(
    gx.ValidationDefinition(
        name="titanic_validation",
        data=batch_definition,
        suite=suite,
    )
)

# Build docs
context.build_data_docs()

# Open docs
context.open_data_docs()