import pandas as pd
import numpy as np
import matplotlib.pyplot as py


def main_menu():
    print("Your Choices:\n1. Top Players\n2. Club Stats\n3. League Stats")
    mmdec = int(input("Enter Your Choice: "))
    if mmdec == 1:
        top_menu()
    elif mmdec == 2:
        club_menu()
    elif mmdec == 3:
        league_menu()
    else:
        print("Enter appropriate value")


def top_menu():
    print("Your Choices:\n1. By Position\n2. By Performance\n3. Back to Main Menu")
    tmdec = int(input("Enter Your Choice: "))
    if tmdec == 1:
        print("Your Choices:\n1. Defending\n2. Attacking\n3. Goalkeeping\n4. Best Overall Players\n5. Back to Top Menu")
        tm_pos_dec = int(input("Enter Your Choice: "))
        if tm_pos_dec == 1:
            top_def()
        elif tm_pos_dec == 2:
            top_att()
        elif tm_pos_dec == 3:
            top_gk()
        elif tm_pos_dec == 4:
            top_bop()
        elif tm_pos_dec == 5:
            top_menu()
        else:
            print("Enter appropriate value")

    elif tmdec == 2:
        print("Your Choices:\n1. Most Goals\n2. Most Attempts\n3. Best Distribution\n4. Back to Top Menu")
        tm_per_dec = int(input("Enter Your Choice: "))
        if tm_per_dec == 1:
            most_goals()
        elif tm_per_dec == 2:
            most_attempts()
        elif tm_per_dec == 3:
            best_distri()
        elif tm_per_dec == 4:
            top_menu()
        else:
            print("Enter appropriate value")

    elif tmdec == 3:
        main_menu()
    else:
        print("Enter appropriate value")


def club_menu():
    print("Your Choices are:\n1. Most Aggressive Club\n2. Goals Scored\n3. Pass/Cross Accuracy\n4. Goals Conceded\n5. Back to Main Menu")
    cmdec = int(input("Enter Your Choice: "))
    if cmdec == 1:
        most_aggressive()
    elif cmdec == 2:
        goals_scored()
    elif cmdec == 3:
        pass_cross_accuracy()
    elif cmdec == 4:
        goals_conceded()
    elif cmdec == 5:
        main_menu()
    else:
        print("Enter appropriate value")


def league_menu():
    print("Your Choices are:\n1. Total attempts VS attempts on target\n2. Clean sheet by individual keepers/club\n3. Goals saved VS goals conceded\n4. Tackles won VS Tackles Lost\n5. Back to Main Menu")
    lmdec = int(input("Enter Your Choice: "))
    if lmdec == 1:
        totvsat()
    elif lmdec == 2:
        clean_sheet()
    elif lmdec == 3:
        savesvssave()
    elif lmdec == 4:
        tackles()
    elif lmdec == 5:
        main_menu()
    else:
        print("Enter appropriate value")


def top_def():
    defending = pd.read_csv("defending.csv")
    print(defending.head())


def top_att():
    attacking = pd.read_csv("attacking.csv")
    print(attacking.head())


def top_gk():
    gk = pd.read_csv("goalkeeping.csv")
    print(gk.head())


def top_bop():
    bop = pd.read_csv("key_stats.csv")
    print(bop.head())


def most_goals():
    mg = pd.read_csv("goals.csv")
    print(mg.head())


def most_attempts():
    ma = pd.read_csv("attempts.csv")
    print(ma.head())


def best_distri():
    md = pd.read_csv("distribution.csv")
    print(md.head())


def most_aggressive():
    df_attacking = pd.read_csv("attacking.csv")
    club_agg = df_attacking.groupby("club")[["dribbles", "assists"]].sum().sort_values(by="dribbles", ascending=False)
    py.figure(figsize=(10, 8))
    club_agg.plot(kind="bar", stacked=True, color=["red", "blue"], edgecolor="black", ax=py.gca())
    py.title("Most Aggressive Clubs")
    py.xlabel("Club")
    py.ylabel("Total Count")
    py.xticks(rotation=45)
    py.tight_layout()
    py.show()


