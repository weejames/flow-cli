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
    parser_customer_core_teams.add_argument('--parent--isnull', type = str, default = "false", help = "Only fetch teams with a null Parent Team ID")

    # Subcommand for collaboration_pullrequest_metrics API & filters
    parser_collaboration_pullrequest_metrics = subparsers.add_parser('collaboration', help='Interact with Collaboration Metrics API')
    parser_collaboration_pullrequest_metrics.add_argument('--date-range', type = str, help = "Filter response by date range - pattern: [YYYY-MM-DD:YYYY-MM-DD]", required = True)
    parser_collaboration_pullrequest_metrics.add_argument('--apex-user-id', type=str, help="Fetch metrics for apex_user_id")
    parser_collaboration_pullrequest_metrics.add_argument('--apex-user-id--in', type=str, help="Fetch metrics for apex_user_id__in")
    parser_collaboration_pullrequest_metrics.add_argument('--team-id', type=str, help="Fetch metrics for team_id")
    parser_collaboration_pullrequest_metrics.add_argument('--team-id--in', type=str, help="Fetch metrics for team_id__in")
    parser_collaboration_pullrequest_metrics.add_argument('--repo-id', type=str, help="Fetch metrics for repo_id")
    parser_collaboration_pullrequest_metrics.add_argument('--repo-id--in', type=str, help="Fetch metrics for repo_id__in")
    parser_collaboration_pullrequest_metrics.add_argument('--repo-id-not--in', type=str, help="Fetch metrics for repo_id_not__in")
    parser_collaboration_pullrequest_metrics.add_argument('--repo-tag-id', type=str, help="Fetch metrics for repo_tag_id")
    parser_collaboration_pullrequest_metrics.add_argument('--repo-tag-id--in', type=str, help="Fetch metrics for repo_tag_id__in")
    parser_collaboration_pullrequest_metrics.add_argument('--repo-name', type=str, help="Fetch metrics for repo_name")
    parser_collaboration_pullrequest_metrics.add_argument('--include-nested-teams', type=str, help="Fetch metrics for include_nested_teams", default="true")
    parser_collaboration_pullrequest_metrics.add_argument('--include-weekly-data', type=str, help="Fetch metrics for include_weekly_data")
    parser_collaboration_pullrequest_metrics.add_argument('--fields', type=str, help="Fetch metrics for fields")
    parser_collaboration_pullrequest_metrics.add_argument('--metrics', type=str, help="Fetch metrics for metrics")

    # Subcommand for customer_metrics_code_fundamentals API & filters
    parser_collaboration_code_metrics = subparsers.add_parser('code', help='Interact with Code Fundamentals API')
    parser_collaboration_code_metrics.add_argument('--start-date', type = str, help = "Filter response by date range - pattern YYYY-MM-DD", required="true")
    parser_collaboration_code_metrics.add_argument('--end-date', type = str, help = "Filter response by date range")
    parser_collaboration_code_metrics.add_argument('--team-id', type = str, help = "Fetch metrics for this Team ID")
    parser_collaboration_code_metrics.add_argument('--team-id--in', type = str, help = "Fetch metrics for this Team ID")
    parser_collaboration_code_metrics.add_argument('--include-nested-teams', type = str, default = "true", help = "Include nested teams in response.")
    parser_collaboration_code_metrics.add_argument('--resolution', type = str, default = "period", help = "Period.")
    parser_collaboration_code_metrics.add_argument('--apex-user-id', type=str, help="Filter response by apex_user_id")
    parser_collaboration_code_metrics.add_argument('--apex-user-id--in', type=str, help="Filter response by apex_user_id__in")
    parser_collaboration_code_metrics.add_argument('--repo-id', type=str, help="Filter response by repo_id")
    parser_collaboration_code_metrics.add_argument('--repo-id--in', type=str, help="Filter response by repo_id__in")
    parser_collaboration_code_metrics.add_argument('--repo-id-not--in', type=str, help="Filter response by repo_id_not__in")
    parser_collaboration_code_metrics.add_argument('--repo-tag-id', type=str, help="Filter response by repo_tag_id")
    parser_collaboration_code_metrics.add_argument('--repo-tag-id--in', type=str, help="Filter response by repo_tag_id__in")
    parser_collaboration_code_metrics.add_argument('--repo-name', type=str, help="Filter response by repo_name")
   
    # Subcommand for DORA API & filters
    parser_dora = subparsers.add_parser('dora', help='Interact with DORA API')

    subparser_dora = parser_dora.add_subparsers(dest="subcommand")

    parser_dora_frequency_metrics = subparser_dora.add_parser('deployment-frequency', help='Interact with DORA Frequency API')
    parser_dora_frequency_metrics.add_argument('--date-range', type = str, help = "Filter response by date range")
    parser_dora_frequency_metrics.add_argument('--include-nested-teams', type = str, default = "true", help = "Include nested teams in response.")
    parser_dora_frequency_metrics.add_argument('--team-id', type = str, help = "Fetch metrics for this Team ID")
    parser_dora_frequency_metrics.add_argument('--resolution', type = str, default = "period", help = "Period.")

    parser_dora_leadtime_metrics = subparser_dora.add_parser('change-leadtime', help='Interact with DORA Change Leadtime API')
    parser_dora_leadtime_metrics.add_argument('--date-range', type = str, help = "Filter response by date range")
    parser_dora_leadtime_metrics.add_argument('--include-nested-teams', type = str, default = "true", help = "Include nested teams in response.")
    parser_dora_leadtime_metrics.add_argument('--team-id', type = str, help = "Fetch metrics for this Team ID")
    parser_dora_leadtime_metrics.add_argument('--resolution', type = str, default = "period", help = "Period.")

    parser_dora_changefailure_metrics = subparser_dora.add_parser('incident-change-failure-rate', help='Interact with DORA Incident Change Failure Rate API')
    parser_dora_changefailure_metrics.add_argument('--date-range', type = str, help = "Filter response by date range")
    parser_dora_changefailure_metrics.add_argument('--include-nested-teams', type = str, default = "true", help = "Include nested teams in response.")
    parser_dora_changefailure_metrics.add_argument('--team-id', type = str, help = "Fetch metrics for this Team ID")
    parser_dora_changefailure_metrics.add_argument('--resolution', type = str, default = "period", help = "Period.")

    parser_dora_timetorestore_metrics = subparser_dora.add_parser('incident-time-to-restore', help='Interact with DORA Incident Time to Restore API')
    parser_dora_timetorestore_metrics.add_argument('--date-range', type = str, help = "Filter response by date range")
    parser_dora_timetorestore_metrics.add_argument('--include-nested-teams', type = str, default = "true", help = "Include nested teams in response.")
    parser_dora_timetorestore_metrics.add_argument('--team-id', type = str, help = "Fetch metrics for this Team ID")
    parser_dora_timetorestore_metrics.add_argument('--resolution', type = str, default = "period", help = "Period.")

    args = parser.parse_args()

    api_key = auth.get_api_key(args.api_key)

    api_response = None

    match args.command:
        case "teams":
            api_response = customer_core_teams.request(
                api_key,
                args.parent,
                args.parent__isnull
            )

        case "collaboration":
            api_response = collaboration_pullrequest_metrics.request(
                api_key,
                date_range = args.date_range,
                apex_user_id = args.apex_user_id,
                apex_user_id__in = args.apex_user_id__in,
                team_id = args.team_id,
                team_id__in = args.team_id__in,
                repo_id = args.repo_id,
                repo_id__in = args.repo_id__in,
                repo_id_not__in = args.repo_id_not__in,
                repo_tag_id = args.repo_tag_id,
                repo_tag_id__in = args.repo_tag_id__in,
                repo_name = args.repo_name,
                include_nested_teams = args.include_nested_teams,
                include_weekly_data = args.include_weekly_data,
                fields = args.fields,
                metrics = args.metrics
            )

        case "code":
            api_response = customer_metrics_code_fundamentals_period_metrics.request(
                api_key,
                start_date = args.start_date,
                end_date = args.end_date,
                team_id = args.team_id,
                team_id__in = args.team_id__in,
                include_nested_teams = args.include_nested_teams,
                resolution = args.resolution,
                apex_user_id = args.apex_user_id,
                apex_user_id__in = args.apex_user_id__in,
                repo_id = args.repo_id,
                repo_id__in = args.repo_id__in,
                repo_id_not__in = args.repo_id_not__in,
                repo_tag_id = args.repo_tag_id,
                repo_tag_id__in = args.repo_tag_id__in,
                repo_name = args.repo_name
            )

        case "dora":

            match args.subcommand:
                case "deployment-frequency":
                    api_response = dora_build_release.frequency(
                        api_key,
                        date_range = args.date_range,
                        team_id = args.team_id,
                        include_nested_teams = args.include_nested_teams,
                        resolution = args.resolution
                    )
                
                case "change-leadtime":
                    api_response = dora_build_release.leadtime(
                        api_key,
                        date_range = args.date_range,
                        team_id = args.team_id,
                        include_nested_teams = args.include_nested_teams,
                        resolution = args.resolution
                    )

                case "incident-change-failure-rate":
                    api_response = dora_build_release.changefailure(
                        api_key,
                        date_range = args.date_range,
                        team_id = args.team_id,
                        include_nested_teams = args.include_nested_teams,
                        resolution = args.resolution
                    )
                
                case "incident-time-to-restore":
                    api_response = dora_build_release.time_to_restore(
                        api_key,
                        date_range = args.date_range,
                        team_id = args.team_id,
                        include_nested_teams = args.include_nested_teams,
                        resolution = args.resolution
                    )

    print(json.dumps(api_response, indent = 4))

if __name__ == "__main__":
    main()