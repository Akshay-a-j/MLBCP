from BreastCancerPred.components.data_ingestion import DataIngestion
from BreastCancerPred.config.configuration import ConfigurationManager
from BreastCancerPred import logging

stage_name = "Data Ingestion"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logging.info(f"******** Stage {stage_name} has started ********")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logging.info(f"******** Stage {stage_name} has completed ********\n\nx========x")
    except Exception as e:
        logging.exception(e)
        raise e
    