def goals_scored():
    df_scored = pd.read_csv("goals.csv")
    club_scored = df_scored.groupby("club")[["goals"]].sum().sort_values(by="goals", ascending=False)
    py.figure(figsize=(10, 8))
    club_scored.plot(kind="bar", stacked=True, color=["green"], edgecolor="black", ax=py.gca())
    py.title("Goals Scored")
    py.xlabel("Club")
    py.ylabel("Total Count")
    py.xticks(rotation=45)
    py.tight_layout()
    py.show()


def pass_cross_accuracy():
    df_accuracy = pd.read_csv("distribution.csv")
    club_accuracy = df_accuracy.groupby("club")[["pass_accuracy", "cross_accuracy"]].sum().sort_values(by="pass_accuracy", ascending=False)
    py.figure(figsize=(10, 8))
    club_accuracy.plot(kind="bar", stacked=True, color=["orange", "magenta"], edgecolor="black", ax=py.gca())
    py.title("Pass/Cross Accuracy")
    py.xlabel("Club")
    py.ylabel("Total Count")
    py.xticks(rotation=45)
    py.tight_layout()
    py.show()


def goals_conceded():
    df_accuracy = pd.read_csv("goalkeeping.csv")
    club_conceded = df_accuracy.groupby("club")[["conceded", "saved_penalties"]].sum().sort_values(by="conceded", ascending=False)
    py.figure(figsize=(10, 8))
    club_conceded.plot(kind="bar", stacked=True, color=["cyan", "crimson"], edgecolor="black", ax=py.gca())
    py.title("Goals Conceded")
    py.xlabel("Club")
    py.ylabel("Total Count")
    py.xticks(rotation=45)
    py.tight_layout()
    py.show()


def totvsat():
    df_total = pd.read_csv("attempts.csv").head(30)
    league_total = df_total.groupby("player_name")[["total_attempts", "on_target"]].sum().sort_values(by="total_attempts", ascending=False)
    py.figure(figsize=(10, 8))
    league_total.plot(kind="bar", stacked=True, color=["yellow", "green"], edgecolor="black", ax=py.gca())
    py.title("Total Attempts VS Attempts on Target")
    py.xlabel("Player")
    py.ylabel("Total Count")
    py.xticks(rotation=45)
    py.tight_layout()
    py.show()


def clean_sheet():
    df_clean = pd.read_csv("goalkeeping.csv").head(20)
    league_clean = df_clean.groupby("player_name")[["cleansheets"]].sum().sort_values(by="cleansheets", ascending=False)
    py.figure(figsize=(10, 8))
    league_clean.plot(kind="bar", stacked=True, color=["blue"], edgecolor="black", ax=py.gca())
    py.title("Clean Sheets")
    py.xlabel("Player")
    py.ylabel("Total Count")
    py.xticks(rotation=45)
    py.tight_layout()
    py.show()


def savesvssave():
    df_saves = pd.read_csv("goalkeeping.csv").head(30)
    league_saves = df_saves.groupby("club")[["saved", "conceded"]].sum().sort_values(by="saved", ascending=False)
    py.figure(figsize=(10, 8))
    league_saves.plot(kind="bar", stacked=True, color=["cyan", "black"], edgecolor="black", ax=py.gca())
    py.title("Goals Saved VS Goals Conceded")
    py.xlabel("Club")
    py.ylabel("Total Count")
    py.xticks(rotation=45)
    py.tight_layout()
    py.show()


def tackles():
    tac = pd.read_csv("defending.csv").head(35)
    league_tac = tac.groupby("club")[["t_won", "t_lost"]].sum().sort_values(by="t_won", ascending=False)
    py.figure(figsize=(10, 8))
    league_tac.plot(kind="bar", stacked=True, color=["purple", "black"], edgecolor="black", ax=py.gca())
    py.title("Tackles Won VS Tackles Lost")
    py.xlabel("Club")
    py.ylabel("Total Count")
    py.xticks(rotation=45)
    py.tight_layout()
    py.show()


main_menu()
