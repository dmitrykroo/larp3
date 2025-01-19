from services.ai_service import AIService
from services.valuation_service import ValuationService
from services.user_service import UserService
from connectors.database_connector import DatabaseConnector
from utils.logger import setup_logger

class ReportService:
    """
    Service responsible for generating and managing user reports.
    """

    def __init__(self, config):
        self.logger = setup_logger(config.get('logging', {}))
        self.ai_service = AIService(config)
        self.valuation_service = ValuationService(config)
        self.user_service = UserService(config)
        self.db_connector = DatabaseConnector(config['database'])
        self.logger.info("ReportService initialized.")

    def generate_user_report(self, user_id):
        """
        Generate a comprehensive report for a user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            str: Generated report text.
        """
        self.logger.info(f"Generating report for User ID: {user_id}")
        user = self.user_service.get_user(user_id)
        nfts = self.db_connector.fetch_user_nfts(user_id)
        market_data = self.valuation_service.get_market_trends()

        report = self.ai_service.generate_report(user_id, nfts, market_data)
        self.logger.debug(f"Report generated for User ID {user_id}: {report}")
        return report

    def save_report(self, user_id, report):
        """
        Save the generated report to the database.

        Args:
            user_id (str): The ID of the user.
            report (str): The report content.
        """
        self.logger.info(f"Saving report for User ID: {user_id}")
        self.db_connector.insert_report(user_id, report)
        self.logger.info("Report saved successfully.")

    def retrieve_report(self, report_id):
        """
        Retrieve a report by its ID.

        Args:
            report_id (str): The ID of the report.

        Returns:
            str: Report content.
        """
        self.logger.info(f"Retrieving report with ID: {report_id}")
        report = self.db_connector.fetch_report(report_id)
        if report:
            self.logger.debug(f"Report retrieved: {report}")
            return report
        else:
            self.logger.error(f"Report with ID {report_id} not found.")
            raise ValueError("Report not found.")
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
