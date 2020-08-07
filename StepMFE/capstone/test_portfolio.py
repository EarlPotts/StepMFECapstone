from .utils import create_portfolio

# Create your tests here.
class TestPortfolioCreation:
  def test_various_costs_values_one(self):
    b = [('Google', 8, 4), ('Alphabet', 4, 3), ('YouTube', 4, 2), ('Sidewalk Labs', 2, 1), ('Nest', 3, 3)] 
    m = 10
    assert create_portfolio(b, m) == (['Nest', 'Sidewalk Labs', 'Alphabet'], 7)

  def test_various_costs_values_two(self):
    b = [('Microsoft', 7, 5), ('Apple', 5, 3), ('Netflix', 2, 2), ('Amazon', 8, 5), ('Google', 6, 5), ('Facebook', 3, 2)]
    m = 13
    assert create_portfolio(b, m) == (['Google', 'Microsoft'], 10)

  def test_various_costs_values_three(self):
    b = [('Park', 23, 92), ('Library', 31, 57), ('Museum', 29, 49), ('Laboratory', 44, 68), ('Theater', 53, 60), ('Lake', 38, 43), ('Gym', 63, 67), ('Cafe', 85, 84), ('Restaurant', 89, 87), ('Store', 82, 72)]
    m = 165
    assert create_portfolio(b, m) == (['Lake', 'Laboratory', 'Museum', 'Library', 'Park'], 309)

  def test_very_valuable_expensive_one(self):
    b = [('Google', 12, 14), ('Alphabet', 24, 20), ('YouTube', 15, 10), ('Sidewalk Labs', 5, 4), ('Nest', 14, 9)] 
    m = 25
    assert create_portfolio(b, m) == (['Alphabet'], 20)

  def test_very_valuable_expensive_two(self):
    b = [('Microsoft', 234, 50), ('Apple', 357, 88), ('Netflix', 100, 26), ('Amazon', 120, 35), ('Google', 850, 333), ('Facebook', 54, 22)]
    m = 1000
    assert create_portfolio(b, m) == (['Google', 'Amazon'], 368)

  def test_all_too_expensive_one(self):
    b = b = [('Google', 43, 23), ('Alphabet', 34, 34), ('YouTube', 56, 76), ('Sidewalk Labs', 32, 32), ('Nest', 27, 19)] 
    m = 15
    assert create_portfolio(b, m) == ([], 0)

  def test_all_selectable_one(self):
    b = [('Microsoft', 234, 50), ('Apple', 123, 39), ('Netflix', 100, 26), ('Amazon', 120, 35), ('Google', 150, 333), ('Facebook', 54, 22)]
    m = 1000
    assert create_portfolio(b, m) == (['Facebook', 'Google', 'Amazon', 'Netflix', 'Apple', 'Microsoft'], 505)
