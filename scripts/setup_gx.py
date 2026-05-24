import great_expectations as gx

context = gx.get_context()

# Cria datasource pandas

datasource = context.data_sources.add_pandas(
    name="titanic_datasource"
)

# Adiciona asset CSV

asset = datasource.add_csv_asset(
    name="titanic_csv",
    filepath_or_buffer="data/train.csv"
)

# Define batch

batch_definition = asset.add_batch_definition_whole_dataframe(
    "whole_file"
)

print("Datasource criada com sucesso")