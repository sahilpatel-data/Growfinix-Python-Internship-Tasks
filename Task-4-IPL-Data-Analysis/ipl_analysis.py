import pandas as pd
import matplotlib.pyplot as plt
import os


DATA_FOLDER = "data"
CHARTS_FOLDER = "charts"
REPORTS_FOLDER = "reports"


def create_folders():
    os.makedirs(DATA_FOLDER, exist_ok=True)
    os.makedirs(CHARTS_FOLDER, exist_ok=True)
    os.makedirs(REPORTS_FOLDER, exist_ok=True)


def clean_ipl_data():
    try:
        df = pd.read_csv(f"{DATA_FOLDER}/matches.csv")
    except FileNotFoundError:
        print("Error: data/matches.csv file not found.")
        return None
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

    # Clean column names
    df.columns = df.columns.str.strip()

    # Standardize old team names
    team_name_replacements = {
        "Delhi Daredevils": "Delhi Capitals",
        "Kings XI Punjab": "Punjab Kings",
        "Rising Pune Supergiant": "Rising Pune Supergiants"
    }

    team_columns = ["team1", "team2", "winner", "toss_winner"]

    for col in team_columns:
        if col in df.columns:
            df[col] = df[col].replace(team_name_replacements)

    # Drop rows where winner is missing
    if "winner" in df.columns:
        df = df.dropna(subset=["winner"])

    # Save cleaned dataset
    df.to_csv(f"{DATA_FOLDER}/cleaned_matches.csv", index=False)

    return df


def calculate_team_win_stats(df):
    print("\n===== TEAM WIN ANALYSIS =====\n")

    team1_counts = df["team1"].value_counts()
    team2_counts = df["team2"].value_counts()
    matches_played = team1_counts.add(team2_counts, fill_value=0)

    wins = df["winner"].value_counts()

    stats_df = pd.DataFrame({
        "Matches Played": matches_played,
        "Wins": wins
    }).fillna(0)

    stats_df["Matches Played"] = stats_df["Matches Played"].astype(int)
    stats_df["Wins"] = stats_df["Wins"].astype(int)

    stats_df["Win Rate (%)"] = (stats_df["Wins"] / stats_df["Matches Played"]) * 100
    stats_df["Win Rate (%)"] = stats_df["Win Rate (%)"].round(2)

    stats_df = stats_df.sort_values(by=["Win Rate (%)", "Wins"], ascending=False)

    stats_df.to_csv(f"{DATA_FOLDER}/team_win_stats.csv")

    print("Team win statistics saved.")

    return stats_df


def calculate_kkr_season_performance(df):
    print("\n===== KKR SEASON-WISE PERFORMANCE =====\n")

    kkr_matches = df[(df["team1"] == "Kolkata Knight Riders") | (df["team2"] == "Kolkata Knight Riders")].copy()

    matches_per_season = kkr_matches.groupby("season").size()
    wins_per_season = kkr_matches[kkr_matches["winner"] == "Kolkata Knight Riders"].groupby("season").size()

    season_stats = pd.DataFrame({
        "Matches Played": matches_per_season,
        "Wins": wins_per_season
    }).fillna(0)

    season_stats["Matches Played"] = season_stats["Matches Played"].astype(int)
    season_stats["Wins"] = season_stats["Wins"].astype(int)

    season_stats["Losses"] = season_stats["Matches Played"] - season_stats["Wins"]
    season_stats["Win Rate (%)"] = (season_stats["Wins"] / season_stats["Matches Played"]) * 100
    season_stats["Win Rate (%)"] = season_stats["Win Rate (%)"].round(2)

    season_stats = season_stats.sort_index()
    season_stats.to_csv(f"{DATA_FOLDER}/kkr_season_performance.csv")

    print("KKR season performance saved.")

    return season_stats


def calculate_kkr_toss_decision_stats(df):
    print("\n===== KKR TOSS DECISION ANALYSIS =====\n")

    kkr_toss_wins = df[df["toss_winner"] == "Kolkata Knight Riders"].copy()

    toss_stats = kkr_toss_wins.groupby("toss_decision").size().rename("Total Matches")
    toss_wins = kkr_toss_wins[kkr_toss_wins["winner"] == "Kolkata Knight Riders"].groupby("toss_decision").size().rename("Wins")

    toss_df = pd.DataFrame({
        "Total Matches": toss_stats,
        "Wins": toss_wins
    }).fillna(0)

    toss_df["Total Matches"] = toss_df["Total Matches"].astype(int)
    toss_df["Wins"] = toss_df["Wins"].astype(int)

    toss_df["Losses"] = toss_df["Total Matches"] - toss_df["Wins"]
    toss_df["Win Rate (%)"] = (toss_df["Wins"] / toss_df["Total Matches"]) * 100
    toss_df["Win Rate (%)"] = toss_df["Win Rate (%)"].round(2)

    toss_df.to_csv(f"{DATA_FOLDER}/kkr_toss_decision_stats.csv")

    print("KKR toss decision stats saved.")

    return toss_df


