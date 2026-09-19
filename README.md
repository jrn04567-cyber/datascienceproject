# End-to-End Data Science Project

## Workflows — ML Pipeline Architecture

The project is structured into sequential pipeline stages:

1. **Data Ingestion**: Download, extract, and split data artifacts.
2. **Data Validation**: Validate raw data schemas, missing values, and column types.
3. **Data Transformation**: Feature engineering, data scaling, and preprocessing.
4. **Model Trainer**: Train and fine-tune machine learning algorithms.
5. **Model Evaluation**: Track experiments, calculate metrics, and log artifacts using **MLflow** and **DagsHub**.

---

## Standard Development Workflow (Per Component)

For building or updating any pipeline component, follow this exact 8-step sequence:

1. **Update `config/config.yaml`**: Specify source paths, target directory locations, and artifact URLs.
2. **Update `schema.yaml`**: Define data schema, expected column names, and data types for validation.
3. **Update `params.yaml`**: Set model hyperparameters and training arguments.
4. **Update the entity (`src/<package>/entity/`)**: Define typed dataclasses for the component's configurations.
5. **Update the configuration manager (`src/<package>/config/configuration.py`)**: Implement configuration reader methods to return the dataclass objects.
6. **Update the components (`src/<package>/components/`)**: Write the core execution logic (e.g., download files, validate against schema, train models).
7. **Update the pipeline (`src/<package>/pipeline/`)**: Create dedicated execution stage classes (e.g., `Stage01DataIngestionPipeline`).
8. **Update `main.py`**: Import and trigger the stage pipeline with clear log banners and error handling.

---

## Environment Setup & Execution

### 1. Activate Environment
* **Command Prompt (CMD):**
  ```cmd
  conda activate .\venv