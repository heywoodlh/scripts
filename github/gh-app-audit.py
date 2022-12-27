#!/usr/bin/env python3

## This application will use GitHub's API to list all GitHub Apps installed on an organization.
## It will print out the App Name, repository access and permissions granted to the App.

## Example command:
## ./gh-app-audit.py --api "$TOKEN" --org my-org | jq '.installations[] | {app_slug, repository_selection, permissions}'

import requests
import argparse

# Set arguments named '--api' and '--organization'
# If '--organization' is not set permit '--user' to be set
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--api", help="GitHub token with read:org scope", required=True)
parser.add_argument("--org", help="GitHub organization name", required=True)
args = parser.parse_args()

# Function to list app installations for an org or user
def list_app_installations(token, org):
    # Replace YOUR_ACCESS_TOKEN with a personal access token that has the `read:org` and `admin:org` permissions
    headers = {
        "Authorization": "Bearer " + token,
        "Accept": "application/vnd.github+json",
    }

    url = "https://api.github.com/orgs/" + org + "/installations"
    response = requests.get(url, headers=headers)
    print(response.text)

if __name__ == "__main__":
    list_app_installations(args.api, args.org)
