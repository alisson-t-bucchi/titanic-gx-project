import great_expectations as gx

context = gx.get_context()

checkpoint = context.checkpoints.add_or_update(
    gx.Checkpoint(
        name="titanic_checkpoint",
        validation_definitions=[
            gx.ValidationDefinition(
                name="titanic_validation",
                data=context.data_sources
                    .get("titanic_datasource")
                    .get_asset("titanic_csv")
                    .get_batch_definition("whole_file"),
                suite=context.suites.get("titanic_suite")
            )
        ]
    )
)

results = checkpoint.run()

print(results)

context.build_data_docs()
context.open_data_docs()