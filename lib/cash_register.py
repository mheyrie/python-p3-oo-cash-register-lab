#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount =  discount
    self.total = 0
    self.items = []
    pass

  def total(self):
    return self.total
  
  def item (self):
    return self.item
  
  def title_price(self, title, price):
    if (type(title) in str) and (type(price) in (int, float)):
      self.total += price
    else:
      pass
