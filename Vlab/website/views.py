from cmath import sqrt
from gzip import READ
from re import L
import re
from sys import flags
from django.http.request import RawPostDataException
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import numpy as np
from numpy.lib.shape_base import get_array_prepare
from django.urls import reverse
from .models import Post
import math as m

# Create your views here.

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def large(data):
    large = 0.0
    for i in data:
        if i>large:
            large = i
    
    return large

def home(request):

    return render(request,'index.html')

def course(request):

    return render(request,'course.html')

def DOM(request):

    return render(request,'DOM/DOM.html')

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return  render(request,'login.html')

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username is already exist')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email is already exist')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password not matching')
            return redirect('signup')
        
    else:
        return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def experiment(request):


    url1 = Post.objects.filter(name__contains = 'experiment').last()
    return render(request,'experiment.html',{'url1':url1})

def DOMEXP1(request):

    if request.method == 'POST':
        M1 = float(request.POST['val11'])
        M2 = float(request.POST['val12'])

        L1 = float(request.POST['val21'])
        L1 *= 0.01
        L2 = float(request.POST['val22'])
        L2 *= 0.01

        N1 = float(request.POST['val31'])
        N2 = float(request.POST['val32'])

        t1 = float(request.POST['val41'])
        t2 = float(request.POST['val42'])

        th_time1 = 2*3.14*(m.sqrt(L1/9.81))
        th_time2 = 2*3.14*(m.sqrt(L2/9.81))

        exp_time1 = t1/N1
        exp_time2 = t2/N2

        a = th_time1*th_time1
        b = th_time2*th_time2
        c = L1*100
        d = L2*100
        x = [a,b]
        y = [c,d]

        plt.switch_backend('AGG')
        plt.figure(figsize=(5,5))
        plt.title('Relation of T^2 Vs L')
        plt.plot(x,y)
        plt.xticks(rotation=45)
        plt.xlabel('T^2')
        plt.ylabel('L')
        plt.grid()
        plt.tight_layout()
        graph = get_graph()

        url1 = Post.objects.filter(name__contains = 'To verify the relation').last()
        
        data = {
            'M1':M1,
            'M2':M2,
            'url1':url1,
            'chart':graph,
            'exp_time1':exp_time1,
            'exp_time2':exp_time2,
            'th_time1':th_time1,
            'th_time2':th_time2,
        }
        return render(request,'DOM/DOM EXP 1.html',data)
    
    else:
        url1 = Post.objects.filter(name__contains = 'To verify the relation').last()
        
        return render(request,'DOM/DOM EXP 1.html',{'url1':url1})

def DOMEXP2(request):

    if request.method == 'POST':
        
        L1 = float(request.POST['L1'])
        L2 = float(request.POST['L2'])
        L3 = float(request.POST['L3'])

        OG1 = float(request.POST['OG1'])
        OG2 = float(request.POST['OG2'])
        OG3 = float(request.POST['OG3'])

        N1 = float(request.POST['N1'])
        N2 = float(request.POST['N2'])
        N3 = float(request.POST['N3'])

        t1 = float(request.POST['t1'])
        t2 = float(request.POST['t2'])
        t3 = float(request.POST['t3'])

        T1 = t1/N1
        T2 = t2/N2
        T3 = t3/N3

        K_exp1 = m.sqrt(((T1*T1*981*OG1)/39.4784176)-(OG1*OG1))
        K_exp2 = m.sqrt(((T2*T2*981*OG2)/39.4784176)-(OG2*OG2))
        K_exp3 = m.sqrt(((T3*T3*981*OG3)/39.4784176)-(OG3*OG3))

        K_th1 = L1/3.464101615
        K_th2 = L2/3.464101615
        K_th3 = L3/3.464101612

        url1 = Post.objects.filter(name__contains = 'To determine the Radius of Gyration ‘K’ of given compound pendulum and To verify the relation').last()

        data = {
            'L1':L1,
            'OG1':OG1,
            'T1': T1,
            'T2': T2,
            'T3':T3,
            'K_exp1':K_exp1,
            'K_exp2':K_exp2,
            'K_exp3':K_exp3,
            'K_th1': K_th1,
            'K_th2': K_th2,
            'K_th3': K_th3,
            'url1' : url1,
        }

        return render(request,'DOM/DOM EXP 2.html',data)

    else:

        url1 = Post.objects.filter(name__contains = 'To determine the Radius of Gyration ‘K’ of given compound pendulum and To verify the relation').last()
        return render(request,'DOM/DOM EXP 2.html',{'url1':url1})

