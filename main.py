import logging
from BreastCancerPred.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from BreastCancerPred.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from BreastCancerPred.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from BreastCancerPred.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from BreastCancerPred.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

stage_name = "Data Ingestion"
try:
    logging.info(f"******** Stage {stage_name} has started ********")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logging.info(f"******** Stage {stage_name} has completed ********\n\nx========x")
except Exception as e:
    logging.exception(e)
    raise e


stage_name = "Data Validation"
try:
    logging.info(f"******* Stage {stage_name} has started ********")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logging.info(f"******** Stage {stage_name} has completed ******** \n\nx=======x")
except Exception as e:
    logging.exception(e)
    raise e


stage_name = "Data Transformation"
try:
    logging.info(f"******* Stage {stage_name} has started ********")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logging.info(f"******** Stage {stage_name} has completed ******** \n\nx=======x")
except Exception as e:
    logging.exception(e)
    raise e


stage_name = "Model Training"
try:
    logging.info(f"******* Stage {stage_name} has started ********")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logging.info(f"******** Stage {stage_name} has completed ******** \n\nx=======x")
except Exception as e:
    logging.exception(e)
    raise e

stage_name = "Model Evaluation"
try:
    logging.info(f"******* Stage {stage_name} has started ********")
    obj = ModelEvaluationPipeline()
    obj.main()
    logging.info(f"******** Stage {stage_name} has completed ******** \n\nx=======x")
except Exception as e:
    logging.exception(e)
    raise e