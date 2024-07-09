from BreastCancerPred.config.configuration import ConfigurationManager
from BreastCancerPred.components.data_transformation import DataTransformation
import logging

stage_name = "Data Transformation"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation()
            data_tranformation = DataTransformation(config = data_transformation_config)
            data_tranformation.preprocess()
        except Exception as e:
            raise e
        

if __name__ == "__main__":
    try:
        logging.info(f"******* Stage {stage_name} has started ********")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logging.info(f"******** Stage {stage_name} has completed ******** \n\nx=======x")
    except Exception as e:
        logging.exception(e)
        raise e