def DOMEXP3(request):

    if request.method == 'POST':
        
        L1 = float(request.POST['L1'])
        L2 = float(request.POST['L2'])
        L3 = float(request.POST['L3'])

        D1 = float(request.POST['D1'])
        D2 = float(request.POST['D2'])
        D3 = float(request.POST['D3'])

        W1 = float(request.POST['W1'])
        W2 = float(request.POST['W2'])
        W3 = float(request.POST['W3'])

        N1 = float(request.POST['N1'])
        N2 = float(request.POST['N2'])
        N3 = float(request.POST['N3'])

        t1 = float(request.POST['t1'])
        t2 = float(request.POST['t2'])
        t3 = float(request.POST['t3'])

        T1 = t1/N1
        T2 = t2/N2
        T3 = t3/N3

        K_exp1 = m.sqrt((T1*T1*D1*D1*981)/(16*9.86*L1))
        K_exp2 = m.sqrt((T2*T2*D2*D2*981)/(16*9.86*L2))
        K_exp3 = m.sqrt((T3*T3*D3*D3*981)/(16*9.86*L3))

        K_th1 = L1/3.464101615
        K_th2 = L2/3.464101615
        K_th3 = L3/3.464101612

        url1 = Post.objects.filter(name__contains = 'To determine the radius of gyration of given bar by using Bi-Filer suspension').last()

        data = {
            'L1':L1,
            'L2': L2,
            'L3': L3,
            'W1': W1,
            'W2': W2,
            'W3': W3,
            'T1': T1,
            'T2': T2,
            'T3':T3,
            'K_exp1':K_exp1,
            'K_exp2':K_exp2,
            'K_exp3':K_exp3,
            'K_th1': K_th1,
            'K_th2': K_th2,
            'K_th3': K_th3,
            'url1' : url1,
        }

        return render(request,'DOM/DOM EXP 3.html',data)
    
    else:
        url1 = Post.objects.filter(name__contains = 'To determine the radius of gyration of given bar by using Bi-Filer suspension').last()
    
    return render(request,'DOM/DOM EXP 3.html',{'url1':url1})

def DOMEXP4(request):

    if request.method == 'POST':
        
        W1 = float(request.POST['W1'])
        D1 = float(request.POST['D1'])
        K1 = W1/D1

        W2 = float(request.POST['W2'])
        D2 = float(request.POST['D2'])
        K2 = W2/D2

        W3 = float(request.POST['W3'])
        D3 = float(request.POST['D3'])
        K3 = W3/D3

        MK = (K1+K2+K3)/3

        T_th1 = (2*3.14)*(m.sqrt(W1/(MK*981)))
        F_th1 = 1/T_th1
        T_th2 = (2*3.14)*(m.sqrt(W2/(MK*981)))
        F_th2 = 1/T_th2
        T_th3 = (2*3.14)*(m.sqrt(W3/(MK*981)))
        F_th3 = 1/T_th3

        N1 = float(request.POST['N1'])
        t1 = float(request.POST['t1'])
        T_exp1 = t1/N1
        F_exp1 = 1/T_exp1

        N2 = float(request.POST['N2'])
        t2 = float(request.POST['t2'])
        T_exp2 = t2/N2
        F_exp2 = 1/T_exp2
        
        N3 = float(request.POST['N3'])
        t3 = float(request.POST['t3'])
        T_exp3 = t3/N3
        F_exp3 = 1/T_exp3

        url1 = Post.objects.filter(name__contains = 'To study the longitudinal vibrations of helical spring').last()

        data = {
            'W1':W1,
            'W2':W2,
            'W3':W3,
            'K1':K1,
            'K2':K2,
            'K3':K3,
            'MK':MK,
            'T_th1':T_th1,
            'T_th2':T_th2,
            'T_th3':T_th3,
            'T_exp1':T_exp1,
            'T_exp2':T_exp2,
            'T_exp3':T_exp3,
            'F_th1':F_th1,
            'F_th2':F_th2,
            'F_th3':F_th3,
            'F_exp1':F_exp1,
            'F_exp2':F_exp2,
            'F_exp3':F_exp3,
            'url1' : url1,
        }

        return render(request,'DOM/DOM EXP 4.html', data)

    else:
        url1 = Post.objects.filter(name__contains = 'To study the longitudinal vibrations of helical spring').last()
    
    return render(request,'DOM/DOM EXP 4.html',{'url1':url1})