def plot_team_win_rates(stats_df):
    plt.figure(figsize=(12, 6))
    stats_df["Win Rate (%)"].plot(kind="bar")
    plt.title("IPL Team Win Rates")
    plt.xlabel("Teams")
    plt.ylabel("Win Rate (%)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(f"{CHARTS_FOLDER}/team_win_rate_chart.png")
    plt.close()


def plot_kkr_season_performance(season_stats):
    plt.figure(figsize=(10, 5))
    season_stats["Win Rate (%)"].plot(kind="line", marker="o")
    plt.title("KKR Season-wise Win Rate")
    plt.xlabel("Season")
    plt.ylabel("Win Rate (%)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{CHARTS_FOLDER}/kkr_season_win_rate_chart.png")
    plt.close()


def plot_kkr_toss_decision_stats(toss_df):
    plt.figure(figsize=(8, 5))
    toss_df["Win Rate (%)"].plot(kind="bar")
    plt.title("KKR Win Rate by Toss Decision")
    plt.xlabel("Toss Decision")
    plt.ylabel("Win Rate (%)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(f"{CHARTS_FOLDER}/kkr_toss_decision_chart.png")
    plt.close()


def generate_summary_report(team_stats, season_stats, toss_stats):
    top_team = team_stats.iloc[0]
    top_team_name = team_stats.index[0]
    top_3_teams = team_stats.head(3)

    best_kkr_season = season_stats["Win Rate (%)"].idxmax()
    worst_kkr_season = season_stats["Win Rate (%)"].idxmin()

    best_kkr_win_rate = season_stats.loc[best_kkr_season, "Win Rate (%)"]
    worst_kkr_win_rate = season_stats.loc[worst_kkr_season, "Win Rate (%)"]

    total_kkr_matches = season_stats["Matches Played"].sum()
    total_kkr_wins = season_stats["Wins"].sum()

    best_toss_decision = toss_stats["Win Rate (%)"].idxmax()
    best_toss_win_rate = toss_stats.loc[best_toss_decision, "Win Rate (%)"]

    report_lines = []

    report_lines.append("IPL DATA ANALYSIS REPORT")
    report_lines.append("=" * 50)
    report_lines.append("")

    report_lines.append("1. OVERALL TEAM PERFORMANCE")
    report_lines.append("-" * 50)
    report_lines.append(
        f"Top team by win rate: {top_team_name} "
        f"({top_team['Win Rate (%)']}% win rate, "
        f"{top_team['Wins']} wins in {top_team['Matches Played']} matches)"
    )
    report_lines.append("")
    report_lines.append("Top 3 teams by win rate:")
    for team_name, row in top_3_teams.iterrows():
        report_lines.append(
            f"- {team_name}: {row['Win Rate (%)']}% win rate, "
            f"{row['Wins']} wins in {row['Matches Played']} matches"
        )

    report_lines.append("")
    report_lines.append("2. KKR SEASON-WISE PERFORMANCE")
    report_lines.append("-" * 50)
    report_lines.append(
        f"Best KKR season: {best_kkr_season} with {best_kkr_win_rate}% win rate"
    )
    report_lines.append(
        f"Worst KKR season: {worst_kkr_season} with {worst_kkr_win_rate}% win rate"
    )
    report_lines.append(f"Total KKR matches in dataset: {total_kkr_matches}")
    report_lines.append(f"Total KKR wins in dataset: {total_kkr_wins}")

    report_lines.append("")
    report_lines.append("3. KKR TOSS DECISION ANALYSIS")
    report_lines.append("-" * 50)
    for decision, row in toss_stats.iterrows():
        report_lines.append(
            f"When KKR chose to {decision}: "
            f"{row['Wins']} wins out of {row['Total Matches']} matches "
            f"({row['Win Rate (%)']}% win rate)"
        )

    report_lines.append("")
    report_lines.append(
        f"Better toss decision for KKR based on this dataset: "
        f"{best_toss_decision} ({best_toss_win_rate}% win rate)"
    )

    with open(f"{REPORTS_FOLDER}/analysis_summary.txt", "w", encoding="utf-8") as file:
        for line in report_lines:
            file.write(line + "\n")


def main():
    create_folders()

    df = clean_ipl_data()

    if df is not None:
        team_stats = calculate_team_win_stats(df)
        kkr_season_stats = calculate_kkr_season_performance(df)
        kkr_toss_stats = calculate_kkr_toss_decision_stats(df)

        plot_team_win_rates(team_stats)
        plot_kkr_season_performance(kkr_season_stats)
        plot_kkr_toss_decision_stats(kkr_toss_stats)

        generate_summary_report(team_stats, kkr_season_stats, kkr_toss_stats)

        print("\nAll files generated successfully in data/, charts/, and reports/ folders.")


if __name__ == "__main__":
    main()