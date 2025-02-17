#access constant without always checking files
from textSummarizer.constants import *   
from textSummarizer.utils.common import read_yaml,create_directories
from textSummarizer.entity import DataIngestionConfig, DataValidationConfig,DataTransformationConfig, ModelTrainerConfig,ModelEvaluationConfig

class ConfigurationManager:        #
    def __init__(
        self,
        config_file_path = CONFIG_FILE_PATH,
        params_file_path = PARAMS_FILE_PATH):

        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    


    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES,
        )

        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_name = config.tokenizer_name
        )

        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.TrainingArguments
        
        if params is None:
         params = {}

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
        root_dir=config.root_dir,
        data_path=config.data_path,
        model_ckpt=config.model_ckpt,
        num_train_epochs = getattr(params, 'num_train_epochs', 3),
        warmup_steps = getattr(params, 'warmup_steps', 0),
        per_device_train_batch_size = getattr(params, 'per_device_train_batch_size', 8),
        weight_decay = getattr(params, 'weight_decay', 0.01),
        logging_steps = getattr(params, 'logging_steps', 100),
        evaluation_strategy = getattr(params, 'evaluation_strategy', 'steps'),
        eval_steps = getattr(params, 'eval_steps', 500),
        save_steps = getattr(params, 'save_steps', 500),
        gradient_accumulation_steps = getattr(params, 'gradient_accumulation_steps', 1)
    )

        return model_trainer_config

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_path = config.model_path,
            tokenizer_path = config.tokenizer_path,
            metric_file_name = config.metric_file_name
           
        )

        return model_evaluation_config
    

    
