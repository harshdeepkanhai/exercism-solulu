=begin
Write your code for the 'Resistor Color Duo' exercise in this file. Make the tests in
`resistor_color_duo_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/resistor-color-duo` directory.
=end

class ResistorColorDuo
  RESISTOR_BAND = %w{black brown red orange yellow green blue violet grey white}
  def self.value(colors)
    colors
      .take(2)
      .map { |x| RESISTOR_BAND.index(x) }
      .join.to_i
  end
end