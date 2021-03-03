def sockMerchant(n, ar):
    uniques_socks = set(ar)
    number_pairs = 0
    for unique_sock in uniques_socks:
        amount_this_unique_sock = ar.count(unique_sock)
        pairs_this_sock = amount_this_unique_sock // 2
        number_pairs += pairs_this_sock
    return number_pairs
