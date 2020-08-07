//import {fcn} from '../src/main.js';
const main = require('../src/main');

describe("A suite", function() {
  it("contains spec with an expectation", function() {
    var trie = main.setup();
    expect(trie.guessWord("a")).toEqual([ 'accordion', 'adage', 'apple', 'application' ]);
    expect(trie.guessWord("app")).toEqual([ 'apple', 'application' ]);
    expect(trie.guessWord("b")).toEqual([ 'bread']);

  });
});