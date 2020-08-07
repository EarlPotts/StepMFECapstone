'''
inputs:
  b: a list of tuples
    each tuple contains information on a particular business
    first element: name or ID of the business
    second element: cost to invest in that business
    third element: value score of that business
  m: the amount of money the investor has to spend, in hundreds
output: a tuple 
  first element: the businesses in our optimal portfolio
  second element: the maximum value of our optimal portfolio, calculated based on relevance
'''

def create_portfolio(b, m):
  # first we create two matrices of businesses + 1 rows, money + 1 columns, one of potential businesses, one of selected
  potential = [[0 for x in range(m + 1)] for y in range(len(b) + 1)]
  selected = [[[] for x in range(m + 1)] for y in range(len(b) + 1)]
  # at row i, column j, we have a subproblem of i businesses and a portfolio of j money
  for i in range(1, len(b) + 1): 
    for j in range(1, m + 1):
      # calculate the maximum value without our current business
      max_without_curr = potential[i - 1][j]
      # set the maximum value with our current business to 0 because we don't know our current business' cost yet
      max_with_curr = 0
      cost_of_curr = b[i - 1][1]
      # if our current business' cost fits into the portfolio 
      if j >= cost_of_curr: 
        # calculate the remaining cost we have to spend on other businesses
        remaining_cost = j - cost_of_curr
        # calculate the total value of our current business and the other businesses that fit into the portfolio
        max_with_curr = b[i - 1][2] + potential[i - 1][remaining_cost]
      # set the total value 
      if max_with_curr > max_without_curr:
        potential[i][j] = max_with_curr
        # add our current business to our subproblem's selected businesses
        selected[i][j].append(b[i - 1][0])
        # add the other businesses that fit into the portfolio to our subproblem's selected businesses
        selected[i][j].extend(selected[i - 1][remaining_cost])
      else: 
        potential[i][j] = max_without_curr 
        selected[i][j].extend(selected[i - 1][j])
  # return the optimal portfolio's businesses and their total value
  return (selected[len(b)][m], potential[len(b)][m])
