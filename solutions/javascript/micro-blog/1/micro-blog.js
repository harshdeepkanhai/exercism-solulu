//
// This is only a SKELETON file for the 'Micro-blog' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const truncate = (input) => {
  let str_itr = input[Symbol.iterator]();
  let str_val = ""
  for (let i=0;i<5;i++) {

    let str_add = str_itr.next().value;
    if (str_add) {
      str_val += str_add
    }
  }
  return str_val
};
