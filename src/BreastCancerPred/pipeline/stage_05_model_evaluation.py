import logging
from BreastCancerPred.config.configuration import ConfigurationManager
from BreastCancerPred.components.model_evaluation import ModelEvaluation

stage_name = "Model Evaluation"

class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation()
            model_evaluation = ModelEvaluation(config=model_evaluation_config)
            model_evaluation.model_evaluation()

        except Exception as e:
            raise e
        
if __name__ == "__main__":
    try:
        logging.info(f"******* Stage {stage_name} has started ********")
        obj = ModelEvaluationPipeline()
        obj.main()
        logging.info(f"******** Stage {stage_name} has completed ******** \n\nx=======x")
    except Exception as e:
        logging.exception(e)
        raise e
    