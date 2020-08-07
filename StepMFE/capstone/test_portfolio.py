from .utils import create_portfolio

# Create your tests here.
class TestPortfolioCreation:
  def test_one(self):
    b = [('Google', 8, 4), ('Alphabet', 4, 3), ('YouTube', 4, 2), ('Sidewalk Labs', 2, 1), ('Nest', 3, 3)] 
    m = 10
    assert create_portfolio(b, m) == (['Nest', 'Sidewalk Labs', 'Alphabet'], 7)

  def test_two(self):
    b = [('Microsoft', 7, 5), ('Apple', 5, 3), ('Netflix', 2, 2), ('Amazon', 8, 5), ('Google', 6, 5), ('Facebook', 3, 2)]
    m = 13
    assert create_portfolio(b, m) == (['Google', 'Microsoft'], 10)

  def test_three(self):
    b = [('Park', 23, 92), ('Library', 31, 57), ('Museum', 29, 49), ('Laboratory', 44, 68), ('Theater', 53, 60), ('Lake', 38, 43), ('Gym', 63, 67), ('Cafe', 85, 84), ('Restaurant', 89, 87), ('Store', 82, 72)]
    m = 165
    assert create_portfolio(b, m) == (['Lake', 'Laboratory', 'Museum', 'Library', 'Park'], 309)