def DOMEXP5(request):

    if request.method == 'POST':
        W1 = float(request.POST['W1'])
        L1 = float(request.POST['L1'])
        K1 = float(request.POST['K1'])
        t1 = float(request.POST['t1'])
        T_exp1 = t1/K1
        Fn_exp1 = 1/T_exp1
        Me1 = W1*((L1*L1)/772.55)
        T_th1 = 2*3.14*m.sqrt(Me1/K1)
        Fn_th1 = 1/T_th1

        W2 = float(request.POST['W2'])
        L2 = float(request.POST['L2'])
        K2 = float(request.POST['K2'])
        t2 = float(request.POST['t2'])
        T_exp2 = t2/K2
        Fn_exp2 = 1/T_exp2
        Me2 = W2*((L2*L2)/772.55)
        T_th2 = 2*3.14*m.sqrt(Me2/K2)
        Fn_th2 = 1/T_th2

        url1 = Post.objects.filter(name__contains = 'To study the un-damped free vibration of equivalent spring mass system').last()

        data = {
            'W1':W1,
            'L1':L1,
            'T_exp1':T_exp1,
            'Fn_exp1':Fn_exp1,
            'T_th1':T_th1,
            'Fn_th1':Fn_th1,
            'W2':W2,
            'L2':L2,
            'T_exp2':T_exp2,
            'Fn_exp2':Fn_exp2,
            'T_th2':T_th2,
            'Fn_th2':Fn_th2,
            'url1' : url1,
        }

        return render(request, 'DOM/DOM EXP 5.html', data)

    else:
        url1 = Post.objects.filter(name__contains = 'To study the un-damped free vibration of equivalent spring mass system').last()
    
    return render(request,'DOM/DOM EXP 5.html',{'url1':url1})

