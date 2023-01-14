"""
Generate a table of contents markdown file for all the markdown files in /docs/, and all its subdirectories.
the generated file should be placed in /docs/ and named "README.md"
the generated file should respect the directory structure of /docs/
the file should look like this:
# Table of Contents

- account-public-service-prod.ol.epicgames.com
    - account
        - api
            - epicdomains
                - [ssodomains](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/account-public-service-prod.ol.epicgames.com/account/api/epicdomains/ssodomains.md)
            - oauth
                - sessions
                    - kill
                        [eg1~eyJraWQiOiJ0RkMyVUloRnBUTV9FYTNxY09kX01xUVQxY0JCbTlrRkxTRGZlSmhzUkc4IiwiYWxnIjoiUFMyNTYifQ.eyJhc](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/account-public-service-prod.ol.epicgames.com/account/api/oauth/sessions/kill/eg1~eyJraWQiOiJ0RkMyVUloRnBUTV9FYTNxY09kX01xUVQxY0JCbTlrRkxTRGZlSmhzUkc4IiwiYWxnIjoiUFMyNTYifQ.eyJhc.md)
                - [exchange](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/account-public-service-prod.ol.epicgames.com/account/api/oauth/exchange.md)
                - [token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/account-public-service-prod.ol.epicgames.com/account/api/oauth/token.md)
                - [verify](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/account-public-service-prod.ol.epicgames.com/account/api/oauth/verify.md)
            - public
                - account
                    - [ec0ebb7e56f6454e86c62299a7b32e20](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/account-public-service-prod.ol.epicgames.com/account/api/public/account/ec0ebb7e56f6454e86c62299a7b32e20.md)
                - [account](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/account-public-service-prod.ol.epicgames.com/account/api/public/account.md)
- datarouter.ol.epicgames.com
    - datarouter
        - api
            - v1
                - public
                    - [data](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/datarouter.ol.epicgames.com/datarouter/api/v1/public/data.md)
###### Generated by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
"""

import os
import json
from datetime import datetime


def main():
    """
    generate a table of contents markdown file for all the markdown files in /docs/, and all its subdirectories.
    the generated file should be placed in /docs/ and named "README.md"
    the generated file should respect the directory structure of /docs/
    the file should look like this:
    # Table of Contents

- account-public-service-prod.ol.epicgames.com
    - account
        - api
            - epicdomains
                - [ssodomains](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/account-public-service-prod.ol.epicgames.com/account/api/epicdomains/ssodomains.md)
            - oauth
                - sessions
                    - kill
                        [eg1~eyJraWQiOiJ0RkMyVUloRnBUTV9FYTNxY09kX01xUVQxY0JCbTlrRkxTRGZlSmhzUkc4IiwiYWxnIjoiUFMyNTYifQ.eyJhc](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/account-public-service-prod.ol.epicgames.com/account/api/oauth/sessions/kill/eg1~eyJraWQiOiJ0RkMyVUloRnBUTV9FYTNxY09kX01xUVQxY0JCbTlrRkxTRGZlSmhzUkc4IiwiYWxnIjoiUFMyNTYifQ.eyJhc.md)
                - [exchange](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/account-public-service-prod.ol.epicgames.com/account/api/oauth/exchange.md)
                - [token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/account-public-service-prod.ol.epicgames.com/account/api/oauth/token.md)
                - [verify](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/account-public-service-prod.ol.epicgames.com/account/api/oauth/verify.md)
            - public
                - account
                    - [ec0ebb7e56f6454e86c62299a7b32e20](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/account-public-service-prod.ol.epicgames.com/account/api/public/account/ec0ebb7e56f6454e86c62299a7b32e20.md)
                - [account](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/account-public-service-prod.ol.epicgames.com/account/api/public/account.md)
- datarouter.ol.epicgames.com
    - datarouter
        - api
            - v1
                - public
                    - [data](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/datarouter.ol.epicgames.com/datarouter/api/v1/public/data.md)
###### Generated by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
    """
    # get all markdown files in /docs/
    markdown_files = []
    for root, dirs, files in os.walk("docs"):
        for file in files:
            if file.endswith(".md"):
                markdown_files.append(os.path.join(root, file).replace("\\", "/"))

    # sort the markdown files by their directory structure
    markdown_files.sort()

    # create a table of contents
    toc = "# Table of Contents\n\n"

    # sort the markdown files by their directory structure
    markdown_files.sort()

    # iterate through the markdown files
    for markdown_file in markdown_files:
        # get the file's directory structure
        directory_structure = markdown_file.replace("docs/", "").replace(".md", "").split("/")

        # iterate through the directory structure
        for i in directory_structure:
            # add 4 spaces for each directory
            toc += " "

        # add the markdown file's name and link
        toc += "- [" + directory_structure[-1] + "](" + markdown_file.replace("docs/", "") + ")\n"

    # add the footer to the table of contents
    toc += "\n\n###### Generated by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)"

    # save the table of contents to /docs/README.md
    with open("docs/README.md", "w") as file:
        file.write(toc)


if __name__ == "__main__":
    main()
