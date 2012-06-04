'''
Created on May 29, 2012

@author: Michael R. Johnston (mj@thewellrunsite.com)
'''
import unittest
from datetime import date
from amember import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class AmemberTest(unittest.TestCase):

    def setUp(self):
        self.Session = sessionmaker()
        engine = create_engine('mysql://root@localhost/mydb')
        self.Session.configure(bind=engine)
        self.session = self.Session()

    def tearDown(self):
        pass

    def test_CustomerList(self):
        ''' Read through all the customers '''
        c = 0
        for cust in self.session.query(AmemberMember):
            c = c + 1

        print "%s customers in the db" % c

    def test_first(self):
        ''' Print first customer record and orders '''
        cust = self.session.query(AmemberMember).first()
        if cust == None:
            print "Got nothing"
        else:
            print cust.name_l, cust.name_f, cust.email, cust.login

    def test_payments(self):
        ''' Shows the active products for the first account '''
        print "===================="
        cust = self.session.query(AmemberMember).first()
        for payment in cust.payments:
            if (payment.expire_date >= date.today()) and payment.completed:
                print payment.product_id, payment.begin_date, payment.expire_date, payment.amount

    def test_products(self):
        ''' Shows the active products for first account by name '''
        print "====================="
        cust = self.session.query(AmemberMember).first()
        for payment in cust.payments:
            if (payment.expire_date >= date.today()) and payment.completed:
                print payment.product.title, payment.begin_date, payment.expire_date, payment.amount

if __name__ == '__main__':
    unittest.main()
