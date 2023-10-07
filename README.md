# End-to-End-ML-project
## Image classification project

Tech stack inlcuded in this project:
1. GitHub Repository Setup
2. Project Template Creation
3. Project Setup & Requirements Installation
4. Logging, Utils and Exception Module
5. Project Workflow
6. All Components Notebook Experiment
7. All Components Modular Code Implementation
8. Training Pipeline
9. DVC (MLOps Tool) - For pipeline tracking and implementation
10. Docker
11. Final CI/CD Deployment on AWS and Azure



How to build each stage:
1) Update config/config.yaml
2) Update entity in project/entity/config_entity.py with config.yaml variable
3) Expand the ConfigurationManager class in project/config/configuration.py
4) Create a module for new stage
5) *Create the pipeline for new stage 
6) *Update main.py for new stage


To see training results in tensorboard type:
```shell
tensorboard --logdir artifacts/prepare_callbacks/tensorboard_log_dir/
```

To run full pipeline run:
```shell
python - m main
```

To run dvc pipeline run:
```shell
dvc repro
```

To display dvc pipeline 
```shell
dvc dag
```