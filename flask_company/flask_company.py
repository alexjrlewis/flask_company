"""

    A Flask extension providing.
    
    (c) 2020 by getintocrypto.io. 
"""

from typing import Optional
from flask import Flask

class Company():
    """

    Attributes:
        name: The name of the company.
        email: The email contact of the company.
        address: The address of the company.
        number: The company's number on https://www.gov.uk/government/organisations/companies-house
        url: The URL of the company, <company name>.com
        twitter: The twitter handle of the company.
        instagram: The instagram handle of the company.
        whereby: The whereby handle of the company.

    """

    def __init__(self, app: Optional[flask.app.Flask] = None):
        """Initiates a new instance."""
        if app is not None:
            self.init_app(app)

    def init_app(self, app: flask.app.flask):
        """Initializes the application with the extension.

        Args:
            app: The Flask application object.
        """
        self.name = app.config.get('COMPANY_NAME', '')
        self.email = app.config.get('COMPANY_EMAIL', '')
        self.address = app.config.get('COMPANY_ADDRESS', '')
        self.number = app.config.get('COMPANY_NUMBER', '')
        self.url = app.config.get('COMPANY_URL', '')
        self.twitter = app.config.get('COMPANY_TWITTER', '')
        self.instagram = app.config.get('COMPANY_INSTAGRAM', '')
        self.whereby = app.config.get('COMPANY_WHEREBY', '')

    @property
    def twitter(self) -> str:
        return f'https://twitter.com/{self._twitter}'

    @twitter.setter
    def twitter(self, twitter: str):
        self._twitter = twitter

    @property
    def instagram(self) -> str:
        return f'https://instagram.com/{self._instagram}'

    @instagram.setter
    def instagram(self, instagram: str):
        self._instagram = instagram
    
    @property
    def whereby(self) -> str:
        return f'https://whereby.com/{self._whereby}'

    @whereby.setter
    def whereby(self, whereby: str) -> str:
        self._whereby = whereby

def main():
    pass

if __name__ == '__main__':
    main()    