def DOMEXP6(request):

    if request.method == 'POST':
        S11 = float(request.POST['1S1'])
        f11 = S11/6.28
        A11 = float(request.POST['1A1'])
        S12 = float(request.POST['1S2'])
        f12 = S12/6.28
        A12 = float(request.POST['1A2'])
        S13 = float(request.POST['1S3'])
        f13 = S13/6.28
        A13 = float(request.POST['1A3'])
        S14 = float(request.POST['1S4'])
        f14 = S14/6.28
        A14 = float(request.POST['1A4'])
        S15 = float(request.POST['1S5'])
        f15 = S15/6.28
        A15 = float(request.POST['1A5'])
        S16 = float(request.POST['1S6'])
        f16 = S16/6.28
        A16 = float(request.POST['1A6'])
        S17 = float(request.POST['1S7'])
        f17 = S17/6.28
        A17 = float(request.POST['1A7'])
        S18 = float(request.POST['1S8'])
        f18 = S18/6.28
        A18 = float(request.POST['1A8'])
        S19 = float(request.POST['1S9'])
        f19 = S19/6.28
        A19 = float(request.POST['1A9'])
        S110 = float(request.POST['1S10'])
        f110 = S110/6.28
        A110 = float(request.POST['1A10'])

        x1 = [A11,A12,A13,A14,A15,A16,A17,A18,A19,A110]
        y1 = [f11,f12,f13,f14,f15,f16,f17,f18,f19,f110]

        plt.switch_backend('AGG')
        plt.figure(figsize=(5,5))
        plt.title('Relation of amplitude v/s frequency(Three hole open)')
        plt.plot(x1,y1)
        plt.xticks(rotation=45)
        plt.xlabel('Amplitude')
        plt.ylabel('Frequency')
        plt.grid()
        plt.tight_layout()
        graph1 = get_graph()

        S21 = float(request.POST['2S1'])
        f21 = S21/6.28
        A21 = float(request.POST['2A1'])
        S22 = float(request.POST['2S2'])
        f22 = S22/6.28
        A22 = float(request.POST['2A2'])
        S23 = float(request.POST['2S3'])
        f23 = S23/6.28
        A23 = float(request.POST['2A3'])
        S24 = float(request.POST['2S4'])
        f24 = S24/6.28
        A24 = float(request.POST['2A4'])
        S25 = float(request.POST['2S5'])
        f25 = S25/6.28
        A25 = float(request.POST['2A5'])
        S26 = float(request.POST['2S6'])
        f26 = S26/6.28
        A26 = float(request.POST['2A6'])
        S27 = float(request.POST['2S7'])
        f27 = S27/6.28
        A27 = float(request.POST['2A7'])
        S28 = float(request.POST['2S8'])
        f28 = S28/6.28
        A28 = float(request.POST['2A8'])
        S29 = float(request.POST['2S9'])
        f29 = S29/6.28
        A29 = float(request.POST['2A9'])

        x2 = [A21,A22,A23,A24,A25,A26,A27,A28,A29]
        y2 = [f21,f22,f23,f24,f25,f26,f27,f28,f29]

        plt.switch_backend('AGG')
        plt.figure(figsize=(5,5))
        plt.title('Relation of amplitude v/s frequency(Two hole open)')
        plt.plot(x2,y2)
        plt.xticks(rotation=45)
        plt.xlabel('Amplitude')
        plt.ylabel('Frequency')
        plt.grid()
        plt.tight_layout()
        graph2 = get_graph()

        S31 = float(request.POST['3S1'])
        f31 = S31/6.28
        A31 = float(request.POST['3A1'])
        S32 = float(request.POST['3S2'])
        f32 = S32/6.28
        A32 = float(request.POST['3A2'])
        S33 = float(request.POST['3S3'])
        f33 = S33/6.28
        A33 = float(request.POST['3A3'])
        S34 = float(request.POST['3S4'])
        f34 = S34/6.28
        A34 = float(request.POST['3A4'])
        S35 = float(request.POST['3S5'])
        f35 = S35/6.28
        A35 = float(request.POST['3A5'])
        S36 = float(request.POST['3S6'])
        f36 = S36/6.28
        A36 = float(request.POST['3A6'])
        S37 = float(request.POST['3S7'])
        f37 = S37/6.28
        A37 = float(request.POST['3A7'])
        S38 = float(request.POST['3S8'])
        f38 = S38/6.28
        A38 = float(request.POST['3A8'])
        S39 = float(request.POST['3S9'])
        f39 = S39/6.28
        A39 = float(request.POST['3A9'])

        x3 = [A31,A32,A33,A34,A35,A36,A37,A38,A39]
        y3 = [f31,f32,f33,f34,f35,f36,f37,f38,f39]

        plt.switch_backend('AGG')
        plt.figure(figsize=(5,5))
        plt.title('Relation of amplitude v/s frequency(One hole open)')
        plt.plot(x3,y3)
        plt.xticks(rotation=45)
        plt.xlabel('Amplitude')
        plt.ylabel('Frequency')
        plt.grid()
        plt.tight_layout()
        graph3 = get_graph()

        url1 = Post.objects.filter(name__contains = 'To study the forced vibrations of equivalent spring mass system').last()

        data = {
            'chart1': graph1,
            'chart2': graph2,
            'chart3': graph3,
            'url1': url1
        }

        return render(request,'DOM/DOM EXP 6.html', data)
    
    else:
        url1 = Post.objects.filter(name__contains = 'To study the forced vibrations of equivalent spring mass system').last()
    
    return render(request,'DOM/DOM EXP 6.html',{'url1':url1})

