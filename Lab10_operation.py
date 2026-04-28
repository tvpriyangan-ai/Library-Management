# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:40:53 2026

@author: Priyangan
"""
from Lab10_library import LibraryAccount

member1=LibraryAccount(201, 2, 50)
member2=LibraryAccount(202,2,50)
member_list=[member1, member2]


for member in member_list:
    member.borrow_book(1)
    
for member in member_list:
    member.return_book(1)
    
for member in member_list:
   member.add_fine(20)
    
for member in member_list:
    print(member.get_member(), member.get_fine())
    
member2.transfer_fine(30,member1)

for member in member_list:
    print(member.get_member(), member.get_fine())
    