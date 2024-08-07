import argparse
import json

from apis import customer_core_teams, collaboration_pullrequest_metrics, customer_metrics_code_fundamentals_period_metrics, dora_build_release
from utils import auth

def main():
    parser = argparse.ArgumentParser(
        description="CLI application to interact with Pluralsight Flow APIs"
    )
    parser.add_argument('--api-key', type = str, help = "Pluralsight Flow API Key for authentication")

    subparsers = parser.add_subparsers(dest = 'command')

    # Subcommand for customer_core_teams API & filters
    parser_customer_core_teams = subparsers.add_parser('teams', help='Interact with Teams API')
    parser_customer_core_teams.add_argument('--parent', type = str, help = "Filter response by Parent Team ID")
    parser_customer_core_teams.add_argument('--parent-isnull', type = str, default = "false", help = "Only fetch teams with a null Parent Team ID")

    # Subcommand for collaboration_pullrequest_metrics API & filters
    parser_collaboration_pullrequest_metrics = subparsers.add_parser('collaboration', help='Interact with Collaboration Metrics API')
    parser_collaboration_pullrequest_metrics.add_argument('--date-range', type = str, help = "Filter response by date range - pattern: [YYYY-MM-DD:YYYY-MM-DD]", required = True)
    parser_collaboration_pullrequest_metrics.add_argument('--team-id', type = str, help = "Fetch metrics for this Team ID")
    parser_collaboration_pullrequest_metrics.add_argument('--include-nested-teams', type = str, default = "true", help = "Include nested teams in response.")

    # Subcommand for customer_metrics_code_fundamentals API & filters
    parser_collaboration_pullrequest_metrics = subparsers.add_parser('code', help='Interact with Code Fundamentals API')
    parser_collaboration_pullrequest_metrics.add_argument('--start-date', type = str, help = "Filter response by date range")
    parser_collaboration_pullrequest_metrics.add_argument('--end-date', type = str, help = "Filter response by date range")
    parser_collaboration_pullrequest_metrics.add_argument('--team-id', type = str, help = "Fetch metrics for this Team ID")
    parser_collaboration_pullrequest_metrics.add_argument('--include-nested-teams', type = str, default = "true", help = "Include nested teams in response.")
    parser_collaboration_pullrequest_metrics.add_argument('--resolution', type = str, default = "period", help = "Period.")

    # Subcommand for DORA API & filters
    parser_dora = subparsers.add_parser('dora', help='Interact with DORA API')

    subparser_dora = parser_dora.add_subparsers(dest="subcommand")

    parser_dora_frequency_metrics = subparser_dora.add_parser('frequency', help='Interact with DORA Frequency API')
    parser_dora_frequency_metrics.add_argument('--date-range', type = str, help = "Filter response by date range")
    parser_dora_frequency_metrics.add_argument('--include-nested-teams', type = str, default = "true", help = "Include nested teams in response.")
    parser_dora_frequency_metrics.add_argument('--team-id', type = str, help = "Fetch metrics for this Team ID")
    parser_dora_frequency_metrics.add_argument('--resolution', type = str, default = "period", help = "Period.")

    args = parser.parse_args()

    api_key = auth.get_api_key(args.api_key)

    match args.command:
        case "teams":
            teams = customer_core_teams.request(
                api_key,
                args.parent,
                args.parent_isnull
            )

            print(json.dumps(teams, indent = 4))
        case "collaboration":
            pr_metrics = collaboration_pullrequest_metrics.request(
                api_key,
                date_range = args.date_range,
                team_id = args.team_id,
                include_nested_teams = args.include_nested_teams
            )

            print(json.dumps(pr_metrics, indent = 4))
        case "code":
            code_metrics = customer_metrics_code_fundamentals_period_metrics.request(
                api_key,
                start_date = args.start_date,
                end_date = args.end_date,
                team_id = args.team_id,
                include_nested_teams = args.include_nested_teams,
                resolution = args.resolution
            )

            print(json.dumps(code_metrics, indent = 4))
        case "dora":

            match args.subcommand:
                case "frequency":
                    dora_frequency_metrics = dora_build_release.frequency(
                        api_key,
                        date_range = args.date_range,
                        team_id = args.team_id,
                        include_nested_teams = args.include_nested_teams,
                        resolution = args.resolution
                    )

                    print(json.dumps(dora_frequency_metrics, indent = 4))

if __name__ == "__main__":
    main()