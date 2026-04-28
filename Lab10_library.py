# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:39:44 2026

@author: Priyangan
"""
class LibraryAccount:
    def __init__(self, member_id, books_borrowed, fine_balance):
        self.__member_id = member_id
        self.__books_borrowed = books_borrowed
        self.__fine_balance = fine_balance
    def get_member(self):
        return self.__member_id
    def get_books(self):
        return self.__books_borrowed
    def get_fine(self):
        return self.__fine_balance
    
    def borrow_book(self, count):
        if count > 0:
            self.__books_borrowed+=count
        else:
            print("Invalid Activity")
    
    def return_book(self, count):
        if count>0 and count <=self.__books_borrowed:
            self.__books_borrowed-=count
        else:
            print("Invalid Activity")
    
    def add_fine(self, amount):
       if amount>0:
           self.__fine_balance+=amount
    
    def pay_fine(self, amount):
        if amount>0 and amount <=self.__fine_balance:
            self.__fine_balance-=amount
        else:
            print("Insuffiecient amount in balance")
            
    def transfer_fine(self,amount, acc):
        if amount>0 and amount<=self.__fine_balance:
            self.__fine_balance-=amount
            acc.add_fine(amount)
        else:
            print("Invalid Transaction")
    
            
        
