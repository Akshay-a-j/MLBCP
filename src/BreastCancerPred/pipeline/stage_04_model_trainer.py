import os
import logging
from BreastCancerPred.config.configuration import ConfigurationManager
from BreastCancerPred.components.model_trainer import ModelTrainer

stage_name = "Model Training"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer()
            model_trainer = ModelTrainer(config=model_trainer_config)
            model_trainer.train_model()
        except Exception as e:
            raise e
        
    
if __name__ == "__main__":
    try:
        logging.info(f"******* Stage {stage_name} has started ********")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logging.info(f"******** Stage {stage_name} has completed ******** \n\nx=======x")
    except Exception as e:
        logging.exception(e)
        raise e
