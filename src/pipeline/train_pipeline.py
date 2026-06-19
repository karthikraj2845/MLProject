import sys

from src.exception import CustomException
from src.logger import logging

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__ == "__main__":
    try:
        logging.info("Training Pipeline Started")

        data_ingestion = DataIngestion()

        train_data, test_data = (
            data_ingestion.initiate_data_ingestion()
        )

        logging.info("Data Ingestion Completed")

        data_transformation = DataTransformation()

        train_arr, test_arr, _ = (
            data_transformation.initiate_data_transformation(
                train_data,
                test_data
            )
        )

        logging.info("Data Transformation Completed")

        model_trainer = ModelTrainer()

        r2_score = model_trainer.initiate_model_trainer(
            train_arr,
            test_arr
        )

        print(f"Best Model R² Score: {r2_score}")

        logging.info("Training Pipeline Completed")

    except Exception as e:
        raise CustomException(e, sys)