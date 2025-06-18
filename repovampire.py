#!/usr/bin/env python3
#! coding: utf-8
"""
Coded by Br3noAraujo
RepoVampire - A tool to drain all public repositories from a GitHub user.
"""

import argparse
import requests
import os
import sys

# --- Style Definitions ---
# Using 256-color mode for more shades of red
C_RESET = "\033[0m"
C_BANNER_1 = "\033[38;5;196m"
C_BANNER_2 = "\033[38;5;160m"
C_BANNER_3 = "\033[38;5;124m"
C_BANNER_4 = "\033[38;5;88m"
C_TEXT_LIGHT = "\033[38;5;66m"
C_TEXT_DARK = "\033[38;5;124m"
C_ERROR = "\033[38;5;196m"
C_SUCCESS = "\033[38;5;40m"


BANNER = f"""
{C_BANNER_1}    ╦═╗┌─┐┌─┐┌─┐    
{C_BANNER_2}    ╠╦╝├┤ ├─┘│ │    
{C_BANNER_3}    ╩╚═└─┘┴  └─┘    
{C_BANNER_4} ╦  ╦┌─┐┌┬┐┌─┐┬┬─┐┌─┐
{C_BANNER_2} ╚╗╔╝├─┤│││├─┘│├┬┘├┤ 
{C_BANNER_1}  ╚╝ ┴ ┴┴ ┴┴  ┴┴└─└─┘ by Br3noAraujo🩸
{C_RESET}"""

def get_public_repos(username):
    """Fetches all public repository clone URLs for a given GitHub user."""
    repos = []
    page = 1
    while True:
        api_url = f"https://api.github.com/users/{username}/repos?page={page}&per_page=100"
        response = requests.get(api_url)
        if response.status_code == 404:
            print(f"{C_ERROR}Error: GitHub user '{username}' not found. 🩸{C_RESET}")
            sys.exit(1)
        response.raise_for_status()  # Raise an exception for other bad statuses
        
        data = response.json()
        if not data:
            break
        
        for repo in data:
            repos.append(repo['clone_url'])
        page += 1
        
    return repos

def main():
    """Main function to parse arguments and clone repos."""
    print(BANNER)

    parser = argparse.ArgumentParser(
        description=f"{C_TEXT_LIGHT}RepoVampire - A tool to drain all public repositories from a GitHub user. 🩸{C_RESET}",
        epilog=f"{C_BANNER_1}Enjoy the hunt!{C_RESET}",
        formatter_class=argparse.RawTextHelpFormatter,
        add_help=False # We'll handle help manually to show banner first
    )
    parser.add_argument("username", nargs='?', default=None, help="The GitHub username to target.")
    parser.add_argument("-h", "--help", action="store_true", help="Show this help message and exit")

    args = parser.parse_args()

    # Show detailed help if -h or --help is used
    if args.help:
        parser.print_help()
        sys.exit(0)

    # Show minimalist usage if no username is provided
    if not args.username:
        print(f"\n{C_TEXT_LIGHT}Usage: python3 {os.path.basename(sys.argv[0])} <username> 🩸{C_RESET}")
        print(f"{C_BANNER_1}Use -h or --help for more details.{C_RESET}")
        sys.exit(0)
    
    target_user = args.username
    
    print(f"{C_TEXT_LIGHT}Searching for public repositories for {C_TEXT_DARK}{target_user}{C_TEXT_LIGHT}...{C_RESET}")
    
    try:
        repo_urls = get_public_repos(target_user)
    except requests.exceptions.RequestException as e:
        print(f"{C_ERROR}API Request Failed: {e} 🩸{C_RESET}")
        sys.exit(1)

    if not repo_urls:
        print(f"{C_TEXT_DARK}User '{target_user}' has no public repositories. The hunt is over.{C_RESET}")
        sys.exit(0)

    print(f"{C_SUCCESS}Found {len(repo_urls)} public repositories. Preparing to drain...{C_RESET}\n")

    # Create a directory for the user
    if not os.path.exists(target_user):
        os.makedirs(target_user)
        print(f"{C_TEXT_LIGHT}Created directory: ./{target_user}/{C_RESET}")

    os.chdir(target_user)
    
    for url in repo_urls:
        repo_name = url.split('/')[-1].replace('.git', '')
        print(f"{C_TEXT_DARK}Sinking fangs into {C_TEXT_LIGHT}{repo_name}{C_TEXT_DARK}... 🩸{C_RESET}")
        os.system(f"git clone {url} --quiet")

    print(f"\n{C_SUCCESS}Successfully drained all public repositories from {target_user}. Happy hunting! 🩸{C_RESET}")


if __name__ == "__main__":
    main()








