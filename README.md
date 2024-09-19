# flow-cli

A command-line interface to interact with the Pluralsight Flow APIs. Not all APIs are implemented. Just the ones I needed to access.  Outputs the response from the Flow APIs as JSON.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/weejames/flow-cli.git
    cd flow-cli
    ```

2. Install `pipenv` if it's not already installed:
    ```bash
    pip install pipenv
    ```

3. Install the dependencies using `pipenv`:
    ```bash
    pipenv install
    ```

4. Activate the virtual environment:
    ```bash
    pipenv shell
    ```

## Usage

### Running the CLI Application

To run the application, use the following command:
```bash
python3 flow-cli.py [--api-key YOUR_API_KEY] <command> [options]
```

## Supported Commands / APIs

I've only partially documented the available commands. I recommend using the help function to see what's available. Works on sub commands too.

```bash
python3 flow-cli.py --help

python3 flow-cli.py teams --help
```

### Teams API

```bash
python3 flow-cli.py [--api-key YOUR_API_KEY] teams [options]
```

#### Options

* --parent-isnull: Filter results to only return top level teams
* --parent: Filter results to only subteams of the specified Team ID

### Collaboration - Pull Requests API

```bash
python3 flow-cli.py [--api-key YOUR_API_KEY] collaboration [options]
```

#### Options

* --date-range DATE_RANGE Filter response by date range - pattern: [YYYY-MM-DD:YYYY-MM-DD]
* --apex-user-id APEX_USER_ID Fetch metrics for apex_user_id
* --apex-user-id--in APEX_USER_ID__IN Fetch metrics for apex_user_id__in
* --team-id TEAM_ID Fetch metrics for team_id
* --team-id--in TEAM_ID__IN Fetch metrics for team_id__in
* --repo-id REPO_ID Fetch metrics for repo_id
* --repo-id--in REPO_ID__IN Fetch metrics for repo_id__in
* --repo-id-not--in REPO_ID_NOT__IN Fetch metrics for repo_id_not__in
* --repo-tag-id REPO_TAG_ID Fetch metrics for repo_tag_id
* --repo-tag-id--in REPO_TAG_ID__IN Fetch metrics for repo_tag_id__in
* --repo-name REPO_NAME Fetch metrics for repo_name
* --include-nested-teams INCLUDE_NESTED_TEAMS Fetch metrics for include_nested_teams
* --include-weekly-data INCLUDE_WEEKLY_DATA Fetch metrics for include_weekly_data
* --fields FIELDS       Fetch metrics for fields
* --metrics METRICS     Fetch metrics for metrics

### Code Fundamentals API

```bash
python3 flow-cli.py [--api-key YOUR_API_KEY] code [options]
```

#### Options

* --team-id: Filter results to those for a single team; defaults to account level
* --start-date: Only include data from this date; format is `yyyy-mm-dd`
* --end-date: Only include data to this date; format is `yyyy-mm-dd`
* --include-nested-teams: Include nested teams when calculating results; `true` or `false`; default `true`
* --resolution: Defaults to `period` set by date range, can also be set to `week`


## License

This project is licensed under the MIT License.