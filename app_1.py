# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:27:05 2020

@author: User
"""

from flask import Flask, redirect, url_for,render_template
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
   return render_template('Main.html')

if __name__ == '__main__':
   app.run()