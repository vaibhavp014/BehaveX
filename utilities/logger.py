import logging
import os
from dotenv import load_dotenv

# Load configuration from .env file
load_dotenv()

# Check if logging is enabled
enable_logging = os.getenv("ENABLE_LOGGING", "True").lower() == "true"

if enable_logging:
    # Set up the log directory
    log_dir = "reports/logs"
    os.makedirs(log_dir, exist_ok=True)  # Create the directory if it doesn't exist

    # Configure logging
    log_file = os.path.join(log_dir, "framework_execution.log")
    logging.basicConfig(
        filename=log_file,
        filemode="a",
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )
    logger = logging.getLogger()
else:
    # Configure a basic logger that does nothing
    logger = logging.getLogger()
    logger.addHandler(logging.NullHandler())  # Prevents logging output





# import logging
# import os
#
# # Set up the log directory
# log_dir = "reports/logs"
# os.makedirs(log_dir, exist_ok=True)  # Create the directory if it doesn't exist
#
# # Configure logging
# log_file = os.path.join(log_dir, "framework_execution.log")
# logging.basicConfig(
#     filename=log_file,
#     filemode="a",
#     format="%(asctime)s - %(levelname)s - %(message)s",
#     level=logging.INFO
# )
#
# # Define a logger instance
# logger = logging.getLogger()
