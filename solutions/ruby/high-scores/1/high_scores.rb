=begin
Write your code for the 'High Scores' exercise in this file. Make the tests in
`high_scores_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/high-scores` directory.
=end

class HighScores
  def initialize(arr)
    @arr = arr
  end

  def scores
    @arr
  end

  def latest
    @arr[-1]
  end

  def personal_best
    @arr.max
  end

  def personal_top_three
    @arr.sort {|x, y| y <=> x}[0,3]
  end

  def latest_is_personal_best?
    @arr[-1] == @arr.max
  end
end