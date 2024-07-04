from BreastCancerPred.config.configuration import ConfigurationManager
from BreastCancerPred.components.data_validation import DataValidation
import logging

stage_name = "Data Validation"

class DataValidationTrainingPipeline:
    def __init__(self) -> None:
        pass


    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.validate_all_columns()



if __name__ == "__main__":
    try:
        logging.info(f"******* Stage {stage_name} has started ********")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logging.info(f"******** Stage {stage_name} has completed ******** \n\nx=======x")
    except Exception as e:
        logging.exception(e)
        raise e