def DOMEXP7(request):

    if request.method == 'POST':
        L1= float(request.POST['L1'])
        N1 = float(request.POST['N1'])
        t1 = float(request.POST['t1'])
        T_exp1 = t1/N1
        F_exp1 = 1/T_exp1
        K1 = (0.8*7.95*100)/L1
        T_th1 = 6.28*m.sqrt(0.32/K1)
        F_th1 = 1/T_th1

        L2= float(request.POST['L2'])
        N2 = float(request.POST['N2'])
        t2 = float(request.POST['t2'])
        T_exp2 = t2/N2
        F_exp2 = 1/T_exp2
        K2 = (0.8*7.95*100)/L2
        T_th2 = 6.28*m.sqrt(0.32/K2)
        F_th2 = 1/T_th2

        L3= float(request.POST['L3'])
        N3 = float(request.POST['N3'])
        t3 = float(request.POST['t3'])
        T_exp3 = t3/N3
        F_exp3 = 1/T_exp3
        K3 = (0.8*7.95*100)/L3
        T_th3 = 6.28*m.sqrt(0.32/K3)
        F_th3 = 1/T_th3

        url1 = Post.objects.filter(name__contains = 'To study the torsional vibration (un-damped) of single rotor shaft system').last()

        data = {
            'K1':K1,
            'K2':K2,
            'K3':K3,
            'L1':L1,
            'T_exp1':T_exp1,
            'F_exp1':F_exp1,
            'T_th1':T_th1,
            'F_th1':F_th1,
            'L2':L2,
            'T_exp2':T_exp2,
            'F_exp2':F_exp2,
            'T_th2':T_th2,
            'F_th2':F_th2,
            'L3':L3,
            'T_exp3':T_exp3,
            'F_exp3':F_exp3,
            'T_th3':T_th3,
            'F_th3':F_th3,
            'url1':url1,
        }

        return render(request,'DOM/DOM EXP 7.html',data)

    else:
        url1 = Post.objects.filter(name__contains = 'To study the torsional vibration (un-damped) of single rotor shaft system').last()
    
    return render(request,'DOM/DOM EXP 7.html',{'url1':url1})

def DOMEXP8(request):

    if request.method == 'POST':
        IA1 = float(request.POST['IA1'])
        IB1 = float(request.POST['IB1'])
        N1 = float(request.POST['N1'])
        t1 = float(request.POST['t1'])
        T_exp1 = t1/N1
        T_th1 = 6.28*m.sqrt((IA1*IB1)/(5.89*(IA1+IB1)))

        IA2 = float(request.POST['IA2'])
        IB2 = float(request.POST['IB2'])
        N2 = float(request.POST['N2'])
        t2 = float(request.POST['t2'])
        T_exp2 = t2/N2
        T_th2 = 6.28*m.sqrt((IA2*IB2)/(5.89*(IA2+IB2)))

        IA3 = float(request.POST['IA3'])
        IB3 = float(request.POST['IB3'])
        N3 = float(request.POST['N3'])
        t3 = float(request.POST['t3'])
        T_exp3 = t3/N3
        T_th3 = 6.28*m.sqrt((IA3*IB3)/(5.89*(IA3+IB3)))

        url1 = Post.objects.filter(name__contains = 'To study the free vibration of two rotor system and to determine the natural frequency of vibration theoretically and experimentally').last()

        data = {
            'N1': N1,
            't1':t1,
            'IA1':IA1,
            'IB1':IB1,
            'T_exp1':T_exp1,
            'T_th1':T_th1,
            'N2': N2,
            't2':t2,
            'IA2':IA2,
            'IB2':IB2,
            'T_exp2':T_exp2,
            'T_th2':T_th2,
            'N3': N3,
            't3':t3,
            'IA3':IA3,
            'IB3':IB3,
            'T_exp3':T_exp3,
            'T_th3':T_th3,
            'url1':url1,
        }

        return render(request,'DOM/DOM EXP 8.html',data)


    else:
        url1 = Post.objects.filter(name__contains = 'To study the free vibration of two rotor system and to determine the natural frequency of vibration theoretically and experimentally').last()
    
    return render(request,'DOM/DOM EXP 8.html',{'url1':url1})

