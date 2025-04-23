import os
from dotenv import load_dotenv

load_dotenv()


class FOWOConfig:
    """Configuration class containing arguments for the SDK Client.
    Contains configuration for  the base URL and progressive backoff
    """

    fowo_base_url: str
    fowo_backoff: bool
    fowo_backoff_max_time: int
    fowo_bulk_file_format: str

    def __init__(
        self,
        fowo_base_url: str = None,
        fowo_backoff: bool = True,
        fowo_backoff_max_time: int = 30,
        fowo_bulk_fle_format: str = "csv",
    ):
        """Constructor for configuration class.
        Contains initialization values to overwrite defaults


        Args:
            fowo_base_url(optional):
                The base URL for all the API calls, passthis in or set in environment variable

            fowo_backoff:
                A boolean that determines if the SDK should retry the call using backoff when errors occur.

            fowo_backoff_max_time:
                The max number of seconds the SDK should keep trying an API call before stopping.

            fowo_bulk_file_format:
                if bulk files should be in csv or parquet format.
        """
        self.fowo_base_url = fowo_base_url or os.getenv("FOWO_API_BASE_URL")
        print(f"FOWO_API_BASE_URL in FOWOConfig init: {self.fowo_base_url}")

        if not self.fowo_base_url:
            raise ValueError(
                "Base URL is required.set FOWO_API_BASE_URL environment variable"
            )

        self.fowo_backoff = fowo_backoff
        self.fowo_backoff_max_time = fowo_backoff_max_time
        self.fowo_bulk_file_format = fowo_bulk_fle_format

    def __str__(self):
        """Stringify function to return contents of config object for logging"""
        return f"{self.fowo_base_url} {self.fowo_backoff} {self.fowo_backoff_max_time} {self.fowo_bulk_file_format}"
