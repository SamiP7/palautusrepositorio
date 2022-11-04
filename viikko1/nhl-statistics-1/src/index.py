from statistics import Statistics
from player_reader import PlayerReader
from statistics import SortBy


def main():
    stats = Statistics(
        PlayerReader()
    )
    philadelphia_flyers_players = stats.team("PHI")
    top_scorers = stats.top(10)

    print("Philadelphia Flyers:")
    for player in philadelphia_flyers_players:
        print(player)

    print("Top point goal scorers:")
    for player in stats.top(10, SortBy.GOALS):
        print(player)
    print("Top by assists:")
    for player in stats.top(10, SortBy.ASSISTS):
        print(player)
    print("Top point getters:")
    for player in stats.top(10, SortBy.POINTS):
        print(player)


if __name__ == "__main__":
    main()
