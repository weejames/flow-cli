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

### Teams API

```bash
python3 flow-cli.py [--api-key YOUR_API_KEY] teams [options]
```

#### Options

--parent-isnull: Filter results to only return top level teams
--parent: Filter results to only subteams of the specified Team ID

### Pull Request Metrics API

```bash
python3 flow-cli.py [--api-key YOUR_API_KEY] prs [options]
```

#### Options

--team-id: Filter results to those for a single team
--date-range: Filter results by date range; format is "[yyyy-mm-dd:yyyy-mm-dd]"
--include-nested-teams: Include nested teams when calculating results; true or false

### Code Fundamentals API

```bash
python3 flow-cli.py [--api-key YOUR_API_KEY] code [options]
```

#### Options

--team-id: Filter results to those for a single team; defaults to account level
--start-date: Only include data from this date; format is `yyyy-mm-dd`
--end-date: Only include data to this date; format is `yyyy-mm-dd`
--include-nested-teams: Include nested teams when calculating results; `true` or `false`; default `true`
--resolution: Defaults to `period` set by date range, can also be set to `week`


## License

This project is licensed under the MIT License.