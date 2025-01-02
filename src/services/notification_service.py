import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from utils.logger import setup_logger

class NotificationService:
    """
    Service responsible for sending notifications to users.
    """

    def __init__(self, config):
        self.logger = setup_logger(config.get('logging', {}))
        self.smtp_server = config.get('smtp', {}).get('server')
        self.smtp_port = config.get('smtp', {}).get('port', 587)
        self.smtp_user = config.get('smtp', {}).get('username')
        self.smtp_password = config.get('smtp', {}).get('password')
        self.from_email = config.get('smtp', {}).get('from_email')
        self.logger.info("NotificationService initialized.")

    def send_email(self, to_email, subject, body):
        """
        Send an email notification.

        Args:
            to_email (str): Recipient email address.
            subject (str): Email subject.
            body (str): Email body.
        """
        self.logger.info(f"Sending email to {to_email} with subject '{subject}'")
        message = MIMEMultipart()
        message['From'] = self.from_email
        message['To'] = to_email
        message['Subject'] = subject

        message.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_user, self.smtp_password)
                server.send_message(message)
            self.logger.info(f"Email sent successfully to {to_email}")
        except Exception as e:
            self.logger.error(f"Failed to send email to {to_email}: {e}")

    def send_valuation_alert(self, user_email, nft_id, valuation):
        """
        Send a valuation alert to the user.

        Args:
            user_email (str): Recipient email address.
            nft_id (str): ID of the NFT.
            valuation (float): Valuation amount.
        """
        subject = f"Valuation Alert for NFT {nft_id}"
        body = f"Dear User,\n\nThe valuation for your NFT with ID {nft_id} is now ${valuation:.2f}.\n\nBest regards,\nNFT Valuation Advisor"
        self.send_email(user_email, subject, body)

    def send_report(self, user_email, report):
        """
        Send a comprehensive report to the user.

        Args:
            user_email (str): Recipient email address.
            report (str): Report content.
        """
        subject = "Your NFT Valuation Report"
        body = f"Dear User,\n\nHere is your latest NFT valuation report:\n\n{report}\n\nBest regards,\nNFT Valuation Advisor"
        self.send_email(user_email, subject, body)
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
