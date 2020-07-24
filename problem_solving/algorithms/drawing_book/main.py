# Programmer: Hugo Leça Ribeiro
# Date: 24/07/2020

# Rather than use loops, we can resume it in a math formula.
# Let's suppose we have a book with 10 pages, and we want to know how many flips we need to get the page 4
# initial_page + flips_needed * pages_for_each_flip = page_we_want + 1
#      1       +      x       *         2           =      4       + 1
#            2x + 1   =  5
#            2x = 4
#            x = 4/2
#            x = 2
# So, the flips we need to get the age 5 starting at page 1 is 2
# We can resume this formula to:   flips_needed = page_we_want // 2

# To go to the end to the begin we can use this formula:
#  turns_needed = (- final_page + page_we_want) // -2


def pageCount(n, p):
    # from begin
    turns_needed_initial = p // 2
    # from the end
    # If the last page is an even number we add 1
    if n % 2 == 0:
        n += 1
    turns_needed_end = (-n + p) // -2
    if turns_needed_initial < turns_needed_end:
        return turns_needed_initial
    else:
        return turns_needed_end
