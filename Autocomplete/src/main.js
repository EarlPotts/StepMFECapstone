var trie;
module.exports.setup= ()=>{
    trie = new Trie();
    trie.addMultiple(["apple", "Apple", "adage", "application", "bread","dictionary", "couch", "accordion"]);
    return trie;
}

//create a class trie nodes and the trie
class TrieNode{
    constructor(value) {
    this.children = {};
    this.lastLetter = false;
    this.letter = value;
  }
}

class Trie extends TrieNode{
    constructor(){super(null);}

    add(word){
        word = word.toLowerCase();
        const addRecursive = (node, wordLeft) => {
            //if no node for the letter, create a new one and place it
            const letter = wordLeft[0];
            if(node.children[letter] == null){
                node.children[letter] = new TrieNode(letter);
                //check if it's the last letter in the word
                if(wordLeft.length == 1){
                    node.children[letter].lastLetter = true;
                    return;
                }
            }
            //do recursion on the rest of the word
            if(wordLeft.length > 1){
                addRecursive(node.children[letter], wordLeft.substring(1));
            }
        };

        //call the method using the root node as a starter
        addRecursive(this, word)
    }

    addMultiple(wordList){
        for(let i in  wordList){
            this.add(wordList[i]);
        }
    }

    guessWord(guess){
        //create a list to store the matches
        var matches = [];
        //recursive method to get all matches for a given phrase and add to list
        var getMatches = function(stringLeft, node){
            //loop through node's children
            for(let letter in node.children){
                //store the child node and check if that is the end of a word
                const child = node.children[letter];
                if(child.lastLetter){
                    //add the new word to the list
                    matches.push(stringLeft + child.letter);
                }
                getMatches(stringLeft+letter, child);
            }
        }

        var startNode = this;
        var word = guess;
        //traverse through the tree until we get to the end of our guess
        while(word){
            startNode = startNode.children[word[0]];
            word = word.substring(1);
        }
        //find all the words from our guess starting point, if it exists
        if(startNode){
            getMatches(guess, startNode);
        }
        return matches.sort();
    }


}
//add to trie
//method to give in input of letters and give back list of matching words
//take the input and find subtrees that make up a word from the starting point to the
//termination node

//once we traverse through the given string, keep storing that string, and as we traverse the sub trees
//keep track of the string we build, then once we get to the termination charcter add to our list or results