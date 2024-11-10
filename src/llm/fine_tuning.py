import openai
from utils.logger import setup_logger

class FineTuning:
    """
    Class responsible for fine-tuning LLMs with custom datasets.
    """

    def __init__(self, config):
        self.logger = setup_logger(config.get('logging', {}))
        self.api_key = config.get('api_key')
        openai.api_key = self.api_key
        self.logger.info("FineTuning initialized.")

    def prepare_training_data(self, dataset_path):
        """
        Prepare training data from a dataset file.

        Args:
            dataset_path (str): Path to the dataset file.

        Returns:
            list of dict: Formatted training data.
        """
        self.logger.info(f"Preparing training data from {dataset_path}")
        import json
        try:
            with open(dataset_path, 'r') as file:
                data = json.load(file)
            training_data = [{"prompt": item["prompt"], "completion": item["completion"]} for item in data]
            self.logger.debug(f"Prepared {len(training_data)} training samples.")
            return training_data
        except Exception as e:
            self.logger.error(f"Failed to prepare training data: {e}")
            return []

    def create_fine_tune(self, training_data, model_base='gpt-4'):
        """
        Initiate a fine-tuning job with the provided training data.

        Args:
            training_data (list of dict): Training data samples.
            model_base (str): Base model to fine-tune.

        Returns:
            str: Fine-tuning job ID.
        """
        self.logger.info("Starting fine-tuning job.")
        try:
            response = openai.FineTune.create(
                training_file=training_data,
                model=model_base,
                n_epochs=4,
                learning_rate_multiplier=0.1
            )
            job_id = response['id']
            self.logger.info(f"Fine-tuning job started with ID: {job_id}")
            return job_id
        except Exception as e:
            self.logger.error(f"Failed to start fine-tuning job: {e}")
            return ""

    def check_job_status(self, job_id):
        """
        Check the status of a fine-tuning job.

        Args:
            job_id (str): The ID of the fine-tuning job.

        Returns:
            str: Status of the job.
        """
        self.logger.info(f"Checking status for fine-tuning job ID: {job_id}")
        try:
            response = openai.FineTune.retrieve(id=job_id)
            status = response['status']
            self.logger.debug(f"Fine-tuning job status: {status}")
            return status
        except Exception as e:
            self.logger.error(f"Failed to retrieve job status: {e}")
            return "unknown"

    def list_fine_tune_jobs(self):
        """
        List all fine-tuning jobs.

        Returns:
            list of dict: List of fine-tuning jobs.
        """
        self.logger.info("Listing all fine-tuning jobs.")
        try:
            response = openai.FineTune.list()
            jobs = response.get('data', [])
            self.logger.debug(f"Retrieved {len(jobs)} fine-tuning jobs.")
            return jobs
        except Exception as e:
            self.logger.error(f"Failed to list fine-tuning jobs: {e}")
            return []