def DOMEXP9(request):


    url1 = Post.objects.filter(name__contains = 'To study the damped torsional oscillations and determine the damping coefficient Ct').last()
    
    return render(request,'DOM/DOM EXP 9.html',{'url1':url1})

def DOMEXP10(request):

    if request.method == 'POST':
        W1 = float(request.POST['W1'])
        K1 = float(request.POST['K1'])
        t1 = float(request.POST['t1'])
        T1 = t1/K1
        Fn1 = 1/T1
        fb1 = (3.14/21218)*m.sqrt(16535.736/(W1*W1))
        FL1 = m.sqrt((79371.5328*1000000)/(418401.9856*W1))
        F1 = (1/(FL1*FL1))+(1/(fb1*fb1))

        W2 = float(request.POST['W2'])
        K2 = float(request.POST['K2'])
        t2 = float(request.POST['t2'])
        T2 = t2/K2
        Fn2 = 1/T2
        fb2 = (3.14/21218)*m.sqrt(16535.736/(W2*W2))
        FL2 = m.sqrt((79371.5328*1000000)/(418401.9856*W2))
        F2 = (1/(FL2*FL2))+(1/(fb2*fb2))

        W3 = float(request.POST['W3'])
        K3 = float(request.POST['K3'])
        t3 = float(request.POST['t3'])
        T3 = t3/K3
        Fn3 = 1/T3
        fb3 = (3.14/21218)*m.sqrt(16535.736/(W3*W3))
        FL3 = m.sqrt((79371.5328*1000000)/(418401.9856*W3))
        F3 = (1/(FL3*FL3))+(1/(fb3*fb3))

        x = [F1,F2,F3]
        y = [W1,W2,W3]

        plt.switch_backend('AGG')
        plt.figure(figsize=(5,5))
        plt.title('Relation of 1/F2 v/s W')
        plt.plot(x,y)
        plt.xticks(rotation=45)
        plt.xlabel('1/F2')
        plt.ylabel('W')
        plt.grid()
        plt.tight_layout()
        graph = get_graph()

        url1 = Post.objects.filter(name__contains = 'To verify the Dunkerley’s Rule').last()

        data = {
            'T1':T1,
            'T2':T2,
            'T3':T3,
            'Fn1':Fn1,
            'FL1':FL1,
            'F1':F1,
            'Fn2':Fn2,
            'FL2':FL2,
            'F2':F2,
            'Fn3':Fn3,
            'FL3':FL3,
            'F3':F3,
            'chart':graph,
            'url1':url1
        }

        return render(request,'DOM/DOM EXP 10.html',data)


    else:
        url1 = Post.objects.filter(name__contains = 'To verify the Dunkerley’s Rule').last()
    
    return render(request,'DOM/DOM EXP 10.html',{'url1':url1})

