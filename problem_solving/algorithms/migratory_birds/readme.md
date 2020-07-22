    birds = [0, 0, 0, 0, 0]
    for bird in arr:
        birds[bird-1] += 1
    highest_value = max(birds)
    result = birds.index(highest_value) + 1
    return result

The logic used was:

Create a list of possibles ids (1 to 5). birds = [0, 0, 0, 0, 0]

For each bird that you saw add 1 to the index of 'birds'

Select the highest value found in 'birds'

Search the index of this highest_value

As the index begin at 0, we need to add 1 in our 'result'