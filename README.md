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

## License

This project is licensed under the MIT License.