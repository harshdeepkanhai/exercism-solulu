//
// This is only a SKELETON file for the 'OCR Numbers' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

const DIGITS = {
    ' _ | ||_|   ': '0',
    '     |  |   ': '1',
    ' _  _||_    ': '2',
    ' _  _| _|   ': '3',
    '   |_|  |   ': '4',
    ' _ |_  _|   ': '5',
    ' _ |_ |_|   ': '6',
    ' _   |  |   ': '7',
    ' _ |_||_|   ': '8',
    ' _ |_| _|   ': '9',
  };


export const convert = (pattern) => {
  
  const allLines = pattern.split('\n')
  
  if (allLines.length % 4 !== 0) {
    throw new Error('Total number of lines must be divisible by 4.')
  }

  const result = []

  for (let i = 0; i < allLines.length; i += 4) {
    const block = allLines.slice(i, i + 4)
    const width = block[0].length

    if (block.some(line => line.length !== width)) {
      throw new Error('All lines in a block must have equal length.')
    }

    const numDigits = width / 3
    let number = ''

    for (let d = 0; d < numDigits; d++) {
      const digit =
        block[0].slice(d * 3, d * 3 + 3) +
        block[1].slice(d * 3, d * 3 + 3) +
        block[2].slice(d * 3, d * 3 + 3) +
        block[3].slice(d * 3, d * 3 + 3)

      number += DIGITS[digit] || '?'
    }

    result.push(number)
  }

  return result.join(',')
}