def DOMEXP11(request):

    if request.method == 'POST':
        F1 = float(request.POST['F1'])
        A1 = float(request.POST['A1'])

        F2 = float(request.POST['F2'])
        A2 = float(request.POST['A2'])

        F3 = float(request.POST['F3'])
        A3 = float(request.POST['A3'])

        x = [A1,A2,A3]
        y = [F1,F2,F3]

        plt.switch_backend('AGG')
        plt.figure(figsize=(5,5))
        plt.title('Relation of amplitude v/s frequency for each damping')
        plt.plot(x,y)
        plt.xticks(rotation=45)
        plt.xlabel('amplitude')
        plt.ylabel('frequency')
        plt.grid()
        plt.tight_layout()
        graph = get_graph()

        url1 = Post.objects.filter(name__contains = 'To study the forced lateral vibrations of the beam fir different damping').last()

        data = {
            'chart':graph,
            'url1':url1,
        }

        return render(request,'DOM/DOM EXP 11.html',data)

    else:
        url1 = Post.objects.filter(name__contains = 'To study the forced lateral vibrations of the beam fir different damping').last()
    
    return render(request,'DOM/DOM EXP 11.html',{'url1':url1})

def dashboard(request):
    createdby = request.user.id
    posts = Post.objects.filter(author_id = createdby).order_by('-created_at')
    for i in posts:
        print(i.name)
    return render(request,'dashboard.html',{'posts':posts})

def post_link(request):

    name = request.POST['experiment1']
    formlink = request.POST['link']
    createdby = request.user.id
    post = Post(name = name, formlink = formlink, author_id = createdby)
    post.save()

    return redirect(experiment)

def plot(request):
    # Data for plotting
    #x = np.arange(0.0, 2.0, 0.01)
    #y = 2 + np.cos(2 * np.pi * x)
    val11 = float(request.POST['val11'])
    val12 = float(request.POST['val12'])
    val13 = float(request.POST['val13'])
    val14 = float(request.POST['val14'])
    val15 = float(request.POST['val15'])
    val16 = float(request.POST['val16'])
    val17 = float(request.POST['val17'])
    val18 = float(request.POST['val18'])

    data1 = [val11,val12,val13,val14,val15,val16,val17,val18]
    val1 = large(data1)
    print(val1)

    val21 = float(request.POST['val21'])
    val22 = float(request.POST['val22'])
    val23 = float(request.POST['val23'])
    val24 = float(request.POST['val24'])
    val25 = float(request.POST['val25'])
    val26 = float(request.POST['val26'])
    val27 = float(request.POST['val27'])
    val28 = float(request.POST['val28'])

    data2 = [val21,val22,val23,val24,val25,val26,val27,val28]
    val2 = large(data2)
    print(val2)

    val31 = float(request.POST['val31'])
    val32 = float(request.POST['val32'])
    val33 = float(request.POST['val33'])
    val34 = float(request.POST['val34'])
    val35 = float(request.POST['val35'])
    val36 = float(request.POST['val36'])
    val37 = float(request.POST['val37'])
    val38 = float(request.POST['val38'])

    data3 = [val31,val32,val33,val34,val35,val36,val37,val38]
    val3 = large(data3)
    print(val3)

    val41 = float(request.POST['val41'])
    val42 = float(request.POST['val42'])
    val43 = float(request.POST['val43'])
    val44 = float(request.POST['val44'])
    val45 = float(request.POST['val45'])
    val46 = float(request.POST['val46'])
    val47 = float(request.POST['val47'])
    val48 = float(request.POST['val48'])

    data4 = [val41,val42,val43,val44,val45,val46,val47,val48]
    val4 = large(data4)
    print(val4)

    a = val1-val2
    b = 100 - 50
    c = a/b
    print(c)

    y = [val1,val2,val3,val4]
    x = [50,100,150,200]

    plt.switch_backend('AGG')
    plt.figure(figsize=(5,5))
    plt.title('thermal conductivity')
    plt.plot(x,y)
    plt.xticks(rotation=45)
    plt.xlabel('Distance of thermocouple (mm)')
    plt.ylabel('Temperature (dT)')
    plt.grid()
    plt.tight_layout()
    graph = get_graph()
    return render(request, 'graph.html', {'chart':graph})

#def add(request):
 #   num1 = int(request.POST['num1'])
  #  num2 = int(request.POST['num2'])
   # res1 = num1 +num2
    #res2 = num1-num2
    #res = [res1,res2]
    #print(res)
    #return render(request, 'home.html',{'add':res})
