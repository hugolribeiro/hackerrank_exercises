def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    amount_games = 0
    while s >= p:
        s -= p
        p -= d
        if p < m:
            p = m
        amount_games += 1
    return amount_games
