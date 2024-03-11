from flask import Blueprint, render_template,request,flash, redirect,url_for
import csv
import random
import math
import numpy as np
import pandas as pd




views = Blueprint('views',__name__)

@views.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST' :
        runs= float(request.form.get('runs'))
        overs = float(request.form.get('overs'))
        wickets=float(request.form.get('wickets'))
        runslast=float(request.form.get('runslast'))
        wicketslast=float(request.form.get('wicketslast'))
        striker=float(request.form.get('striker'))
        nonstriker=float(request.form.get('nonstriker'))
        playingteam=request.form.get('teamp')
        bowlingteam=request.form.get('teamb')
        print(runs,overs,wickets,runslast,wicketslast,striker,nonstriker,playingteam,bowlingteam)
        beta=[[ 1.60145545e+02],[ 1.22012119e+00],[-7.43350817e+00],[-6.16768526e+00],[-4.53106981e-02],[-2.39623370e+00],[-1.31971661e-02],[-4.58902951e-02],[-9.12007863e-04],[ 3.77436691e-01],[-3.14798833e-02],[ 1.25782484e-04],[ 1.63558715e-01],[ 7.32348809e-05],[-1.60459852e-03]]
        prediction =int(np.dot([[1,runs,wickets,overs,runslast,wicketslast,striker,nonstriker,np.power(runs,2), np.power(wickets,2), np.power(overs,2), np.power(runslast,2), np.power(wicketslast,2), np.power(striker,2), np.power(nonstriker,2)]],beta))
        s=str(prediction)
        a=s.replace('[','')
        b=a.replace(']','')
        flash('your team '+ playingteam + ' will score ' +b+ " runs against " + bowlingteam,category='success')
        return redirect(url_for('views.result'))
    return render_template("Ipl.htm")



@views.route('/tp')
def tp():
    
    return render_template("tp.htm")


@views.route('/result')
def result():
    
    return render_template("Ipl2.htm")


     

