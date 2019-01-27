# Mayeu's Beancount script

A collection of quick'n'dirty scripts I use for my accounting with
[beancount][b].

Since beancount is written in Python 3, all those script are only compatible
with this version of Python.

[b]: http://furius.ca/beancount/

## bean-extract-price

This script generate price transactions to the standard output for all the
currency contains in your beancount files.

### Example

    $ bean-extract-price my-transactions.beancount
    2018-11-02 price EUR                    37.36450741740964078280492768 THB
    
    2018-11-02 price EUR                    35.36842105263157894736842105 TWD
    
    2018-11-02 price LKR                                  0.02 MYR
    
    2018-11-02 price MYR                    7.168458781362007168458781362 THB
    
    2018-11-06 price EUR                    37.32653325202801337842082894 THB
    
    2018-11-08 price CHF                    0.8733024691358024691358024691 EUR
    
    2018-11-11 price THB                    0.02679230769230769230769230769 EUR
    
    2018-11-16 price EUR                    37.29386684962387591580701282 THB
    
    2018-11-24 price EUR                    37.41488237173971828216032842 THB
    
    2018-11-30 price SEK                    0.09707746478873239436619718310 EUR
