layout: post
title: My codewars(4)
description: "codewars"
tags: [技术,codewars]
image:
  background: triangular.png
comments: true
share: true
---

24.

Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').

Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').

Create a funciton which translates a given DNA string into RNA.

For example:

```DNAtoRNA("GCAT") returns ("GCAU")```

solution:

    function DNAtoRNA(dna){
      return dna.replace(/T/g, 'U');
    }

or

    function DNAtoRNA(dna) {
      return dna.split("T").join("U");
    }

25.

Create a function that takes an integer as an argument and returns "Even" or "Odd".

    function even_or_odd(number) {
      if (number%2==0) {
                        return "Even";
                    }else{
                        return "Odd";
                    }
    }
    function even_or_odd(number) {
     return number%2==0?"Even":"Odd";
    }

26.

I would like to be able to pass an array with two elements to my swapValues function to swap the values. However it appears that the values aren't changing.

Can you figure out what's wrong here?

example:

    function swapValues() {
        var args = Array.prototype.slice.call(arguments);
        var temp = args[0];
        args[0] = args[1];
        args[1] = temp;
    }

solution 1:

    function swapValues(args) {
        var temp = args[0];
        args[0] = args[1];
        args[1] = temp;
    }

solution 2:

    function swapValues(args) {
        args[1] = [args[0], args[0] = args[1]][0];
    }

solution 3:

    function swapValues() {
      return arguments[0].reverse();
    }

good discourse about solution 3:

![img](http://7vznhl.com1.z0.glb.clouddn.com/2015-5-16-1codewars1.png)

27.

Description:

Complete the bool_to_word (Javascript: boolToWord ) method.

Given: a boolean value

Return: a 'Yes' string for true and a 'No' string for false

solution:

    function boolToWord( bool ){
      return bool ? 'Yes':'No';
    }

28.

Description:

Code as fast as you can! You need to double the integer and return it.

solution:

    function doubleInteger(i) {
      // i will be an integer. Double it and return it.
      return i * 2;
    }

29.

Description:

Regular Ball Super Ball

Create a class Ball.

Ball objects should accept one argument for "ball type" when instantiated.

If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

for example:

```ball1 = new Ball();```
```ball2 = new Ball("super");```

```ball1.ballType     //=> "regular"```
```ball2.ballType     //=> "super"```

solution:

    var Ball = function(ballType) {
      if (!ballType){
        this.ballType = 'regular';
      }
      else {
        this.ballType= 'super';
      }
    };

or:

    var Ball = function(ballType) {
      this.ballType = ballType ? ballType : "regular";
    };
    var Ball = function(ballType) {
      this.ballType = ballType || 'regular';
    };

30.

Sentence Smash

Write a method smash that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!

Example

```var words = ['hello', 'world', 'this', 'is', 'great'];```
```smash(words); // returns "hello world this is great"```

solution:

    function smash (words) {
        var string = words.join(" ");
        return string; 
    };
