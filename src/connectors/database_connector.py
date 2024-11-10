import psycopg2
from psycopg2.extras import RealDictCursor
from utils.logger import setup_logger

class DatabaseConnector:
    """
    Connector to interact with the PostgreSQL database.
    """

    def __init__(self, config):
        self.logger = setup_logger(config.get('logging', {}))
        self.host = config.get('host')
        self.port = config.get('port', 5432)
        self.username = config.get('username')
        self.password = config.get('password')
        self.dbname = config.get('dbname')
        self.connection = self._connect()
        self.logger.info("DatabaseConnector initialized.")

    def _connect(self):
        try:
            conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                user=self.username,
                password=self.password,
                dbname=self.dbname
            )
            self.logger.info("Connected to the PostgreSQL database successfully.")
            return conn
        except psycopg2.Error as e:
            self.logger.error(f"Failed to connect to the database: {e}")
            raise

    def insert_user(self, user):
        """
        Insert a new user into the database.

        Args:
            user (User): The user object to insert.
        """
        self.logger.info(f"Inserting user {user.id} into the database.")
        query = """
        INSERT INTO users (id, username, email, registered_at, nfts_owned)
        VALUES (%s, %s, %s, %s, %s)
        """
        with self.connection.cursor() as cursor:
            cursor.execute(query, (user.id, user.username, user.email, user.registered_at, user.nfts_owned))
            self.connection.commit()
        self.logger.debug(f"User {user.id} inserted successfully.")

    def fetch_user(self, user_id):
        """
        Fetch a user by ID.

        Args:
            user_id (str): The ID of the user.

        Returns:
            dict or None: User data or None if not found.
        """
        self.logger.info(f"Fetching user with ID: {user_id}")
        query = "SELECT * FROM users WHERE id = %s"
        with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, (user_id,))
            user = cursor.fetchone()
        self.logger.debug(f"Fetched user: {user}")
        return user

    def update_user_nfts(self, user_id, nfts_owned):
        """
        Update the NFTs owned by a user.

        Args:
            user_id (str): The ID of the user.
            nfts_owned (list of str): List of NFT IDs.
        """
        self.logger.info(f"Updating NFTs for User ID: {user_id}")
        query = "UPDATE users SET nfts_owned = %s WHERE id = %s"
        with self.connection.cursor() as cursor:
            cursor.execute(query, (nfts_owned, user_id))
            self.connection.commit()
        self.logger.debug(f"NFTs updated for User ID: {user_id}")

    def delete_user(self, user_id):
        """
        Delete a user from the database.

        Args:
            user_id (str): The ID of the user.
        """
        self.logger.info(f"Deleting user with ID: {user_id}")
        query = "DELETE FROM users WHERE id = %s"
        with self.connection.cursor() as cursor:
            cursor.execute(query, (user_id,))
            self.connection.commit()
        self.logger.debug(f"User {user_id} deleted successfully.")

    def fetch_user_nfts(self, user_id):
        """
        Fetch all NFTs owned by a user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            list of dict: List of NFT data.
        """
        self.logger.info(f"Fetching NFTs for User ID: {user_id}")
        query = "SELECT * FROM nfts WHERE owner_id = %s"
        with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, (user_id,))
            nfts = cursor.fetchall()
        self.logger.debug(f"Fetched NFTs: {nfts}")
        return nfts

    def insert_report(self, user_id, report):
        """
        Insert a generated report into the database.

        Args:
            user_id (str): The ID of the user.
            report (str): The report content.
        """
        self.logger.info(f"Inserting report for User ID: {user_id}")
        query = """
        INSERT INTO reports (user_id, report, generated_at)
        VALUES (%s, %s, NOW())
        """
        with self.connection.cursor() as cursor:
            cursor.execute(query, (user_id, report))
            self.connection.commit()
        self.logger.debug(f"Report inserted for User ID: {user_id}")

    def fetch_report(self, report_id):
        """
        Fetch a report by its ID.

        Args:
            report_id (str): The ID of the report.

        Returns:
            dict or None: Report data or None if not found.
        """
        self.logger.info(f"Fetching report with ID: {report_id}")
        query = "SELECT * FROM reports WHERE id = %s"
        with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, (report_id,))
            report = cursor.fetchone()
        self.logger.debug(f"Fetched report: {report}")
        return report

    def close_connection(self):
        """
        Close the database connection.
        """
        self.logger.info("Closing database connection.")
        self.connection.close()
        self.logger.info("Database connection closed.")